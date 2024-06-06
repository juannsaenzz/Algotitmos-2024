
#! EJERCICIO 20

#! Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
#! cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
#! norte, sur, este, oeste, noreste, norodef registrar_movimientos():
#! partida, retornando por el mismo camino que fue.

class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def size(self):
        return len(self.__elements)


def registrar_movimientos():
    movimientos = Stack()
    while True:
        try:
            pasos = input("Ingrese la cantidad de pasos (o 'fin' para terminar): ")
            if pasos.lower() == 'fin':
                break
            direccion = input("Ingrese la dirección (norte, sur, este, oeste, noreste, noroeste, sureste, suroeste): ")
            movimientos.push((int(pasos), direccion))
        except ValueError:
            print("Error: La cantidad de pasos debe ser un número entero.")
    return movimientos


def generar_secuencia_regreso(movimientos):
    secuencia_regreso = Stack()
    while movimientos.size() > 0:
        pasos, direccion = movimientos.pop()
        # Invertir la dirección opuesta para regresar
        if direccion == 'norte':
            direccion_regreso = 'sur'
        elif direccion == 'sur':
            direccion_regreso = 'norte'
        elif direccion == 'este':
            direccion_regreso = 'oeste'
        elif direccion == 'oeste':
            direccion_regreso = 'este'
        elif direccion == 'noreste':
            direccion_regreso = 'suroeste'
        elif direccion == 'noroeste':
            direccion_regreso = 'sureste'
        elif direccion == 'sureste':
            direccion_regreso = 'noroeste'
        elif direccion == 'suroeste':
            direccion_regreso = 'noreste'
        # Agregar la dirección y pasos invertidos a la secuencia de regreso
        secuencia_regreso.push((pasos, direccion_regreso))
    return secuencia_regreso


# Ejemplo de uso:
print("Registrar movimientos del robot:")
movimientos_robot = registrar_movimientos()

print("\nGenerar secuencia de movimientos para regresar al punto de partida:")
secuencia_regreso = generar_secuencia_regreso(movimientos_robot)
while secuencia_regreso.size() > 0:
    pasos, direccion = secuencia_regreso.pop()
    print(f"Ir {pasos} pasos hacia {direccion}")
