
#! EJERCICIO 11

#! Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
#! de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:

#! a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
#! b. indicar el plantea natal de Luke Skywalker y Han Solo
#! c. insertar un nuevo personaje antes del maestro Yoda
#! d. eliminar el personaje ubicado después de Jar Jar Binks

from pila import Stack
from cola import Queue

def mostrar_personajes_por_planeta(cola, planeta):
    pila_aux = Stack()
    encontrados = []
    
    # Buscar y mostrar los personajes del planeta dado
    while cola.size() > 0:
        personaje = cola.attention()
        if personaje["planeta"] == planeta:
            encontrados.append(personaje["nombre"])
        pila_aux.push(personaje)
    
    # Devolver los personajes a la cola original
    while pila_aux.size() > 0:
        cola.arrive(pila_aux.pop())
    
    if encontrados:
        print(f"Personajes encontrados en el planeta {planeta}:")
        for personaje in encontrados:
            print(personaje)
    else:
        print(f"No se encontraron personajes en el planeta {planeta}")


def encontrar_planeta_natal(cola, personaje):
    pila_aux = Stack()
    encontrado = False
    
    # Buscar el planeta natal del personaje
    while cola.size() > 0:
        p = cola.attention()
        if p["nombre"] == personaje:
            print(f"El planeta natal de {personaje} es {p['planeta']}")
            encontrado = True
        pila_aux.push(p)
    
    # Devolver los personajes a la cola original
    while pila_aux.size() > 0:
        cola.arrive(pila_aux.pop())
    
    if not encontrado:
        print(f"No se encontró el personaje {personaje}")

def insertar_antes_de_maestro_yoda(cola, nuevo_personaje):
    pila_aux = Stack()
    
    # Buscar la posición del maestro Yoda
    while cola.size() > 0:
        personaje = cola.attention()
        if personaje["nombre"] == "Yoda":
            break
        pila_aux.push(personaje)
    
    # Insertar el nuevo personaje antes de Yoda
    cola.arrive(nuevo_personaje)
    
    # Restaurar la cola original
    while pila_aux.size() > 0:
        cola.arrive(pila_aux.pop())

def eliminar_despues_de_jar_jar(cola):
    pila_aux = Stack()
    encontrado = False
    
    # Buscar y eliminar el personaje después de Jar Jar Binks
    while cola.size() > 0:
        personaje = cola.attention()
        if personaje["nombre"] == "Jar Jar Binks":
            encontrado = True
            cola.attention()  # Descartar el siguiente personaje
        else:
            pila_aux.push(personaje)
    
    # Devolver los personajes a la cola original
    while pila_aux.size() > 0:
        cola.arrive(pila_aux.pop())
    
    if not encontrado:
        print("Jar Jar Binks no encontrado en la cola")

cola_star_wars = Queue()

# Agregar personajes a la cola_star_wars
cola_star_wars.arrive({"nombre": "Luke Skywalker", "planeta": "Tatooine"})
cola_star_wars.arrive({"nombre": "Han Solo", "planeta": "Corellia"})
cola_star_wars.arrive({"nombre": "Leia Organa", "planeta": "Alderaan"})
cola_star_wars.arrive({"nombre": "Yoda", "planeta": "Dagobah"})
cola_star_wars.arrive({"nombre": "Jar Jar Binks", "planeta": "Naboo"})

# Luego, llamar a las funciones
mostrar_personajes_por_planeta(cola_star_wars, "Alderaan")
mostrar_personajes_por_planeta(cola_star_wars, "Endor")
mostrar_personajes_por_planeta(cola_star_wars, "Tatooine")

encontrar_planeta_natal(cola_star_wars, "Luke Skywalker")
encontrar_planeta_natal(cola_star_wars, "Han Solo")

insertar_antes_de_maestro_yoda(cola_star_wars, {"nombre": "Nuevo Personaje", "planeta": "Planeta Nuevo"})

eliminar_despues_de_jar_jar(cola_star_wars)
