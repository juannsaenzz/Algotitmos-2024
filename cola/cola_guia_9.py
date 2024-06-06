
#! EJERCICIO 9

#! Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.

from cola import Queue

def calcular_rango_y_contar_negativos(cola):
    if cola.size() == 0:
        return None, 0

    minimo = maximo = cola.attention()
    negativos = 1 if minimo < 0 else 0

    while cola.size() > 0:
        elemento = cola.attention()
        if elemento < minimo:
            minimo = elemento
        elif elemento > maximo:
            maximo = elemento
        if elemento < 0:
            negativos += 1

    rango = maximo - minimo
    return rango, negativos


# Ejemplo de uso
cola = Queue()
cola.arrive(3)
cola.arrive(-1)
cola.arrive(7)
cola.arrive(-5)
cola.arrive(10)

rango, negativos = calcular_rango_y_contar_negativos(cola)
print("Rango de la cola:", rango)
print("Cantidad de elementos negativos:", negativos)
