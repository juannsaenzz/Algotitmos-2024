
#! EJERCICIO 14

#! Un grupo de amigos se reúnen a jugar un juego de dados, suponga que dichos jugadores están
#! cargados en una lista de acuerdo a un número asignado de manera aleatoria y su nombre. De-
#! sarrollar un algoritmo que contemple las siguientes condiciones:

#! a. simular la tirada de un dado –de seis lados D6– en cada turno del jugador;
#! b. el orden de turno de los jugadores es el mismo en el que están cargados en la lista;
#! c. después de que tira el último jugador de la lista debe seguir el primero;
#! d. el juego termina cuando uno de los jugadores saca un 5, en ese caso mostrar su nombre;
#! e. Debe modificar el TDA para implementar lista circular.

import random

def simular_tirada_dado():
    return random.randint(1, 6)

def jugar_dados(jugadores):
    while True:
        for jugador in jugadores:
            tirada = simular_tirada_dado()
            print(f"{jugador} tiró el dado y obtuvo: {tirada}")
            if tirada == 5:
                print(f"¡{jugador} ha sacado un 5! El juego ha terminado.")
                return

# Ejemplo de uso
jugadores = ["Juan", "Pedro", "María", "Ana"]
jugar_dados(jugadores)
