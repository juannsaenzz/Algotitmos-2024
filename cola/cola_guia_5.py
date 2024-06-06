
#! EJERCICIO 5

#! Utilizando operaciones de cola y pila, invertir el contenido de una pila.

from cola import Queue
from pila import Stack

def invertir_pila(pila):
    cola = Queue()

    # Vaciar la pila en la cola
    while pila.size() > 0:
        elemento = pila.pop()
        cola.arrive(elemento)

    # Vaciar la cola en una nueva pila
    nueva_pila = Stack()
    while cola.size() > 0:
        elemento = cola.attention()
        nueva_pila.push(elemento)

    return nueva_pila


# Ejemplo de uso
pila_original = Stack()
for i in range(1, 6):
    pila_original.push(i)

print("Pila original:", pila_original._Stack__elements)

pila_invertida = invertir_pila(pila_original)

print("Pila invertida:", pila_invertida._Stack__elements)
