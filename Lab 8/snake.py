import pygame
import random
import time

pygame.init()

# screen sizes and setting screen
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

CELL = 20 # size of cells 20x20


#font option
font_go = pygame.font.SysFont("Times New Roman", 72)
text_go = font_go.render("Game Over", True, "red")
font_s_l = pygame.font.SysFont("Times New Roman", 24)


#sheet (grid)
def draw_grid(color):
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, color, (i * CELL, j * CELL, CELL, CELL), 1)


# function that will display score and level
def display_attribute(score, level):
    font_s_l = pygame.font.SysFont("Times New Roman", 18)
    text_sc = font_s_l.render(f" Score {score} ", True, "black", "white")
    text_lv = font_s_l.render(f" Level {level} ", True, "black", "white")

    screen.blit(text_sc, (3, 3))
    screen.blit(text_lv, (text_sc.get_width() + 5, 3))


# function that will display "Game Over"
def game_over(score, level):
    text_sc = font_s_l.render(f"Score {score}", True, "black")
    text_lv = font_s_l.render(f"Level {level}", True, "black")
    
    screen.fill("gray") 
    screen.blit(text_go, ((WIDTH - text_go.get_width()) // 2, HEIGHT // 2 - text_go.get_height()))
    screen.blit(text_lv, ((WIDTH - text_lv.get_width()) // 2, HEIGHT // 2))
    screen.blit(text_sc, ((WIDTH - text_sc.get_width()) // 2, HEIGHT // 2 + text_sc.get_height()))

    pygame.display.flip() # updates screen
    time.sleep(3) # stops screen to 3 seconds


# POINT 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# SNAKE
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.direction = "RIGHT"
        self.change_to = self.direction
        self.score = 0

    # method for moving of a snake
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # checks direction of button and snakes head to do not intersect with body
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                 self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

        # changes direction
        if self.direction == "RIGHT":
            self.body[0].x += 1
            self.body[0].y += 0
        if self.direction == "LEFT":
            self.body[0].x += -1
            self.body[0].y += 0
        if self.direction == "DOWN":
            self.body[0].x += 0
            self.body[0].y += 1
        if self.direction == "UP":
            self.body[0].x += 0
            self.body[0].y += -1

        # checks the right border
        if self.body[0].x > WIDTH // CELL - 1:
            self.body[0].x = 0
        # checks the left border
        if self.body[0].x < 0:
            self.body[0].x = WIDTH // CELL - 1
        # checks the bottom border
        if self.body[0].y > HEIGHT // CELL - 1:
            self.body[0].y = 0
        # checks the top border
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT // CELL - 1

    # draws snake (head and body parts) in the game
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, (255, 102, 0), (head.x * CELL, head.y * CELL, CELL, CELL), 0, 2)
        for segment in self.body[1:]:
            pygame.draw.rect(screen, (255, 204, 0), (segment.x * CELL, segment.y * CELL, CELL, CELL), 0, 1)
    
    # checks for eating food
    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += 1
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self.body)
        
    # checks for collision with body
    def check_collision_body(self, food):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x != food.pos.x and head.y == segment.y != food.pos.y:
                return True


# FOOD
class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    # draws food
    def draw(self):
        pygame.draw.rect(screen, "forestgreen", (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL), 0, 10)

    # generates food position
    def generate_random_pos(self, body):
        self.pos.x = random.randint(1, WIDTH // CELL - 2) # random number between [1, 28) for x
        self.pos.y = random.randint(1, HEIGHT // CELL - 2) # random number between [1, 28) for y
        for i in range(len(body)):
            # checks if foods position in snakes body
            if body[i].x == self.pos.x and body[i].y == self.pos.y:
                self.generate_random_pos(body)


# LEVEL
class Level:
    def __init__(self):
        self.num = 1
    
    # check score number to change level. Only 3 levels
    def check_score(self, snake):
        if snake.score > 4 and snake.score <= 9:
            self.num = 2
        elif snake.score > 9:
            self.num = 3
        
    # changes design of levels
    def levels(self, snake, food):
        # design for level 2
        if self.num == 2:
            screen.fill("gray")
            
            head = snake.body[0]
            pygame.draw.rect(screen, (48, 45, 255), (head.x * CELL, head.y * CELL, CELL, CELL), 0, 2)
            for segment in snake.body[1:]:
                pygame.draw.rect(screen, (84, 154, 255), (segment.x * CELL, segment.y * CELL, CELL, CELL), 0, 1)
            
            pygame.draw.rect(screen, "yellow", (food.pos.x * CELL, food.pos.y * CELL, CELL, CELL), 0, 10)

        # design for level 3
        else:
            screen.fill((255, 193, 119))
            
            head = snake.body[0]
            pygame.draw.rect(screen, (222, 30, 86), (head.x * CELL, head.y * CELL, CELL, CELL), 0, 2)
            for segment in snake.body[1:]:
                pygame.draw.rect(screen, (255, 82, 40), (segment.x * CELL, segment.y * CELL, CELL, CELL), 0, 1)
            
            pygame.draw.rect(screen, "purple", (food.pos.x * CELL, food.pos.y * CELL, CELL, CELL), 0, 10)

    # changes speed according to level by FPS
    def speed(self):
        if self.num == 2:
            FPS = 7
        elif self.num == 3:
            FPS = 10
        else:
            FPS = 5
        return FPS

            
clock = pygame.time.Clock()

# creates objects
food = Food()
snake = Snake()
level = Level()

# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_to = "RIGHT"
            elif event.key == pygame.K_LEFT:
                snake.change_to = "LEFT"
            elif event.key == pygame.K_DOWN:
                snake.change_to = "DOWN"
            elif event.key == pygame.K_UP:
                snake.change_to = "UP"

    screen.fill("black") # black screen

    draw_grid("black") # grids are black

    snake.move()

    # checks for collision with body
    if snake.check_collision_body(food):
        running = False 
        print(level.num)
        game_over(snake.score, level.num) # shows "Game Over" screen

    # checks collision with food
    snake.check_collision(food)

    # checks score
    level.check_score(snake)

    # draws food and snake, changes background according to level
    if level.num == 1:
        snake.draw()
        food.draw()
    else:
        level.levels(snake, food)
    
    # speed of level
    FPS = level.speed()

    # displaying score and level while playing
    display_attribute(snake.score, level.num)

    pygame.display.flip() # updates screen
    clock.tick(FPS) # Frame numbers per second

pygame.quit()