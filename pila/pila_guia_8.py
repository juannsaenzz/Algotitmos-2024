
#! EJERCICIO 8

#! Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
#! cartas de baraja española–,resolver las siguientes actividades:

#! a. generar las cartas del mazo de forma aleatoria;
#! b. separar la pila mazo en cuatro pilas una por cada palo;
#! c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.

import random

class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)

    def __iter__(self):
        return iter(self.__elements)

def generar_mazo():
    mazo = Stack()
    palos = ['espada', 'basto', 'copa', 'oro']
    for palo in palos:
        for numero in range(1, 13):
            mazo.push((numero, palo))
    mazo_mezclado = list(mazo)  # Convertir la pila en una lista
    random.shuffle(mazo_mezclado)  # Mezclar el mazo de forma aleatoria
    mazo_mezclado_pila = Stack()  # Convertir la lista mezclada en una nueva pila
    for carta in mazo_mezclado:
        mazo_mezclado_pila.push(carta)
    return mazo_mezclado_pila

def separar_por_palo(mazo):
    palos_pilas = {'espada': Stack(), 'basto': Stack(), 'copa': Stack(), 'oro': Stack()}
    while mazo.size() > 0:
        carta = mazo.pop()
        palos_pilas[carta[1]].push(carta)
    return palos_pilas

def ordenar_pila_por_numero(pila):
    temp_pila = Stack()
    while pila.size() > 0:
        temp_pila.push(pila.pop())
    temp_lista = []
    while temp_pila.size() > 0:
        temp_lista.append(temp_pila.pop())
    temp_lista.sort()  # Ordenar las cartas por número
    for carta in temp_lista:
        pila.push(carta)

# Ejemplo de uso:
mazo = generar_mazo()
print("Mazo generado aleatoriamente:", [carta for carta in mazo])

pilas_por_palo = separar_por_palo(mazo)
for palo, pila in pilas_por_palo.items():
    print("Pila de", palo, ":", [carta for carta in pila])

palo_a_ordenar = 'espada'
ordenar_pila_por_numero(pilas_por_palo[palo_a_ordenar])
print("Pila de", palo_a_ordenar, "ordenada:", [carta for carta in pilas_por_palo[palo_a_ordenar]])

