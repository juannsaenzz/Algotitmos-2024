
#! EJERCICIO 18

#! Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
#! letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
#! que resuelva las siguientes situaciones:

#! a. cargar 1000 turnos de manera aleatoria a la cola.
#! b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
#! y F, y la cola_2 con el resto de los turnos (B, D y E).
#! c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
#! tiene mayor cantidad.
#! d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
#! mayor que 506.

import random
from queue import Queue

# Función para cargar 1000 turnos aleatorios en la cola
def cargar_turnos(cola):
    for _ in range(1000):
        codigo_turno = random.choice(['A', 'B', 'C', 'D', 'E', 'F']) + str(random.randint(0, 999)).zfill(3)
        cola.put(codigo_turno)

# Función para separar la cola en dos colas diferentes
def separar_colas(cola, cola_1, cola_2):
    while not cola.empty():
        turno = cola.get()
        if turno[0] in ['A', 'C', 'F']:
            cola_1.put(turno)
        else:
            cola_2.put(turno)

# Función para determinar la cola con mayor cantidad de turnos y la letra con más turnos dentro de esa cola
def mayor_cantidad_turnos(cola_1, cola_2):
    cantidad_cola_1 = cola_1.qsize()
    cantidad_cola_2 = cola_2.qsize()

    if cantidad_cola_1 > cantidad_cola_2:
        print("La cola 1 tiene mayor cantidad de turnos.")
        letra_mas_comun = determinar_letra_mas_comun(cola_1)
    elif cantidad_cola_1 < cantidad_cola_2:
        print("La cola 2 tiene mayor cantidad de turnos.")
        letra_mas_comun = determinar_letra_mas_comun(cola_2)
    else:
        print("Ambas colas tienen la misma cantidad de turnos.")
        letra_mas_comun = None
    
    if letra_mas_comun:
        print(f"La letra con mayor cantidad de turnos es: {letra_mas_comun}")

# Función para determinar la letra con más turnos en una cola
def determinar_letra_mas_comun(cola):
    contador_letras = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
    while not cola.empty():
        turno = cola.get()
        letra = turno[0]
        contador_letras[letra] += 1
    
    letra_mas_comun = max(contador_letras, key=contador_letras.get)
    return letra_mas_comun

# Función para mostrar los turnos de la cola con menos elementos cuyo número de turno es mayor que 506
def mostrar_turnos(cola_1, cola_2):
    if cola_1.qsize() < cola_2.qsize():
        cola_menos_elementos = cola_1
    else:
        cola_menos_elementos = cola_2
    
    print("Turnos de la cola con menos elementos y número mayor que 506:")
    print(f"Cola con menos elementos: {cola_menos_elementos.qsize()} elementos")
    while not cola_menos_elementos.empty():
        turno = cola_menos_elementos.get()
        numero_turno = int(turno[1:])  # Obtener los últimos tres dígitos del turno
        if numero_turno > 506:
            print(turno)


# Crear la cola de turnos
cola_turnos = Queue()

# a. Cargar 1000 turnos aleatorios en la cola
cargar_turnos(cola_turnos)

# b. Separar la cola en dos colas diferentes
cola_1 = Queue()
cola_2 = Queue()
separar_colas(cola_turnos, cola_1, cola_2)

# c. Determinar la cola con mayor cantidad de turnos y la letra con más turnos dentro de esa cola
mayor_cantidad_turnos(cola_1, cola_2)

# d. Mostrar los turnos de la cola con menos elementos cuyo número de turno es mayor que 506
mostrar_turnos(cola_1, cola_2)
