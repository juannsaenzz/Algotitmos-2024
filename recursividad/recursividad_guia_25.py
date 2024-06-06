
#! EJERCICO 25

#! Desarrollar una función recursiva que permita calcular y mostrar por pantalla el triángulo de
#! Pascal, para n filas utilizando una matriz auxiliar para guardar los resultados parciales.

def pascal(n, i, j, aux):
    # Caso base: los bordes del triángulo son 1
    if j == 0 or j == i:
        return 1
    # Si el valor ya fue calculado, retornarlo
    if aux[i][j] != -1:
        return aux[i][j]
    # Calcular el valor recursivamente
    aux[i][j] = pascal(n, i-1, j-1, aux) + pascal(n, i-1, j, aux)
    return aux[i][j]

def calcular_triangulo_de_pascal(n):
    # Crear una matriz auxiliar inicializada con -1
    aux = [[-1 for _ in range(i + 1)] for i in range(n)]
    # Calcular los valores del triángulo
    for i in range(n):
        for j in range(i + 1):
            pascal(n, i, j, aux)
    return aux

def imprimir_triangulo_de_pascal(triangulo):
    for fila in triangulo:
        print(' '.join(map(str, fila)))

# Ejemplo de uso:
n = 5  # Número de filas
triangulo = calcular_triangulo_de_pascal(n)
imprimir_triangulo_de_pascal(triangulo)
