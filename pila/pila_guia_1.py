
#! EJERCICIO 1
#! Determinar el número de ocurrencias de un determinado elemento en una pila.

from pila import Stack
from random import randint

pila = Stack()

for i in range(10):
    pila.push(randint(1, 99))

buscado = int(input('Ingrese el numero a buscar: '))
cont = 0

while pila.size() > 0:
    data = pila.pop()
    print (data)
    if data == buscado:
        cont += 1
        
print()
print(f'el elemento {buscado} se repite {cont} veces')
print()