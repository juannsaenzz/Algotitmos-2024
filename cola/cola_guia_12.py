
#! EJERCICIO 12

#! Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
#! nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
#! ni métodos de ordenamiento.

from cola import Queue

def combinar_colas_ordenadas(cola1, cola2):
    nueva_cola = Queue()

    while cola1.size() > 0 and cola2.size() > 0:
        elemento_cola1 = cola1.attention()
        elemento_cola2 = cola2.attention()

        if elemento_cola1 <= elemento_cola2:
            nueva_cola.arrive(elemento_cola1)
            cola2.arrive(elemento_cola2)  # Devolver el elemento a la cola2
        else:
            nueva_cola.arrive(elemento_cola2)

    # Agregar los elementos restantes de la cola1, si los hay
    while cola1.size() > 0:
        nueva_cola.arrive(cola1.attention())

    # Agregar los elementos restantes de la cola2, si los hay
    while cola2.size() > 0:
        nueva_cola.arrive(cola2.attention())

    return nueva_cola



# Ejemplo de uso
cola1 = Queue()
cola1.arrive(1)
cola1.arrive(3)
cola1.arrive(5)

cola2 = Queue()
cola2.arrive(2)
cola2.arrive(4)
cola2.arrive(6)

nueva_cola = combinar_colas_ordenadas(cola1, cola2)

# Imprimir la nueva cola combinada
print("Nueva cola combinada:")
while nueva_cola.size() > 0:
    print(nueva_cola.attention())
