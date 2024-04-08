
#! EJERCICIO 1
#! Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 3
print(fibonacci(n))

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

#! EJERCICIO 15
#! Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero.
#! Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro el número a calcular su raíz.

#!  Utilizando el método de aproximación de Newton para calcular la raíz cuadrada
def raizCuadradaRecursiva(n, aprox = None):
    if aprox is None:
        aprox = n // 2
    sigAprox = (aprox + n // aprox) // 2 #! metodo de Newton
    if sigAprox >= aprox:
        return aprox
    return raizCuadradaRecursiva(n, sigAprox)

def raizCuadrada(numero):
    if numero < 0:
        print("No se puede calcular la raíz cuadrada de un número negativo")
    elif numero == 0:
        return 0
    else:
        return raizCuadradaRecursiva(numero)
    
numero = 16
print(raizCuadrada(numero))

#! EJERCICIO 16
#!Implementar un función recursiva que permita obtener el valor de an en una sucesión geométrica (o progresión geométrica) con un valor a1= 2 y una razón r = -3.
#! Además desarrollar un algoritmo que permita visualizar todos los valores de dicha sucesión desde a1 hasta an.

#! forma general de sucesion geometrica: an = a . r**(n-1)
#! 2 . (-3)**(n-1) 

def sucesionGeometrica(a1, r, n):
    if n == 1:
        return a1
    else:
        return r * (sucesionGeometrica(a1, r, n-1))

a1 = 2
r = -3
n = 10

for i in range(1, n + 1):
    print(f'a{i}: {sucesionGeometrica(a1, r, i)}')

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

#! EJERCICIO 18
#! Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.

def matrizRec(matriz, fila = 0, columna = 0):
    if fila == len(matriz): #! Verificar si se termino de recorrer la matriz
        return
    print(matriz[fila][columna]) #! Mostrar el valor actual de la matriz
    if columna + 1 < len(matriz[0]): #! Avanzar a la siguiente columna
        matrizRec(matriz, fila, columna + 1)
    else: #! Si se termino de recorrer la columna acutual, avanzar a la siguiente fila
        matrizRec(matriz, fila + 1, 0)
        
matriz = [[1,2,3], [4,5,6], [7,8,9]]
matrizRec(matriz)

#! EJERCICIO 19
#! Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita
#! calcular el valor de un determinado número en dicha sucesión.

#! f(n) = 2 -> n = 1
#!      =  n + (1 / f(n-1)) -> n >= 2

def sucesion(n):
    if n == 1:
        return 2
    else:
        return n + (1 / sucesion(n-1))
    
n = 2
print(sucesion(n))

#! EJERCICIO 20
#! Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de manera recursiva,
#! y permita determinar si un valor dado está o no en dicha lista.

def busquedaSecuencial(lista, valor, indice = 0):
    if indice == len(lista): #! Verificar si se termino de recorrer la lista
        return False
    if lista[indice] == valor: #! Verificar si se encuentra el valor
        return True
    return busquedaSecuencial(lista, valor, indice + 1) #! Incrementar el indice en 1 para cada recorrido

lista = [1,2,3,4,5,6,7]
valor = 4

if busquedaSecuencial(lista, valor):
    print(f'{valor} si esta en la lista')
else:
    print(f'{valor} no esta en la lista')