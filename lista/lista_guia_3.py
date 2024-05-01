
#! EJERCICIO 3
#! Dada una lista de números enteros, implementar un algoritmo para dividir dicha
#! lista en dos, una que contenga los números pares y otra para los números impares.

from random import randint

def es_par(numero):
    return numero % 2 == 0

def es_impar(numero):
    return numero % 2 != 0

lista = []
for i in range(10):
    lista.append(randint(1,99))

print('Listado')
for elemento in lista:
    print(elemento)

lista_pares = []
lista_impares = []

for elemento in lista:
    if es_par(elemento):
        lista_pares.append(elemento)
    elif es_impar(elemento):
        lista_impares.append(elemento)

print()
print('Listado numeros pares')
for elemento in lista_pares:
    print(elemento)

print()
print('Listado numeros impares')
for elemento in lista_impares:
    print(elemento)