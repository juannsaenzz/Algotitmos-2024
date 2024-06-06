
#! EJERCICIO 28

#! Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita
#! calcular el valor de un determinado número en dicha sucesión.

#! f(n) = 3,          si n = 1
#! f(n) = f(n-1)+2n,   si n >= 2

def sucesion_recursiva(n):
    if n == 1:
        return 3
    else:
        return sucesion_recursiva(n-1) + 2*n

# Ejemplo de uso:
numero = 5
resultado = sucesion_recursiva(numero)
print("El valor de la sucesión en n =", numero, "es:", resultado)
