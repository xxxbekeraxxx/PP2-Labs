import pygame
import math
import time

pygame.init()

width = 700
height = 500
center = (width // 2, height // 2)

screen = pygame.display.set_mode((width, height))

img_clock = pygame.image.load("clock.png")
img_clock = pygame.transform.scale(img_clock, (width, height))

img_min_hand = pygame.image.load("min_hand.png")
img_min_hand = pygame.transform.scale(img_min_hand, (750, 300))

img_sec_hand = pygame.image.load("sec_hand.png")
img_sec_hand = pygame.transform.scale(img_sec_hand, (600, 300))

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(img_clock, (0, 0))
    
    current_time = time.localtime()
    minutes = current_time.tm_min 
    seconds = current_time.tm_sec 
    
    min_angle = (minutes % 60) * 6 + 60
    sec_angle = (seconds % 60) * 6 - 50
    
    rotate_min_hand = pygame.transform.rotate(img_min_hand, -min_angle)
    rotate_sec_hand = pygame.transform.rotate(img_sec_hand, -sec_angle)
    
    rect_min = rotate_min_hand.get_rect(center=center)
    rect_sec = rotate_sec_hand.get_rect(center=center)
    
    screen.blit(rotate_min_hand,  rect_min.topleft)
    screen.blit(rotate_sec_hand, rect_sec.topleft)
    
    pygame.display.flip()
    clock.tick(60)