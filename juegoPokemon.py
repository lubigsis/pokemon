from clasePokemon import Pokemon
import time, random


#------creamos los objetos de la clase Pokemon
pokemon1 = Pokemon('Pikachu', 60)
pokemon2 = Pokemon('Jigglypuff', 55)
pokemon3 = Pokemon('Bulbasaur', 50)
pokemon4 = Pokemon ('Charizard', 65)

#------funcion aleatoria para el turno de los pokemones
def tirar_dado(num):
    return random.randint(1, num)
    

#-------------------inicializamos valores antes de que empiece el juego----------------------------------
pokemon1.vida = 100
pokemon2.vida = 100
pokemon3.vida = 100
pokemon4.vida = 100
turno = tirar_dado(2) #un dado de 2 caras   

#--------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------INICIO--------------------------------------------
print('Hola, jugador. Elige tu Pokémon y ¡prepárate para el combate!\n\n')
time.sleep(2)
print('Pikachu, escribe: 1')
time.sleep(2)
print('Jigglypuff, escribe: 2')
time.sleep(2)
print('Bulbasaur, escribe: 3')
time.sleep(2)
print('Charizard, escribe: 4\n')
time.sleep(2)

print('Elijo la opción número:')
respuestaJugador = int(input())

if respuestaJugador == 1:
    respuestaJugador = pokemon1.nombre
elif respuestaJugador == 2:
    respuestaJugador = pokemon2.nombre
elif respuestaJugador == 3:
    respuestaJugador = pokemon3.nombre   
elif respuestaJugador == 4:
    respuestaJugador = pokemon4.nombre
  


print('¡Ha iniciado la batalla!\n'.upper())
time.sleep(2)
print(f'{respuestaJugador} se enfrenta a {pokemon2.nombre}\n')

#------------------------------ciclo de ataque por turnos-------------------------
while pokemon1.vida > 0 and pokemon2.vida > 0:
    if turno == 1:
        pokemon2.vida = pokemon2.vida - pokemon1.ataque
        turno = 2
        time.sleep(2)
        print(f'{pokemon1.nombre} ataca; {pokemon2.nombre} ahora tiene {pokemon2.vida} de vida.')
        print('...Próxima ronda...\n')
        time.sleep(2)
        
    else:
        pokemon1.vida = pokemon1.vida - pokemon2.ataque
        turno = 1
        time.sleep(2)
        print(f'{pokemon2.nombre} ataca; {pokemon1.nombre} ahora tiene {pokemon1.vida} de vida.')
        print('...Próxima ronda...\n')
        time.sleep(2)
        


#---------consultamos si el pokemon 1 perdió
if pokemon1.vida <= 0:
    pokemon2.gano()
else:
    pokemon1.gano()


#Poner opcion random para pc y que no sea la opción que eligió el jugador.
#Agregar un ciclo infinito que nos permita iniciar más batallas
#quitar el 'próxima ronda' del final
#------------------------

#No pueden usar el mismo Pokemón los 2 jugadores
#Agragar clases a los pokemones (Tierra, Electricidad, Fuego, Agua) y darle a cada clase superioridad ante otras clases.
#por ejemplo: si pokemon 1 es de agua y pokemon 2 es de fuego; que el pokemon 1 le reste ataque por 1.5
#Y si el Pokemon de fuego ataca al de agua, que le primero tenga un 25% menos de efectividad en el ataque (en vez de restas 100, que reste solo un 75 0> es decir, un 25% menos nomas)