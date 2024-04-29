
#! EJERCICIO 2
#! Utilizando operaciones de cola y pila, invertir el contenido de una cola.

from cola import Queue
from pila import Stack
from random import randint

cola = Queue()
pila = Stack()

for i in range(10):
    cola.arrive(randint(1,99))

for i in range(cola.size()):
    data = cola.attention()
    print(data)
    pila.push(data)

print()

while pila.size() > 0:
        data = pila.pop()
        cola.arrive(data)

for i in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()