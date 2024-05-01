
#! EJERCICIO 4
#! Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.

from random import randint

lista = []
for i in range(10):
    lista.append(randint(1,99))

print('Listado')
for elemento in lista:
    print(elemento)

num_insertar = int(input('Ingrese el numero a insertar: '))
pos_insertar = int(input('Ingrese la posicion: '))

if pos_insertar < 0 or pos_insertar > len(lista):
    print('POSICION NO VALIDA')
else:
    lista.insert(pos_insertar, num_insertar)
    print()
    print(f'Listado con {num_insertar} en la posicion {pos_insertar}')
    for elemento in lista:
        print(elemento)