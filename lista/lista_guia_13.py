
#! EJERCICIO 13

#! Desarrollar un algoritmo que permita visualizar el contenido de una lista de manera ascenden-
#! te y descendente de sus elementos, debe modificar el TDA para implementar lista doblemen-
#! te enlazada.

def mostrar_ascendente(lista):
    print("Contenido de la lista en orden ascendente:")
    for elemento in lista:
        print(elemento)

def mostrar_descendente(lista):
    print("Contenido de la lista en orden descendente:")
    for elemento in reversed(lista):
        print(elemento)

# Ejemplo de uso
mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
mostrar_ascendente(mi_lista)
mostrar_descendente(mi_lista)
