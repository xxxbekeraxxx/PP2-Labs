import pygame
import random
import time

pygame.init()


# set screen
WIDTH = 400
HEIGTH = 600
screen = pygame.display.set_mode((WIDTH, HEIGTH))
running = True


# loading images
image_bg = pygame.image.load("resources/AnimatedStreet.png")
image_player = pygame.image.load("resources/Player.png")
image_enemy = pygame.image.load("resources/Enemy.png")
image_coin = pygame.image.load("resources/coin.png")
image_coin = pygame.transform.scale(image_coin, (40, 40)) # scale coin to need size


# loading sounds
# sound_bg = pygame.mixer.music.load("resources/background.wav")
# sound_crash = pygame.mixer.Sound("resources/crash.wav")
# pygame.mixer.music.play(-1) # loop for background sound


# class for player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGTH)
        self.speed = 5
    
    # method to moving player car
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 40:
            self.rect = self.rect.move(-self.speed, 0)

        if keys[pygame.K_RIGHT]  and self.rect.right < WIDTH - 40:
            self.rect = self.rect.move(self.speed, 0)


# class for enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, WIDTH - 60), 0)
        self.speed = 7

    # method to moving enemy car
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGTH:
            self.random_position()

    # random position for enemy car
    def random_position(self):
        self.rect.x = random.randint(60, WIDTH - 60)
        self.rect.y = 0


# class for coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, WIDTH - 60), 0)
        self.speed = 4
        self.weight = random.randint(1, 5)
    
    # method to moving for coin
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGTH:
            self.random_position()

    # random position for coin
    def random_position(self):
        self.rect.x = random.randint(60, WIDTH - 60)
        self.rect.y = 0
    
    # random weight for coin
    def random_weight(self):
        self.weight = random.randint(1, 5)


# creating objects
player = Player()
enemy = Enemy()
coin = Coin()

# do group of objects
sprites_all = pygame.sprite.Group()
sprites_enemy = pygame.sprite.Group()
sprites_coin = pygame.sprite.Group()

# adding elements to group
sprites_all.add([player, enemy, coin])
sprites_enemy.add([enemy])
sprites_coin.add([coin])

score = 0 # variable to store sum of collected coins


# texts in the game
font_game_over = pygame.font.SysFont("comicsansms", 72)
text_game_over = font_game_over.render("Game Over", True, "black")
font_score = pygame.font.SysFont("san serif", 28)
font_coin_weight = pygame.font.SysFont("arial", 24)


# frames per sec
clock = pygame.time.Clock()
FPS = 60


# game loop
while running:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.blit(image_bg, (0, 0)) # setting background image
    

    # ability of moving for each objects
    player.move()
    enemy.move()
    coin.move()

    # shows score number in the game
    text_score = font_score.render(f"Score: {score}", True, "black")
    screen.blit(text_score, (WIDTH - text_score.get_width() - 10, 5))


    # show objects in group
    for item in sprites_all:
        screen.blit(item.image, item.rect)


    # enemy and player collide
    if pygame.sprite.spritecollideany(player, sprites_enemy):
        # sound_crash.play() # play crash sound
        time.sleep(1) # screen stops for a second

        screen.fill("red") # screen  fills to red

        # display phrase "Game Over" and score
        screen.blit(text_game_over, ((WIDTH - text_game_over.get_width()) // 2 , HEIGTH // 2 - text_game_over.get_height()))
        screen.blit(text_score, ((WIDTH - text_score.get_width()) // 2 , HEIGTH // 2))
        
        pygame.display.flip() # update screen
        
        time.sleep(3) # screen stops for a 3 seconds
        running = False # game loop ends and window closes

    # player face coin
    if pygame.sprite.spritecollideany(player, sprites_coin):
        coin.random_position() # coin occurs at another position
        coin.random_weight() # coin will have another weight
        score += coin.weight # score increases

    # increasing speed of enemy
    enemy.speed = 7 + (score // 10)
        
    # showing weight of coin 
    text_coin_weight = font_coin_weight.render(f"{coin.weight}", True, "sienna") 
    screen.blit(text_coin_weight, (coin.rect.centerx - 5, coin.rect.centery - 14))

    pygame.display.flip() # update screen
    clock.tick(FPS) # 60 frames per sec

pygame.quit()