#!/usr/bin/env python3
     
class Bot:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.fil_bot, self.col_bot = self.posicion_inicial("R")
        self.inicio_bot=self.posicion_inicial("R")
        self.visitados = []
        self.caminos = []
        self.obj_movimientos = []
        self.obj_actual = None
        self.movimiento = None
        self.encontrado = -1
        self.origen = None       

    def posicion_inicial(self, letra):
        for i in self.laberinto:
            if letra in i:
                return (self.laberinto.index(i), i.index(letra))
            else:
                continue

    def imp_camino(self):
        for i in self.laberinto:
            for j in i:
                print(j + ' ', end="")
            print("")

    def movimientos(self):
        self.fil_actual, self.col_actual = (self.fil_bot, self.col_bot)
        self.origen = self.obj_actual            
        self.derecha = (self.fil_actual, self.col_actual + 1)
        self.izquierda = (self.fil_actual, self.col_actual - 1)
        self.arriba = (self.fil_actual - 1, self.col_actual)
        self.abajo = (self.fil_actual + 1, self.col_actual)
        tup_movimientos = (self.derecha, self.izquierda, self.arriba, self.abajo)
        if (self.fil_actual, self.col_actual) in self.visitados:
            return
        else:
            self.visitados.append((self.fil_actual, self.col_actual))

        for movimiento in tup_movimientos:           
            if movimiento[0] > -1 and movimiento[1] > -1:
                try:
                    if self.laberinto[movimiento[0]][movimiento[1]] == "X":
                        self.encontrado = 1
                        self.movimiento = Arbol((self.fil_actual, self.col_actual))
                        self.movimiento.añadir_origen(movimiento, self.origen)
                        return

                    elif self.laberinto[movimiento[0]][movimiento[1]] == " ":
                        if not movimiento in self.visitados:
                            self.movimiento = Arbol((self.fil_actual, self.col_actual))
                            self.caminos.insert(0, movimiento)
                            self.obj_movimientos.insert(0, self.movimiento)
                            self.movimiento.añadir_origen(movimiento, self.origen)
                        else:
                            continue
                    else:
                        continue
                except IndexError:
                    continue
            else:
                continue

        if self.encontrado == -1:
            if len(self.caminos) > 0:
                self.mover_siguiente()
                self.movimientos()
            else:
                self.movimientos()         

    def mover_siguiente(self):
        if self.caminos[-1] in self.visitados:
            return 
        else:
            self.fil_bot, self.col_bot = self.caminos.pop()
            self.obj_actual = self.obj_movimientos.pop()
    
    def insertar_recorrido(self):
        recorridos = self.movimiento.obtener_recorrido()
        if self.encontrado == -1:
            pass
            #print(-1)
        else:
            pasos = len(recorridos) + 2
            #print(pasos)
        for recorrido in recorridos:
            self.laberinto[recorrido[0]][recorrido[1]] = '*'           
        return (recorridos, self.inicio_bot) 
    
class Arbol:
    def __init__(self, posicion):
        self.origen = None
        self.posicion = posicion

    def añadir_origen(self, camino, origen):
        self.origen = origen
        
    def obtener_recorrido(self, recorridos = []):   
        if self.origen != None:
            recorridos.append(self.posicion)
            return self.origen.obtener_recorrido(recorridos)
        else:
             pass
        return recorridos

def main(laberinto):
    camino = Bot(laberinto)
    camino.movimientos()
    retorno=camino.insertar_recorrido()
    #camino.imp_camino() 
    return retorno
    








