#!/usr/bin/env python3

import os
import pygame
import random
import sys
import time
from pygame.locals import *

class Bot_pygame:
    def __init__(self):
        pass

    def mover_bot(self, position):
        Pygame_ob.laberinto[position[0]][position[1]]='R'
        return (position[0], position[1])
        
    def limpiar(self, last):
        Pygame_ob.laberinto[last[0]][last[1]]=' '
              
class Wall:
    def __init__(self, pos):
        paredes.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], width, width)

class Pygame_utils:
    def __init__(self, laberinto):
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.display.set_caption("Laberinto automático UCP")
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.x, self.y=self.screen.get_size()        
        self.laberinto=laberinto
        self.end_rect=None
        self.counter=0
        
    def get_width(self):
        width=int(self.y/y_len)
        while width*x_len > self.x:    
            width=int(width*0.99)
        return width
          
     
    def define_laberinto(self):
        self.bot_rect_list=[]

        y = (self.y/2)-(y_len/2)*width
        x = (self.x/2)-(x_len/2)*width
        for row in self.laberinto:
            for col in row:
                if col == "#":
                    Wall((x, y))
                elif col == "X":
                    self.end_rect=pygame.Rect(x, y, width, width)
                elif col == "R":
                    if (self.counter % 2) == 0:
                        self.bot_rect_list.append([pygame.transform.scale(pygame.image.load("../images/benderdos.png"), (width, width)),(x,y)])
                    else:
                        self.bot_rect_list.append([pygame.transform.scale(pygame.image.load("../images/benderuno.png"), (width, width)), (x,y)])
                    self.counter+=1
                x += width                
            y += width
            x = (self.x/2)-(x_len/2)*width
    
    def rendering(self):
        self.screen.fill((0,0,0))
        for wall in paredes:
            pygame.draw.rect(self.screen, (255, 255, 255), wall.rect)
        for bot in self.bot_rect_list:
            
            self.screen.blit(bot[0], (bot[1][0],bot[1][1]))
        try:
            pygame.draw.rect(self.screen, (255, 0, 0), self.end_rect)
        except:
            pass
        pygame.display.flip()
        time.sleep(0.4)
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()       
                        
    def completado(self):
        self.screen.fill((0,0,0))
        width=self.y*0.60
        font = pygame.font.SysFont(None, 60)
        textobj = font.render("¡Completado!", 1, (255,255,255))
        bender=pygame.transform.scale(pygame.image.load("../images/bender_final.png"), (width, width))
        textrect = textobj.get_rect()
        textrect.center = ((self.x/2), (self.y/2-(width/2)*1.2))
        self.screen.blit(textobj, textrect)
        self.screen.blit(bender,((self.x/2-width/2), (self.y/2-width/2)))
        pygame.display.flip()
        time.sleep(2)
   
   
    def run(self):
        self.define_laberinto()  

def main(laberinto, recorrido, inicio_bot):
    global paredes, Pygame_ob, Bot_game, width, x_len, y_len
    paredes=[]
    x_len=len(laberinto[0])
    y_len=len(laberinto)


    Pygame_ob=Pygame_utils(laberinto)
    width=Pygame_ob.get_width()
    Bot_game=Bot_pygame()
    
    Pygame_ob.define_laberinto()
    Pygame_ob.rendering()
    ultima_posicion=(inicio_bot[0], inicio_bot[1])
    for i in range(len(recorrido)):
        Bot_game.limpiar(ultima_posicion)   
        ultima_posicion=Bot_game.mover_bot(recorrido.pop())
        Pygame_ob.define_laberinto()
    
        Pygame_ob.rendering()
    
    Pygame_ob.completado()
    


