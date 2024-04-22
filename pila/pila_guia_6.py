
#! EJERCICIO 6
#! Leer una palabra y visualizarla en forma inversa.

from pila import Stack
from random import randint

pila = Stack()
pilaAux = Stack()

def invertir(cadena):
    #! Agrega cada caracter de la cadena a la pila
    for char in cadena:
        print(char)
        pila.push(char)
    
    cadena_inversa = ''
    
    while pila.size() > 0:
        cadena_inversa += pila.pop()
    
    return cadena_inversa

cadena = input('Ingrese una cadena para invertirla: ')
print(f'Cadena de forma inversa: {invertir(cadena)}')