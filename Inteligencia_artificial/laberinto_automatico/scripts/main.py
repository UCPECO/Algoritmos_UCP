#!/usr/bin/env python3


import laberinto_automatico
import maze_generator
import start_screen
import sys
import copy
from laberintos import *


def main():
    laberinto_dict={'1':Laberinto1,'2':Laberinto2,'3':Laberinto3, '4':Laberinto4, '5':Laberinto5}
    
    if start_screen.menu():
        laberinto=str(start_screen.seleccionar_laberinto())
        retorno = laberinto_automatico.main(copy.deepcopy(laberinto_dict[laberinto]))
        maze_generator.main(copy.deepcopy(laberinto_dict[laberinto]), retorno[0], retorno[1])
        main()



if __name__ == '__main__':
    
    main()
    
    
    
    
    
    
    
