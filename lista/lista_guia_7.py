
#! EJERCICIO 7

#! Implementar los algoritmos necesarios para resolver las siguientes tareas:

#! a. concatenar dos listas, una atrás de la otra;
#! b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
#! c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
#! d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

from lista import show_list

# Función para concatenar dos listas una detrás de la otra
def concatenar_listas(lista1, lista2):
    """Concatena dos listas una detrás de la otra."""
    return lista1 + lista2

# Función para concatenar dos listas omitiendo datos repetidos y manteniendo el orden
def concatenar_sin_repetidos(lista1, lista2):
    """Concatena dos listas omitiendo datos repetidos y manteniendo el orden."""
    resultado = []
    seen = set()
    for item in lista1 + lista2:
        if item not in seen:
            seen.add(item)
            resultado.append(item)
    return resultado

# Función para contar cuántos elementos repetidos hay entre dos listas (intersección)
def contar_elementos_repetidos(lista1, lista2):
    """Cuenta cuántos elementos repetidos hay entre dos listas (intersección)."""
    set1 = set(lista1)
    set2 = set(lista2)
    interseccion = set1.intersection(set2)
    return len(interseccion)

# Función para eliminar todos los nodos de una lista de a uno a la vez, mostrando su contenido
def eliminar_nodos(lista):
    """Elimina todos los nodos de una lista de a uno a la vez, mostrando su contenido."""
    while lista:
        elemento = lista.pop(0)
        print(f'Eliminado: {elemento}')

# Ejemplos de uso con integración de funciones
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

# a. concatenar listas
lista_concatenada = concatenar_listas(lista1, lista2)
show_list("Concatenada", lista_concatenada)

# b. concatenar listas sin repetidos
lista_sin_repetidos = concatenar_sin_repetidos(lista1, lista2)
show_list("Sin repetidos", lista_sin_repetidos)

# c. contar elementos repetidos
cantidad_repetidos = contar_elementos_repetidos(lista1, lista2)
print("Cantidad de repetidos:", cantidad_repetidos)

# d. eliminar nodos
lista = [1, 2, 3, 4, 5]
eliminar_nodos(lista)
