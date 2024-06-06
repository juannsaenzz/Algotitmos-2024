
#! EJERCICO 23

#! Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
# !matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
#! y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
#! y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
#! avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.

def es_valido(laberinto, x, y, visitado):
    # Comprobar si (x, y) está dentro de los límites del laberinto y no es una pared ni una casilla visitada
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto) and laberinto[x][y] == 1 and not visitado[x][y]

def resolver_laberinto(laberinto):
    n = len(laberinto)
    visitado = [[False for _ in range(n)] for _ in range(n)]
    camino = []

    def resolver(x, y):
        # Si se llega a la casilla de salida, retornar True
        if x == n-1 and y == n-1:
            camino.append((x, y))
            return True

        if es_valido(laberinto, x, y, visitado):
            visitado[x][y] = True
            camino.append((x, y))

            # Moverse a la derecha
            if resolver(x, y + 1):
                return True

            # Moverse hacia abajo
            if resolver(x + 1, y):
                return True

            # Moverse a la izquierda
            if resolver(x, y - 1):
                return True

            # Moverse hacia arriba
            if resolver(x - 1, y):
                return True

            # Si ninguna dirección es válida, retroceder
            camino.pop()
            visitado[x][y] = False
        
        return False

    if resolver(0, 0):
        return camino
    else:
        return "No hay camino disponible"

# Ejemplo de uso:
laberinto = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

camino = resolver_laberinto(laberinto)
print("Camino encontrado:", camino)
