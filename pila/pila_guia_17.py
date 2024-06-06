
#! EJERCICIO 17

#! Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales, consonan-
#! tes y otros caracteres que no sean letras (signos de puntuación números, espacios, etc.). Luego
#! utilizando las operaciones de pila resolver las siguientes consignas:

#! a. cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);
#! b. cantidad de espacios en blanco;
#! c. porcentaje que representan las vocales respecto de las consonantes sobre el total de carac-
#! teres del párrafo;
#! d. cantidad de números;
#! e. determinar si la cantidad de vocales y otros caracteres son iguales;
#! f. determinar si existe al menos una z en la pila de consonantes.

from pila import Stack

def separar_caracteres(parrafo):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    pila_vocales = Stack()
    pila_consonantes = Stack()
    pila_otros = Stack()

    for caracter in parrafo:
        if caracter.isalpha():
            if caracter in vocales:
                pila_vocales.push(caracter)
            elif caracter in consonantes:
                pila_consonantes.push(caracter)
        else:
            pila_otros.push(caracter)

    return pila_vocales, pila_consonantes, pila_otros

def cantidad_caracteres(pila):
    return pila.size()

def cantidad_espacios(parrafo):
    return parrafo.count(' ')

def porcentaje_vocales_consonantes(pila_vocales, pila_consonantes, pila_otros):
    total_caracteres = pila_vocales.size() + pila_consonantes.size() + pila_otros.size()
    if pila_consonantes.size() == 0:
        return "No se pueden calcular los porcentajes porque no hay consonantes en el párrafo."
    porcentaje_vocales = (pila_vocales.size() / pila_consonantes.size()) * 100
    return porcentaje_vocales

def cantidad_numeros(pila_otros):
    numeros = "0123456789"
    contador = 0
    temp_pila = Stack()

    while pila_otros.size() > 0:
        caracter = pila_otros.pop()
        temp_pila.push(caracter)
        if caracter in numeros:
            contador += 1

    while temp_pila.size() > 0:
        pila_otros.push(temp_pila.pop())

    return contador

def vocales_otros_iguales(pila_vocales, pila_otros):
    return pila_vocales.size() == pila_otros.size()

def existe_z(pila_consonantes):
    while pila_consonantes.size() > 0:
        if pila_consonantes.pop() == 'z':
            return True
    return False

# Ejemplo de uso:
parrafo = "Este es un párrafo de ejemplo con 123 números y algunas vocales."
pila_vocales, pila_consonantes, pila_otros = separar_caracteres(parrafo)

print("Cantidad de caracteres:")
print("Vocales:", cantidad_caracteres(pila_vocales))
print("Consonantes:", cantidad_caracteres(pila_consonantes))
print("Otros:", cantidad_caracteres(pila_otros))

print("\nCantidad de espacios en blanco:", cantidad_espacios(parrafo))

print("\nPorcentaje que representan las vocales respecto de las consonantes:")
print(porcentaje_vocales_consonantes(pila_vocales, pila_consonantes, pila_otros))

print("\nCantidad de números:", cantidad_numeros(pila_otros))

print("\n¿La cantidad de vocales y otros caracteres son iguales?:", vocales_otros_iguales(pila_vocales, pila_otros))

print("\n¿Existe al menos una z en la pila de consonantes?:", existe_z(pila_consonantes))
