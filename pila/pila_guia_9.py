
#! EJERCICIO 9

#! Resolver el problema del factorial de un número utilizando una pila.

from pila import Stack

def factorial(num):
    if num == 0 or num == 1:
        return 1

    resultado = 1
    pila = Stack()
    
    # Empujar números a la pila
    for i in range(2, num + 1):
        pila.push(i)

    # Calcular factorial multiplicando los elementos de la pila
    while pila.size() > 0:
        resultado *= pila.pop()

    return resultado

# Ejemplo de uso
numero = 5
print("El factorial de", numero, "es:", factorial(numero))
