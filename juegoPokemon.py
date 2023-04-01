import random 

#----------creamos la clase Pokemon (dejar 2 espacios en blanco antes/después)
class Pokemon:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = 100

    def gano(self):
        print(f'{self.nombre} ganó esta batalla')


#------creamos los objetos de la clase Pokemon
pokemon1 = Pokemon('Pikachu', 60)
pokemon2 = Pokemon('Jigglypuff', 55)


#------funcion aleatoria para el turno de los pokemones
def tirar_dado(num):
    return random.randint(1, num)
    

#-------------------inicializamos valores antes de que empiece el juego----------------------------------
##lo que va a continuación ponerlo dsp en un ciclo infinito, pq tiene q incializarse cada vez q empieza el juego.
pokemon1.vida = 100
pokemon2.vida = 100
turno = tirar_dado(2) #un dado de 2 caras


#---------------------------
print('¡Ha iniciado la batalla!\n'.upper())
print(f'{pokemon1.nombre} se enfrenta a {pokemon2.nombre}\n')

#------------------------------ciclo de ataque por turnos-------------------------
while pokemon1.vida > 0 and pokemon2.vida > 0:
    if turno == 1:
        pokemon2.vida = pokemon2.vida - pokemon1.ataque
        turno = 2
        print(f'{pokemon1.nombre} ataca; {pokemon2.nombre} ahora tiene {pokemon2.vida} de vida.')
        print('...Próxima ronda...\n')
    else:
        pokemon1.vida = pokemon1.vida -pokemon2.ataque
        turno = 1
        print(f'{pokemon2.nombre} ataca; {pokemon1.nombre} ahora tiene {pokemon1.vida} de vida.')
        print('...Próxima ronda...\n')


#---------consultamos si el pokemon 1 perdió
if pokemon1.vida <= 0:
    pokemon2.gano()
else:
    pokemon1.gano()



#quitar el 'próxima ronda' del final
#poner un timer de string
#Agregar un ciclo infinito que nos permita iniciar más batallas
#------------------------
#que la clase Pokemon esté en un módulo específico (ponerla en otro archivo, el actual es el archivo del juego)
#------------------------
#Agregar más pokemones y permotir al usuario cuál usar
#No pueden usar el mismo Pokemón los 2 jugadores
#Agragr clases a los pokemones (Tierra, Electricidad, Fuego, Agua) y darle a cada clase superioridad ante otras clases.
#por ejemplo: si pokemon 1 es de agua y pokemon 2 es de fuego; que el pokemon 1 le reste ataque por 1.5
#Y si el Pokemon de fuego ataca al de agua, que le primero tenga un 25% menos de efectividad en el ataque (en vez de restas 100, que reste solo un 75 0> es decir, un 25% menos nomas)