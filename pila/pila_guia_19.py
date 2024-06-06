
#! EJERCICIO 19

#! Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
#! treno, desarrollar las funciones necesarias para resolver las siguientes actividades:

#! a. mostrar los nombre películas estrenadas en el año 2014;
#! b. indicar cuántas películas se estrenaron en el año 2018;
#! c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

from pila import Stack

def peliculas_2014(pila):
    print("Tamaño de la pila al inicio de la función peliculas_2014:", pila.size())
    peliculas_encontradas = []  # Lista para almacenar las películas encontradas
    pila_aux = Stack()
    while pila.size() > 0:
        pelicula = pila.pop()
        if pelicula[2] == 2014:  # Comprobando el año de estreno
            peliculas_encontradas.append(pelicula[0])  # Almacenando el nombre de la película
        pila_aux.push(pelicula)
    
    # Devolver las películas nuevamente a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    print("Tamaño de la pila al final de la función peliculas_2014:", pila.size())

    # Imprimir las películas encontradas en orden inverso
    for pelicula in reversed(peliculas_encontradas):
        print(pelicula)

# Ejemplo de uso:
pila_peliculas = Stack()
pila_peliculas.push(("Interstellar", "Paramount Pictures", 2014))
pila_peliculas.push(("The Grand Budapest Hotel", "Fox Searchlight Pictures", 2014))
pila_peliculas.push(("Guardians of the Galaxy", "Marvel Studios", 2014))

print("Películas estrenadas en 2014:")
peliculas_2014(pila_peliculas)

def cantidad_peliculas_2018(pila):
    contador = 0
    print("Tamaño de la pila al inicio de la función cantidad_peliculas_2018:", pila.size())
    pila_aux = Stack()
    while pila.size() > 0:
        pelicula = pila.pop()
        if pelicula[2] == 2018:  # Comprobando el año de estreno
            contador += 1
        pila_aux.push(pelicula)
    
    # Devolver las películas nuevamente a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    print("Tamaño de la pila al final de la función cantidad_peliculas_2018:", pila.size())

    return contador

# Ejemplo de uso:
pila_peliculas = Stack()
pila_peliculas.push(("Black Panther", "Marvel Studios", 2018))
pila_peliculas.push(("Avengers: Infinity War", "Marvel Studios", 2018))
pila_peliculas.push(("Deadpool 2", "20th Century Fox", 2018))
pila_peliculas.push(("Incredibles 2", "Pixar Animation Studios", 2018))

print("Cantidad de películas estrenadas en 2018:", cantidad_peliculas_2018(pila_peliculas))

def peliculas_marvel_2016(pila):
    print("Tamaño de la pila al inicio de la función peliculas_marvel_2016:", pila.size())
    pila_aux = Stack()
    while pila.size() > 0:
        pelicula = pila.pop()
        if pelicula[1] == "Marvel Studios" and pelicula[2] == 2016:  # Comprobando estudio y año de estreno
            print(pelicula[0])  # Imprimiendo el nombre de la película
        pila_aux.push(pelicula)
    
    # Devolver las películas nuevamente a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    print("Tamaño de la pila al final de la función peliculas_marvel_2016:", pila.size())

# Ejemplo de uso:
pila_peliculas = Stack()
pila_peliculas.push(("Captain America: Civil War", "Marvel Studios", 2016))
pila_peliculas.push(("Doctor Strange", "Marvel Studios", 2016))
pila_peliculas.push(("Rogue One: A Star Wars Story", "Lucasfilm", 2016))
pila_peliculas.push(("Fantastic Beasts and Where to Find Them", "Warner Bros.", 2016))

print("Películas de Marvel Studios estrenadas en 2016:")
peliculas_marvel_2016(pila_peliculas)
