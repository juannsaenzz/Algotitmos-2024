
#! EJERCICIO 26

#! Resuelva el problema de colocar las 8 reinas sobre un tablero de ajedrez sin que las mismas
#! se amenacen.

def es_seguro(tablero, fila, col):
    # Verificar la columna
    for i in range(fila):
        if tablero[i][col] == 1:
            return False

    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificar la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(col, len(tablero))):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_8_reinas(tablero, fila):
    # Si hemos colocado 8 reinas, hemos encontrado una solución
    if fila >= len(tablero):
        return True

    # Intentar colocar una reina en cada columna de la fila actual
    for col in range(len(tablero)):
        if es_seguro(tablero, fila, col):
            # Colocar la reina en la casilla (fila, col)
            tablero[fila][col] = 1

            # Recursivamente intentar colocar el resto de las reinas
            if resolver_8_reinas(tablero, fila + 1):
                return True

            # Si no es posible colocar la reina, retroceder (backtracking)
            tablero[fila][col] = 0

    return False

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join('Q' if col == 1 else '.' for col in fila))

# Ejemplo de uso:
n = 8  # Tamaño del tablero (8x8)
tablero = [[0 for _ in range(n)] for _ in range(n)]

if resolver_8_reinas(tablero, 0):
    imprimir_tablero(tablero)
else:
    print("No se encontró una solución")
