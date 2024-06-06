
#! EJERCICIO 8

#! Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando
#! solo una cola como estructura auxiliar.

from cola import Queue

def mantener_ordenado(cola):
    cola_auxiliar = Queue()

    while cola.size() > 0:
        elemento_temporal = cola.attention()

        # Mover elementos de la cola auxiliar a la cola original
        while cola_auxiliar.size() > 0 and cola_auxiliar.on_front() is not None and cola_auxiliar.on_front() < elemento_temporal:
            cola.arrive(cola_auxiliar.attention())

        # Insertar el elemento temporal en la posición correcta en la cola auxiliar
        cola_auxiliar.arrive(elemento_temporal)

    # Mover elementos de la cola auxiliar a la cola original
    while cola_auxiliar.size() > 0:
        cola.arrive(cola_auxiliar.attention())



# Ejemplo de uso
cola = Queue()
cola.arrive(3)
cola.arrive(1)
cola.arrive(4)
cola.arrive(2)
cola.arrive(5)

mantener_ordenado(cola)

print("Cola ordenada:", cola._Queue__elements)
