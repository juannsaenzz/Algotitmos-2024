
#! EJERCICIO 7

#! Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.

from pila import Stack

def eliminar_i_esimo(stack, i):
    if stack.size() < i + 2:  # Verificar si hay al menos i + 2 elementos en la pila
        print("No hay suficientes elementos en la pila.")
        return None

    temp_stack = Stack()  # Pila auxiliar para almacenar elementos temporales

    # Desapilar elementos hasta llegar al i-ésimo elemento debajo de la cima
    for _ in range(i + 1):
        temp_stack.push(stack.pop())

    elemento_eliminado = temp_stack.pop()  # Elemento i-ésimo debajo de la cima

    # Colocar de nuevo los elementos en la pila original
    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())

    return elemento_eliminado

# Ejemplo de uso:
palabras = Stack()
palabras.push("manzana")
palabras.push("banana")
palabras.push("cereza")
palabras.push("dátiles")

i = 1  # Eliminar el segundo elemento debajo de la cima
elemento_eliminado = eliminar_i_esimo(palabras, i)
if elemento_eliminado is not None:
    print("Elemento eliminado:", elemento_eliminado)
    print("Pila actualizada:", [palabras.pop() for _ in range(palabras.size())])
