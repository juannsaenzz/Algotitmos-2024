
#! EJERCICIO 19

#! Modificar las funciones de arribo y atención del TDA cola para adaptarlo a una cola circular,
#! que no necesite la función mover al final; y desarrollar un función que permita realizar un ba-
#! rrido de dicha estructura respetando el principio de funcionamiento de la cola.

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__elements = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, element):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.__elements[self.rear] = element
            self.size += 1

    def dequeue(self):
        if not self.is_empty():
            element = self.__elements[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return element
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.__elements[self.front]
        else:
            return None

    def scan(self):
        if not self.is_empty():
            current = self.front
            while current != self.rear:
                print(self.__elements[current], end=" ")
                current = (current + 1) % self.capacity
            print(self.__elements[self.rear])
        else:
            print("La cola está vacía.")


# Ejemplo de uso:
cola_circular = CircularQueue(5)
cola_circular.enqueue(1)
cola_circular.enqueue(2)
cola_circular.enqueue(3)
cola_circular.enqueue(4)
cola_circular.enqueue(5)

# Realizar un barrido de la cola circular
print("Contenido de la cola circular:")
cola_circular.scan()

# Atender un elemento de la cola circular
print("Elemento atendido:", cola_circular.dequeue())

# Realizar un barrido de la cola circular después de la atención
print("Contenido de la cola circular después de la atención:")
cola_circular.scan()
