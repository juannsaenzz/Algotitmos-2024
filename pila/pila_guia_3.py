
#! EJERCICIO 3
#! Reemplazar todas las ocurrencias de un determinado elemento en una pila.

from pila import Stack
from random import randint

pila = Stack()
pilaAux = Stack()

for i in range(10):
    pila.push(randint(1, 99))

elemento = int(input('Ingrese el elemento a reemplazar: '))
reemplazo = int(input('Ingrese el elemento que reemplaza al otro: '))

while pila.size() > 0:
    data = pila.pop()
    print (data)
    if data == elemento:
        pilaAux.push(reemplazo)
    else:
        pilaAux.push(data)

while pilaAux.size() > 0:
    pila.push(pilaAux.pop())   