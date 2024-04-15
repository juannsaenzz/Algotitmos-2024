
#! Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.

from pila import Stack
from random import randint

pila = Stack()
pilaAux = Stack()

for i in range(10):
    pila.push(randint(1, 99))

while pila.size() > 0:
    data = pila.pop()
    print (data)
    if data % 2 == 0:
        pilaAux.push(data)
        
while pilaAux.size() > 0:
    pila.push(pilaAux.pop())
    
print()
print(pila.size())