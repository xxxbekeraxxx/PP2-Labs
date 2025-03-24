import pygame
import math
from color_palette import *

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

screen.fill(colorWHITE)
base_layer.fill(colorWHITE)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0

prevX = 0
prevY = 0

color = colorBLACK

def show_options():
    font = pygame.font.SysFont("arial", 18)
    text_rect = font.render(" Rectangle ", True, colorBLACK, colorGRAY)
    text_circle = font.render(" Circle ", True, colorBLACK, colorGRAY)
    text_line = font.render(" Line ", True, colorBLACK, colorGRAY)
    text_erase = font.render(" Eraser ", True, colorBLACK, colorGRAY)

    w1 = text_rect.get_width() + 6
    w2 = text_circle.get_width() + w1 + 3
    w3 = text_line.get_width() + w2 + 3
    w4 = text_erase.get_width() + w3 + 3
        
    pygame.draw.rect(screen, colorWHITE, (0, 0, w4, 51))

    text_rect = screen.blit(text_rect, (3, 3))
    text_circle = screen.blit(text_circle, (w1, 3))
    text_line = screen.blit(text_line, (w2, 3))
    text_erase = screen.blit(text_erase, (w3, 3))

    return text_rect, text_circle, text_line, text_erase


def show_colors():
    rect_red = pygame.draw.rect(screen, colorRED, (3, 27, 21, 21))
    rect_blue = pygame.draw.rect(screen, colorBLUE, (27, 27, 21, 21))
    rect_green = pygame.draw.rect(screen, colorGREEN, (51, 27, 21, 21))
    rect_black = pygame.draw.rect(screen, colorBLACK, (75, 27, 21, 21))
    rect_gray = pygame.draw.rect(screen, colorGRAY, (99, 27, 21, 21))
    rect_yellow = pygame.draw.rect(screen, colorYELLOW, (123, 27, 21, 21))
    return rect_red, rect_blue, rect_green, rect_black, rect_gray, rect_yellow


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


def calculate_radius(x1, y1, x2, y2):
    r = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return int(r)

option = 1

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            if text_rect.collidepoint(event.pos):
                option = 1
                THICKNESS = 5
            elif text_circle.collidepoint(event.pos):
                option = 2
                THICKNESS = 5
            elif text_line.collidepoint(event.pos):
                option = 3
                THICKNESS = 5
            elif text_erase.collidepoint(event.pos):
                option = 4
                currX = event.pos[0]
                currY = event.pos[1]
            
            if rect_red.collidepoint(event.pos):
                color = colorRED
            elif rect_blue.collidepoint(event.pos):
                color = colorBLUE
            elif rect_green.collidepoint(event.pos):
                color = colorGREEN
            elif rect_black.collidepoint(event.pos):
                color = colorBLACK
            elif rect_gray.collidepoint(event.pos):
                color = colorGRAY
            elif rect_yellow.collidepoint(event.pos):
                color = colorYELLOW
            
            prevX = event.pos[0]
            prevY = event.pos[1]
            

        if event.type == pygame.MOUSEMOTION:
            # print("Position of the mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                screen.blit(base_layer, (0, 0))
                if option == 1:
                    pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif option == 2:
                    r = calculate_radius(prevX, prevY, currX, currY)
                    pygame.draw.circle(screen, color, calculate_rect(prevX, prevY, currX, currY).center, r, THICKNESS)
                elif option == 3:
                    pygame.draw.line(screen, color, (prevX, prevY), (currX, currY), THICKNESS)
                elif option == 4:
                    pygame.draw.circle(screen, colorWHITE, (currX, currY), THICKNESS * 3)
                    base_layer.blit(screen, (0, 0))
                    pygame.draw.circle(screen, colorBLACK, (currX, currY), THICKNESS * 3, 3)
                

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if option == 1:
                pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif option == 2:
                r = calculate_radius(prevX, prevY, currX, currY)
                pygame.draw.circle(screen, color, calculate_rect(prevX, prevY, currX, currY).center, r, THICKNESS)
            elif option == 3:
                pygame.draw.line(screen, color, (prevX, prevY), (currX, currY), THICKNESS)
            elif option == 4:
                pygame.draw.circle(screen, colorWHITE, (currX, currY), THICKNESS * 3, 3)
                
            
            base_layer.blit(screen, (0, 0))


        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS and THICKNESS > 1:
                print("reduced thickness")
                THICKNESS -= 1
        

    text_rect, text_circle, text_line, text_erase = show_options()

    rect_red, rect_blue, rect_green, rect_black, rect_gray, rect_yellow = show_colors()

    pygame.display.flip()
    clock.tick(60)