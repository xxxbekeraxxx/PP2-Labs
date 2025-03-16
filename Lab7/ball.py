import pygame

pygame.init()

width, height = 700, 500
x = width // 2
y = height // 2
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
radius = 25

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - radius > 0:
        y -= 20

    if keys[pygame.K_DOWN] and y + radius < height:
        y += 20

    if keys[pygame.K_RIGHT] and x + radius < width:
        x += 20

    if keys[pygame.K_LEFT] and  x - radius > 0:
        x -= 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()
    clock.tick(60)