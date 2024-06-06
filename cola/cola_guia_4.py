
#! EJERCICIO 4

#! Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.

from cola import Queue
import random

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def eliminar_no_primos(cola):
    primos = Queue()
    while cola.size() > 0:
        numero = cola.attention()
        if es_primo(numero):
            primos.arrive(numero)
    return primos


# Generar una cola de números aleatorios
cola_numeros = Queue()
for _ in range(10):
    cola_numeros.arrive(random.randint(1, 100))

print("Cola original:", cola_numeros._Queue__elements)

# Eliminar los números no primos
cola_primos = eliminar_no_primos(cola_numeros)

print("Cola de primos:", cola_primos._Queue__elements)
