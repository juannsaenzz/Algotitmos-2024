
#! EJERCICIO 21

#! Realizar un algoritmo que ingrese en una pila los dos valores iniciales de la sucesión de Fi-
#! bonacci –o condiciones de fin de forma recursiva– y a partir de estos calcular los siguientes
#! valores de dicha sucesión, hasta obtener el valor correspondiente a un número n ingresado por
#! el usuario.

from pila import Stack

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def calcular_fibonacci(n):
    pila_fibonacci = Stack()
    if n <= 0:
        return pila_fibonacci
    
    # Inicializar la pila con los dos primeros valores de Fibonacci
    pila_fibonacci.push(0)
    if n >= 2:
        pila_fibonacci.push(1)
    
    # Calcular y agregar los siguientes valores de Fibonacci a la pila
    for i in range(2, n):
        fib_n = pila_fibonacci.pop() + pila_fibonacci.on_top()
        pila_fibonacci.push(fib_n)
        # Necesitamos retroceder un paso en la pila para obtener el último valor correcto
        pila_fibonacci.push(pila_fibonacci.pop())
    return pila_fibonacci

# Ejemplo de uso:
numero = int(input("Ingrese el número n para calcular la sucesión de Fibonacci: "))
pila_fibonacci = calcular_fibonacci(numero)
print("Sucesión de Fibonacci hasta el número", numero, ":")
while pila_fibonacci.size() > 0:
    print(pila_fibonacci.pop(), end=" ")
print()
