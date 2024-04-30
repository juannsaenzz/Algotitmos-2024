
#! EJERCICIO 2
#! Diseñar un algoritmo que elimine todas las vocales que se encuentren
#! en una lista de caracteres.

from random import randint

lista = []
for i in range(10):
    lista.append(chr(randint(65, 90)))

print('Listado')
for elemento in lista:
    print(elemento)

vocales = ['A', 'E', 'I', 'O', 'U']

for elemento in lista:
    if elemento in vocales:
        lista.remove(elemento)

print()
print('Listado sin vocales')
for elemento in lista:
    print(elemento)