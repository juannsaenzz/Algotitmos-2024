
class Queue:

    def __init__(self): #! Inicia una cola
        self.__elements = []

    def arrive(self, element): #! Agrega un elemento al final de la cola
        self.__elements.append(element)

    def attention(self): #! Elimina y devuelve el elemento del frente de la cola
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self): #! Muestra la cantidad de elementos de la cola
        return len(self.__elements)

    def on_front(self): #! Devuelve el valor del frente de la cola, sin eliminarlo
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self): #! Elimina el elemento del frente y lo inserta en el final de la cola
        element = self.attention()
        if element is not None:
            self.arrive(element)

# cola_1 = Queue()

# cola_1.arrive(1)
# cola_1.arrive(2)
# cola_1.arrive(3)
# cola_1.arrive(4)
# cola_1.arrive(5)
# cola_1.attention()
# cola_1.attention()
# print(cola_1.size())
# print(cola_1.on_front())
# cola_1.move_to_end()
# cola_1.move_to_end()
# print()
# for i in range(cola_1.size()):
#     print(cola_1.on_front())
#     cola_1.move_to_end()
# print()
# print(cola_1.size())