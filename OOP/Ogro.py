from Enemigo import *

class Ogro(Enemigo):
    def __init__(self, tipo_enemigo, puntos_energia=10, ataque=1):
        super().__init__(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("Ogro aplasta todo!!!")