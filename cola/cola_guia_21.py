
#! EJERCICIO 21

#! Desarrollar un algoritmo que permita administrar los despegues y aterrizajes de un aeropuer-
#! to que tiene una pista, contemplando las siguientes actividades:

#! a. de cada vuelo se conoce el nombre de la empresa, hora salida, hora llegada, aeropuerto de
#! origen, aeropuerto de destino y su tipo (pasajeros, negocios o carga).
#! b. utilizar una cola para administrar los despegues, se deben cargan ordenados por horario de
#! salida. Otra para los aterrizajes, se deben agregan a medida que arriban al aeropuerto.
#! c. en la pista solo puede haber un avión realizando una maniobra de aterrizaje o despegue.
#! d. se debe permitir agregar vuelos tanto de aterrizaje como de despegue en ambas colas des-
#! pués de realizar una atención.
#! e. se debe atender siempre que se pueda a los elementos de la cola de aterrizaje –dado que son
#! aviones que están sobrevolando en la zona de espera–, salvo que sea el horario de salida del
#! primer avión de la cola de despegue, en ese caso se deberá atender dicho despegue.
#! f. cada tipo de avión tiene su tiempo de uso de la pista para la maniobra de despegue y aterri-
#! zaje –adaptados a segundo para los fines prácticos del ejercicio–:
#! I. pasajeros (aterrizaje = 10 segundos, despegue = 5 segundos);
#! II. negocios (aterrizaje = 5 segundos, despegue = 3 segundos);
#! III. carga (aterrizaje = 12 segundos, despegue = 9 segundos).
#! g. se debe poder cancelar vuelos de despegue y poder reprogramar un vuelo para más tarde
#! cuando se lo atiende para despegar (en esta caso el horario de salida será mayor que el
#! último de la cola).

import heapq
from queue import Queue
import time

# Definir una clase para representar un vuelo
class Vuelo:
    def __init__(self, empresa, hora_salida, hora_llegada, origen, destino, tipo):
        self.empresa = empresa
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
        self.origen = origen
        self.destino = destino
        self.tipo = tipo
    
    def __lt__(self, other):
        return self.hora_salida < other.hora_salida

# Función para cargar vuelos de despegue a la cola, ordenados por hora de salida
def cargar_despegues(cola_despegues, vuelo):
    cola_despegues.put(vuelo)

# Función para cargar vuelos de aterrizaje a la cola, sin orden específico
def cargar_aterrizajes(cola_aterrizajes, vuelo):
    cola_aterrizajes.put(vuelo)

# Función para manejar los despegues y aterrizajes
def gestionar_operaciones(cola_despegues, cola_aterrizajes):
    avion_en_pista = None
    while not cola_despegues.empty() or not cola_aterrizajes.empty() or avion_en_pista:
        if not cola_aterrizajes.empty():
            vuelo_aterrizar = cola_aterrizajes.queue[0]
            if not avion_en_pista or vuelo_aterrizar.hora_salida < avion_en_pista.hora_salida:
                avion_en_pista = vuelo_aterrizar
                print(f"Aterrizando vuelo de {vuelo_aterrizar.empresa} en pista...")
                tiempo_aterrizaje = 10 if vuelo_aterrizar.tipo == 'pasajeros' else 5 if vuelo_aterrizar.tipo == 'negocios' else 12
                time.sleep(tiempo_aterrizaje)
                print(f"Aterrizaje de vuelo de {vuelo_aterrizar.empresa} completado.")
                cola_aterrizajes.get()
                avion_en_pista = None

        if not cola_despegues.empty():
            if not avion_en_pista or cola_despegues.queue[0].hora_salida <= avion_en_pista.hora_salida:
                vuelo_despegar = cola_despegues.queue[0]
                avion_en_pista = vuelo_despegar
                print(f"Despegando vuelo de {vuelo_despegar.empresa} desde pista...")
                tiempo_despegue = 5 if vuelo_despegar.tipo == 'pasajeros' else 3 if vuelo_despegar.tipo == 'negocios' else 9
                time.sleep(tiempo_despegue)
                print(f"Despegue de vuelo de {vuelo_despegar.empresa} completado.")
                cola_despegues.get()
                avion_en_pista = None

# Crear las colas para despegues y aterrizajes
cola_despegues = Queue()
cola_aterrizajes = Queue()

# Ejemplo de vuelos
vuelo1 = Vuelo('American Airlines', 8, 10, 'JFK', 'LAX', 'pasajeros')
vuelo2 = Vuelo('United Airlines', 9, 11, 'ORD', 'LAX', 'negocios')
vuelo3 = Vuelo('FedEx', 10, 12, 'MEM', 'LAX', 'carga')

# Cargar los vuelos en las colas
cargar_despegues(cola_despegues, vuelo1)
cargar_despegues(cola_despegues, vuelo2)
cargar_aterrizajes(cola_aterrizajes, vuelo3)

# Gestionar las operaciones en el aeropuerto
gestionar_operaciones(cola_despegues, cola_aterrizajes)
