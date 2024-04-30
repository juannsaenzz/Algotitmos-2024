
#! EJERCICIO 3
#! Dada una lista de números enteros, implementar un algoritmo para dividir dicha
#! lista en dos, una que contenga los números pares y otra para los números impares.

from random import randint

lista = []
for i in range(10):
    lista.append(randint(1,99))

print('Listado')
for elemento in lista:
    print(elemento)

lista_pares = []
lista_impares = []

for elemento in lista:
    if elemento % 2 == 0:
        lista_pares.append(elemento)
    else:
        lista_impares.append(elemento)

print()
print('Listado numeros pares')
for elemento in lista_pares:
    print(elemento)

print()
print('Listado numeros impares')
for elemento in lista_impares:
    print(elemento)