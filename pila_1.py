
#! Determinar el número de ocurrencias de un determinado elemento en una pila.

from pila import Stack
from random import randint

pila = Stack()

for i in range(10):
    pila.push(randint(1, 99))