
#! EJERCICIO 3
#! Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar
#! si es un palíndromo.

from cola import Queue
from pila import Stack
from random import randint

cola = Queue()
pila = Stack()


def es_palindromo(palabra):
    palabra = palabra.upper()
    for char in palabra:
        cola.arrive(char)
        pila.push(char)
        
    while cola.size() > 0 and pila.size() > 0:
        if cola.attention() != pila.pop():
            return False
    
    return True

palabra = input('Ingrese una palabra: ')

if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")