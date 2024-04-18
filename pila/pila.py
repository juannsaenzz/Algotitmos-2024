
class Stack:

    def __init__(self): #! inicia una pila
        self.__elements = []

    def push(self, element): #! agrega un elemento al final de la pila
        self.__elements.append(element)

    def pop(self): #! elimina el ultimo elemento de la pila
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self): #! muestra el ultimo elemento (cima) de la pila
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self): #! muestra la cantidad de elementos de la pila
        return len(self.__elements)