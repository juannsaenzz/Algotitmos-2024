
#! EJERCICIO 5
#! Dada una lista de números enteros eliminar de estas los números primos.

from random import randint

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

lista = []
for i in range(10):
    lista.append(randint(1,99))

print('Listado')
for elemento in lista:
    print(elemento)

for elemento in lista:
    if es_primo(elemento):
        lista.remove(elemento)

print()
print('Listado sin numeros primos')
for elemento in lista:
    print(elemento)