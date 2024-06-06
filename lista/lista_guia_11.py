
#! EJERCICIO 11

#! Dada una lista que contiene información de los personajes de la saga de Star Wars con la si-
#! guiente información nombre, altura, edad, género, especie, planeta natal y episodios en los que
#! apareció, desarrollar los algoritmos que permitan realizar las siguientes actividades:

#! a. listar todos los personajes de género femenino;
#! b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episo-
#! dios de la saga;
#! c. mostrar toda la información de Darth Vader y Han Solo;
#! d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
#! e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
#! f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
#! g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
#! h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
#! i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información.

from lista import *

def listar_personajes_genero(personajes, genero):
    """Lista todos los personajes de un género específico."""
    return [personaje for personaje in personajes if personaje['genero'] == genero]

def listar_personajes_especie_episodios(personajes, especie, episodios):
    """Lista todos los personajes de una especie que aparecieron en ciertos episodios."""
    return [personaje for personaje in personajes if personaje['especie'] == especie and set(episodios).issubset(personaje['episodios'])]

def mostrar_info_personajes(personajes, nombres):
    """Muestra toda la información de los personajes con nombres específicos."""
    return [personaje for personaje in personajes if personaje['nombre'] in nombres]

def listar_personajes_episodios(personajes, episodios):
    """Lista todos los personajes que aparecen en ciertos episodios."""
    return [personaje for personaje in personajes if set(episodios).issubset(personaje['episodios'])]

def personajes_edad_mayor(personajes, edad_limite):
    """Lista los personajes con edad mayor a un límite y de ellos el mayor."""
    mayores = [personaje for personaje in personajes if personaje['edad'] > edad_limite]
    return max(mayores, key=lambda x: x['edad']) if mayores else None

def eliminar_personajes_episodios(personajes, episodios):
    """Elimina todos los personajes que aparecieron en ciertos episodios."""
    return [personaje for personaje in personajes if not set(episodios).issubset(personaje['episodios'])]

def listar_personajes_especie_planeta(personajes, especie, planeta):
    """Lista los personajes de una especie cuyo planeta de origen es específico."""
    return [personaje for personaje in personajes if personaje['especie'] == especie and personaje['planeta_natal'] == planeta]

def mostrar_info_personajes_altura(personajes, altura_limite):
    """Muestra toda la información de los personajes cuya altura es menor a un límite."""
    return [personaje for personaje in personajes if personaje['altura'] < altura_limite]

def determinar_episodios_personaje(personajes, nombre):
    """Determina en qué episodios aparece un personaje y muestra su información."""
    for personaje in personajes:
        if personaje['nombre'] == nombre:
            return personaje['episodios'], personaje
    return None, None

# Suponiendo que 'personajes' es una lista de diccionarios con la información de los personajes de Star Wars
# Ejemplo de uso:

personajes_star_wars = [
    {'nombre': 'Luke Skywalker', 'altura': 172, 'edad': 23, 'genero': 'masculino', 'especie': 'Humano', 'planeta_natal': 'Tatooine', 'episodios': [4, 5, 6]},
    {'nombre': 'Princesa Leia', 'altura': 150, 'edad': 22, 'genero': 'femenino', 'especie': 'Humano', 'planeta_natal': 'Alderaan', 'episodios': [4, 5, 6]},
    # Otros personajes...
]

# a. Listar todos los personajes de género femenino
print("Personajes de género femenino:")
print(listar_personajes_genero(personajes_star_wars, 'femenino'))

# b. Listar todos los personajes de especie Droide que aparecieron en los primeros seis episodios de la saga
print("Personajes de especie Droide que aparecieron en los episodios IV, V y VI:")
print(listar_personajes_especie_episodios(personajes_star_wars, 'Droide', [4, 5, 6]))

# c. Mostrar toda la información de Darth Vader y Han Solo
print("Información de Darth Vader y Han Solo:")
print(mostrar_info_personajes(personajes_star_wars, ['Darth Vader', 'Han Solo']))

# d. Listar los personajes que aparecen en el episodio VII y en los tres anteriores
print("Personajes que aparecen en los episodios IV, V, VI y VII:")
print(listar_personajes_episodios(personajes_star_wars, [4, 5, 6, 7]))

# e. Mostrar los personajes con edad mayor a 850 años y de ellos el mayor
print("Personaje con edad mayor a 850 años:")
print(personajes_edad_mayor(personajes_star_wars, 850))

# f. Eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI
print("Personajes que no aparecieron solo en los episodios IV, V y VI:")
print(eliminar_personajes_episodios(personajes_star_wars, [4, 5, 6]))

# g. Listar los personajes de especie humana cuyo planeta de origen es Alderaan
print("Personajes de especie humana cuyo planeta de origen es Alderaan:")
print(listar_personajes_especie_planeta(personajes_star_wars, 'Humano', 'Alderaan'))

# h. Mostrar toda la información de los personajes cuya altura es menor a 70 centímetros
print("Personajes con altura menor a 70 centímetros:")
print(mostrar_info_personajes_altura(personajes_star_wars, 70))

# i. Determinar en qué episodios aparece Chewbacca y mostrar además toda su información
episodios_chewbacca, info_chewbacca = determinar_episodios_personaje(personajes_star_wars, 'Chewbacca')
print(f"Episodios en los que aparece Chewbacca: {episodios_chewbacca}")
print("Información de Chewbacca:")
print(info_chewbacca)
