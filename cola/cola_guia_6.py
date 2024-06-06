
#! EJERCICIO 6

#! Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ningu-
#! na estructura auxiliar.

from cola import Queue

def contar_ocurrencias(cola, elemento):
    contador = 0
    while cola.size() > 0:
        elemento_actual = cola.attention()
        if elemento_actual == elemento:
            contador += 1
    return contador


# Ejemplo de uso
cola = Queue()
cola.arrive(1)
cola.arrive(2)
cola.arrive(3)
cola.arrive(2)
cola.arrive(4)

elemento_buscado = 2
ocurrencias = contar_ocurrencias(cola, elemento_buscado)
print("Cantidad de ocurrencias de", elemento_buscado, "en la cola:", ocurrencias)
