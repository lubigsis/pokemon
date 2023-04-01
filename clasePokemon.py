import random 


#----------creamos la clase Pokemon (dejar 2 espacios en blanco antes/después)
class Pokemon:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = 100

    def gano(self):
        print(f'{self.nombre} GANÓ LA BATALLA')
