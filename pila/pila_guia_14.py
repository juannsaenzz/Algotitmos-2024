
#! EJERCICIO 14

#! Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden orde-
#! nados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se
#! pueden utilizar métodos de ordenamiento–.

from pila import Stack

def ordenar_pila(pila):
    pila_aux = Stack()  # Pila auxiliar para almacenar temporalmente los elementos

    while pila.size() > 0:
        # Tomar un elemento de la pila original
        temp = pila.pop()

        # Mover elementos mayores que el elemento temporal a la pila auxiliar
        while pila_aux.size() > 0 and pila_aux.on_top() > temp:
            pila.push(pila_aux.pop())

        # Insertar el elemento temporal en la pila auxiliar
        pila_aux.push(temp)

    # Transferir elementos de la pila auxiliar a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

# Ejemplo de uso:
mi_pila = Stack()
elementos = [4, 2, 7, 1, 5]

# Insertar elementos en la pila
for elemento in elementos:
    mi_pila.push(elemento)

# Ordenar la pila
ordenar_pila(mi_pila)

# Imprimir la pila ordenada
print("Pila ordenada:")
while mi_pila.size() > 0:
    print(mi_pila.pop())
