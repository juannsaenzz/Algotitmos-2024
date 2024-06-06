
#! EJERCICIO 18

#! Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejem-
#! plo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso –del
#! objeto más liviano al más pesado–. Solo pueden utilizar pilas auxiliares como estructuras ex-
#! tras, no se pueden utilizar métodos de ordenamiento.

from pila import Stack

def ordenar_por_peso(pila):
    pila_aux = Stack()  # Pila auxiliar para almacenar temporalmente los objetos

    while pila.size() > 0:
        # Tomar un objeto de la pila original
        objeto_actual = pila.pop()

        # Mover objetos más pesados a la pila auxiliar
        while pila_aux.size() > 0 and pila_aux.on_top()[1] < objeto_actual[1]:
            pila.push(pila_aux.pop())

        # Insertar el objeto actual en la posición correcta en la pila auxiliar
        pila_aux.push(objeto_actual)

    # Transferir objetos de la pila auxiliar a la pila original (en orden de peso ascendente)
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

# Ejemplo de uso:
pila_objetos = Stack()
pila_objetos.push(("Monitor", 1))
pila_objetos.push(("Teclado", 0.25))
pila_objetos.push(("Silla", 7))
pila_objetos.push(("Escritorio", 15))
pila_objetos.push(("Ratón", 0.1))

# Ordenar la pila por peso
ordenar_por_peso(pila_objetos)

# Imprimir la pila ordenada
print("Pila ordenada por peso (del objeto más liviano al más pesado):")
while pila_objetos.size() > 0:
    objeto = pila_objetos.pop()
    print(objeto[0], "-", objeto[1], "kg")
