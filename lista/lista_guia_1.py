
#! EJERCICIO 1
#! Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.

from random import randint

lista = []
for i in range(10):
    lista.append(randint(1,99))

print('Listado')
for elemento in lista:
    print(elemento)

print(f'Cantidad de elementos de la lista: {len(lista)}')