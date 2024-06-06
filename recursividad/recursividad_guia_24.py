
#! EJERCICIO 24

#! En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una
#! plataforma de bronce sobre la cual había tres agujas de diamante. En la primera aguja estaban
#! apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que estaba debajo.
#! A los sacerdotes se les encomendó la tarea de pasarlos todos desde la primera aguja a la tercera,
#! con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá ponerse en-
#! cima de otro más pequeño. Se dijo a los sacerdotes que, cuando hubieran terminado de mover
#! los discos, llegaría el fin del mundo. Resolver este problema de la Torre de Hanói.

def hanoi(n, origen, destino, auxiliar, movimientos):
    if n == 1:
        movimientos.append((origen, destino))
        return
    hanoi(n - 1, origen, auxiliar, destino, movimientos)
    movimientos.append((origen, destino))
    hanoi(n - 1, auxiliar, destino, origen, movimientos)

def resolver_hanoi(n):
    movimientos = []
    hanoi(n, 'A', 'C', 'B', movimientos)
    return movimientos

# Ejemplo de uso:
n = 74  # Número de discos
movimientos = resolver_hanoi(n)
print(f"Cantidad total de movimientos: {len(movimientos)}")
# Descomentar la siguiente línea para ver todos los movimientos:
# for i, (origen, destino) in enumerate(movimientos):
#     print(f"Movimiento {i+1}: Mover disco de {origen} a {destino}")

