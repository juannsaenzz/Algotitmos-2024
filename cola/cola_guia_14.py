
#! EJERCICIO 14

#! Realizar un algoritmo que permita realizar las siguientes funciones:

#! a. cargar semáforos de una rotonda y sus respectivos tiempos de encendido en verde –cargue
#! al menos tres semáforos–.
#! b. simular el funcionamiento de los semáforos cargados (cola circular).
#! c. debe mostrar por pantalla el cambio de colores y el número del semáforo.

class Queue:
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

    def arrive(self, element):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.__elements[self.rear] = element
            self.size += 1

    def attention(self):
        if not self.is_empty():
            element = self.__elements[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return element
        else:
            return None

def cargar_semaforos(rotonda, tiempos_verde):
    for tiempo in tiempos_verde:
        rotonda.arrive(tiempo)

def simular_semaforos(rotonda, ciclos):
    contador_ciclos = 0
    contador_semaforo = 1
    while contador_ciclos < ciclos:
        tiempo_verde = rotonda.attention()
        print(f"Semáforo {contador_semaforo}: Verde ({tiempo_verde} segundos)")
        contador_semaforo += 1
        contador_ciclos += 1
        # Volver a colocar el tiempo de verde en la cola
        rotonda.arrive(tiempo_verde)

# Ejemplo de uso
rotonda = Queue(3)  # Capacidad para tres semáforos
cargar_semaforos(rotonda, [20, 30, 25])  # Cargar tiempos de verde para los semáforos
simular_semaforos(rotonda, 10)  # Simular el funcionamiento de los semáforos durante 10 ciclos de tiempo

