
#! EJERCICIO 15

#! Realizar el algoritmo de ordenamiento quicksort de manera que funcione iterativamente.

from pila import Stack

def particion(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_iterativo(arr):
    n = len(arr)
    pila = Stack()
    pila.push(0)
    pila.push(n - 1)

    while pila.size() > 0:
        high = pila.pop()
        low = pila.pop()

        pivot_index = particion(arr, low, high)

        if pivot_index - 1 > low:
            pila.push(low)
            pila.push(pivot_index - 1)

        if pivot_index + 1 < high:
            pila.push(pivot_index + 1)
            pila.push(high)

# Ejemplo de uso:
arr = [8, 3, 1, 5, 4, 7, 6, 2]
print("Arreglo antes de ordenar:", arr)
quicksort_iterativo(arr)
print("Arreglo después de ordenar:", arr)
