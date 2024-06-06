
#! EJERCICIO 10

#! Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una
#! pila con nombres de dioses griegos.

from pila import Stack

def insertar_atenea(pila, i):
    temp_pila = Stack()  # Pila auxiliar para almacenar elementos temporales

    # Desapilar elementos hasta llegar a la i-ésima posición debajo de la cima
    count = 0
    while count < i:
        temp_pila.push(pila.pop())
        count += 1

    # Insertar Atenea en la pila original
    pila.push("Atenea")

    # Colocar los elementos desapilados de vuelta en la pila original
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

# Ejemplo de uso:
nombres_griegos = Stack()
nombres_griegos.push("Zeus")
nombres_griegos.push("Poseidón")
nombres_griegos.push("Hades")

i = 1  # Insertar Atenea en la segunda posición debajo de la cima
insertar_atenea(nombres_griegos, i)

# Imprimir los nombres de los dioses griegos después de insertar Atenea
temp_pila = Stack()
while nombres_griegos.size() > 0:
    temp_pila.push(nombres_griegos.pop())
while temp_pila.size() > 0:
    nombre = temp_pila.pop()
    print(nombre)
    nombres_griegos.push(nombre)

