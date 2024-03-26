
#! EJERCICIO 6
#! Dada una secuencia de caracteres, obtener dicha secuencia invertida.

#! Hola → aloH
#! ola → H
#! la → oH
#! a → loH
#! _ → aloH

def invertir(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return cadena[-1] + invertir(cadena[:-1])
    #! cadena[-1] es el ultimo elemento de la cadena y cadena[:-1] toma todos los valores de la cadena, menos el ultimo
    
print (invertir('hola'))

#! EJERCICIO 7
#! Desarrollar un algoritmo que permita calcular la siguiente serie:
#! h(n) = 1+ 1/2 + 1/3 + ... + 1/n

def serie(n):
    if n == 1:
        return n
    else:
        return 1/n + serie(n-1)
    
print (serie(2))

#! EJERCICIO 10
#! Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

#! N // 10 hasta que N < 10

def contarDigitos(numero):
    if numero < 10:
        return numero
    else:
        return 1 + contarDigitos(numero//10)
    #! cada vez que se puede dividir por 10, se le suma un digito
    
print (contarDigitos(10))