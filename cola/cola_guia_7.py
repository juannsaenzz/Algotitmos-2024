
#! EJERCICIO 7

#! Eliminar el i-ésimo elemento después del frente de la cola.

from cola import Queue

def eliminar_iesimo_despues_del_frente(cola, i):
    # Extraer los primeros i+1 elementos y guardarlos
    elementos_principio = []
    for _ in range(i + 1):
        elemento = cola.attention()
        if elemento is not None:
            elementos_principio.append(elemento)

    # Descartar el siguiente elemento después de los primeros i elementos
    cola.attention()

    # Extraer el resto de los elementos y guardarlos
    elementos_restantes = []
    while cola.size() > 0:
        elemento = cola.attention()
        if elemento is not None:
            elementos_restantes.append(elemento)

    # Reconstruir la cola original
    for elemento in elementos_principio:
        cola.arrive(elemento)
    for elemento in elementos_restantes:
        cola.arrive(elemento)


# Ejemplo de uso
cola = Queue()
cola.arrive(1)
cola.arrive(2)
cola.arrive(3)
cola.arrive(4)
cola.arrive(5)

i = 2
eliminar_iesimo_despues_del_frente(cola, i)

print("Cola después de eliminar el", i+1, "-ésimo elemento después del frente:", cola._Queue__elements)
