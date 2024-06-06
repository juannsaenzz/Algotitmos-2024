
#! EJERCICIO 11

#! Dada una pila de letras determinar cuántas vocales contiene.

from pila import Stack

def contar_vocales(pila):
    vocales = "aeiouAEIOU"
    contador = 0
    
    # Iterar sobre la pila y contar las vocales
    while pila.size() > 0:
        letra = pila.pop()
        if letra in vocales:
            contador += 1
    
    return contador

# Ejemplo de uso:
letras = Stack()
letras.push("a")
letras.push("b")
letras.push("c")
letras.push("e")
letras.push("f")
letras.push("i")

num_vocales = contar_vocales(letras)
print("La pila contiene", num_vocales, "vocales.")
