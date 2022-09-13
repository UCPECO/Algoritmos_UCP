#!/usr/bin/env python3
import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Laberinto automático por UCP')
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
font = pygame.font.SysFont(None, 30)
font2 = pygame.font.SysFont(None, 60)
x, y=screen.get_size()
half_x=int(x/2)
half_y=int(y/2)

def texto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)
 
global click, screen_rect
click = False
screen_rect = screen.get_rect()

def seleccionar_laberinto():
    click=False
    while True: 
        screen.fill((0,0,0))

 
        mx, my = pygame.mouse.get_pos()
        
        button_1 = pygame.Rect((half_x-100), (half_y-half_y*0.4), 200, 50)
        button_2 = pygame.Rect((half_x-100), (half_y-half_y*0.2),200, 50)
        button_3 = pygame.Rect((half_x-100), (half_y),200, 50)
        button_4 = pygame.Rect((half_x-100), (half_y+half_y*0.2),200, 50)
        button_5 = pygame.Rect((half_x-100), (half_y+half_y*0.4),200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                return 1
        if button_2.collidepoint((mx, my)):
            if click:
                return 2
        if button_3.collidepoint((mx, my)):
            if click:
                return 3
        if button_4.collidepoint((mx, my)):
            if click:
                return 4
        if button_5.collidepoint((mx, my)):
            if click:
                return 5                                                                 
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        pygame.draw.rect(screen, (255, 0, 0), button_5)
 
        texto('Laberinto 1', font, (255,255,255), screen, (button_1.centerx), (button_1.centery))
        texto('Laberinto 2', font, (255,255,255), screen, (button_2.centerx), (button_2.centery))
        texto('Laberinto 3', font, (255,255,255), screen, (button_3.centerx), (button_3.centery))
        texto('Laberinto 4', font, (255,255,255), screen, (button_4.centerx), (button_4.centery))
        texto('Laberinto 5', font, (255,255,255), screen, (button_5.centerx), (button_5.centery))
        texto('Seleccione el laberinto', font2, (255,255,255), screen, (button_1.centerx), (half_y-300))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
    
    
    

def menu():
    click=False   
    while True:
   
 
        screen.fill((0,0,0))
        ucp_logo=pygame.transform.scale(pygame.image.load("../images/nobg_logo.png"), (half_y*0.6, half_y*0.6))
        screen.blit(ucp_logo, (((half_x-half_y*0.3), (half_y+half_y*0.3))))

        mx, my = pygame.mouse.get_pos()
        


        button_1 = pygame.Rect((half_x-100), (half_y-half_y*0.2), 200, 50)
        button_2 = pygame.Rect((half_x-100), (half_y),200, 50)
        
        
        if button_1.collidepoint((mx, my)):
            if click:
                return True
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
                return False             
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        texto('Empezar', font, (255,255,255), screen, (button_1.centerx), (button_1.centery))
        texto('Salir', font, (255,255,255), screen, (button_1.centerx), (button_2.centery))
        texto('Bienvenidos', font2, (255,255,255), screen, (button_1.centerx), (half_y-half_y*0.4))


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)


