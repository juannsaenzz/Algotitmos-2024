
#! EJERCICIO 5
#! Determinar si una cadena de caracteres es un palíndromo.

from pila import Stack

pila = Stack()

def es_palindromo(cadena):
    #! Agrega cada caracter de la cadena a la pila
    for char in cadena:
        print(char)
        pila.push(char)

    #! Compara cada caracter de la cadena con el elemento de la cima de la pila
    for char in cadena:
        data = pila.pop()
        if char != data:
            #! Si en alguna comparacion no coincide, no es un palindromo y devuelve false
            return False
    
    return True
        
cadena = input('Ingrese una cadena para determinar si es un palindromo: ')
if es_palindromo(cadena):
    print(f'{cadena} si es un palindromo')
else:
    print(f'{cadena} no es un palindromo')