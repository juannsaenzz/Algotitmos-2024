
#! EJERICIO 4
#! Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

from pila import Stack
from random import randint

pila = Stack()
pilaAux = Stack()

for i in range(10):
    pila.push(randint(1, 99))

while pila.size() > 0:
    data = pila.pop()
    print (data)
    pilaAux.push(data)