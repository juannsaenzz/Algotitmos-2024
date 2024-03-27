
#! EJERCICIO 6
#! Dada una secuencia de caracteres, obtener dicha secuencia invertida.

#! Hola → aloH

def invertirCadena(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return cadena[-1] + invertirCadena(cadena[:-1])
    #! cadena[-1] es el ultimo caracter de la cadena y cadena[:-1] (SLICING para recortar variables o listas) toma todos los caracteres de la cadena, menos el ultimo.
    
print(invertirCadena('hola mundo'))

#! EJERCICIO 7
#! Desarrollar un algoritmo que permita calcular la siguiente serie:
#! h(n) = 1+ 1/2 + 1/3 + ... + 1/n

#! 1/n + (1/n-1...1)

def sumatoriaSerie(n):
    if n == 1:
        return n
    else:
        return 1/n + sumatoriaSerie(n-1)
    
print(sumatoriaSerie(5))

#! EJERCICIO 8
#! Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.

def convertirBinario(numero):
    if numero <= 1:
        return str(numero)
    else:
        return convertirBinario(numero//2) + str(numero%2)

print(convertirBinario(3))

#! EJERCICIO 9
#! Implementar una función para calcular el logaritmo entero de número n en una base b. Recuerde que:
#! log en base b (n/b) = log en base b (n) + log en base b (b)

def logaritmo(n, b):
    if n < b:
        return 0
    else:
        return 1 + logaritmo(n//b, b)
    
print(logaritmo(64, 2))

#! EJERCICIO 10
#! Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

#! N // 10 hasta que N < 10

def contarDigitos(numero):
    if numero < 10:
        return numero
    else:
        return 1 + contarDigitos(numero//10)
    #! cada vez que se puede dividir por 10, se le suma un digito
    
print(contarDigitos(100))

#! EJERCICIO 11
#! Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.

#! 1234 → 4321
#! 1234
#!  4000
#!   300
#!    20
#!     1

def invertirNumero(numero):
    if numero < 10:
        return numero
    else:
        return (numero%10) * 10 ** len(str(numero//10))  + invertirNumero(numero//10)
    
print(invertirNumero(1234))

#! EJERCICIO 12
#! Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos números enteros.

#! 12 - 6  / 2
#!  6    3  / 3
#!  3    1
#! 2*3 = 6 (MCD)

def mcd(num1, num2):
    if num2 <= 1:
        return num1
    else:
        return mcd(num2, num1%num2)
    
print(mcd(12, 6))
    
#! EJERCICIO 14
#! Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no se puede convertir el número a cadena.

#! 123 = 6

def sumarDigitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero%10) + sumarDigitos(numero//10)

print(sumarDigitos(123))

#! EJERCICIO 17
#! Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.

nombres = ['juan', 'maria', 'nico', 'sol']

def barrido(lista):
    if len(lista) == 1:
        print(lista[0])
    else:
        barrido(lista[1:])
        print(lista[0])

barrido(nombres)