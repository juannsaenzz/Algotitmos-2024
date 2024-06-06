
#! EJERCICIO 21

#! Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
#! nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recau-
#! dación. Desarrolle los algoritmos necesarios para realizar las siguientes tareas:

#! a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determina-
#! do año–;
#! b. mostrar los datos de la película que más recaudo;
#! c. indicar las películas con mayor valoración del público, puede ser más de una;
#! d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una
#! lista auxiliar–:
#! I. por nombre,
#! II. por recaudación,
#! III. por año de estreno,
#! IV. por valoración del público.

peliculas = [
    {'nombre': 'Pelicula A', 'valoracion': 8.5, 'anio': 2020, 'recaudacion': 500000},
    {'nombre': 'Pelicula B', 'valoracion': 9.0, 'anio': 2021, 'recaudacion': 800000},
    {'nombre': 'Pelicula C', 'valoracion': 7.5, 'anio': 2019, 'recaudacion': 300000},
    {'nombre': 'Pelicula D', 'valoracion': 9.0, 'anio': 2020, 'recaudacion': 1200000},
    {'nombre': 'Pelicula E', 'valoracion': 6.5, 'anio': 2021, 'recaudacion': 450000},
]

def filtrar_por_anio(peliculas, anio):
    return [pelicula for pelicula in peliculas if pelicula['anio'] == anio]

def pelicula_mayor_recaudacion(peliculas):
    if not peliculas:
        return None
    return max(peliculas, key=lambda pelicula: pelicula['recaudacion'])

def peliculas_mejor_valoradas(peliculas):
    if not peliculas:
        return []
    max_valoracion = max(pelicula['valoracion'] for pelicula in peliculas)
    return [pelicula for pelicula in peliculas if pelicula['valoracion'] == max_valoracion]

def ordenar_por_nombre(peliculas):
    return sorted(peliculas, key=lambda pelicula: pelicula['nombre'])

def ordenar_por_recaudacion(peliculas):
    return sorted(peliculas, key=lambda pelicula: pelicula['recaudacion'], reverse=True)

def ordenar_por_anio(peliculas):
    return sorted(peliculas, key=lambda pelicula: pelicula['anio'])

def ordenar_por_valoracion(peliculas):
    return sorted(peliculas, key=lambda pelicula: pelicula['valoracion'], reverse=True)

def show_list(title, list_values):
    print(f"\n{title}")
    for index, elemento in enumerate(list_values):
        print(f"{index}. Nombre: {elemento['nombre']}, Valoración: {elemento['valoracion']}, Año: {elemento['anio']}, Recaudación: {elemento['recaudacion']}")
    print()

# Ejemplos de uso

# a. Filtrar las películas por año
anio = 2020
peliculas_anio = filtrar_por_anio(peliculas, anio)
show_list(f"Películas del año {anio}", peliculas_anio)

# b. Mostrar los datos de la película que más recaudó
pelicula_top_recaudacion = pelicula_mayor_recaudacion(peliculas)
print(f"Película que más recaudó: Nombre: {pelicula_top_recaudacion['nombre']}, Valoración: {pelicula_top_recaudacion['valoracion']}, Año: {pelicula_top_recaudacion['anio']}, Recaudación: {pelicula_top_recaudacion['recaudacion']}")

# c. Indicar las películas con mayor valoración del público
mejor_valoradas = peliculas_mejor_valoradas(peliculas)
show_list("Películas con mayor valoración", mejor_valoradas)

# d. Mostrar el contenido de la lista en los siguientes criterios de orden
# I. Por nombre
peliculas_ordenadas_nombre = ordenar_por_nombre(peliculas)
show_list("Películas ordenadas por nombre", peliculas_ordenadas_nombre)

# II. Por recaudación
peliculas_ordenadas_recaudacion = ordenar_por_recaudacion(peliculas)
show_list("Películas ordenadas por recaudación", peliculas_ordenadas_recaudacion)

# III. Por año de estreno
peliculas_ordenadas_anio = ordenar_por_anio(peliculas)
show_list("Películas ordenadas por año de estreno", peliculas_ordenadas_anio)

# IV. Por valoración del público
peliculas_ordenadas_valoracion = ordenar_por_valoracion(peliculas)
show_list("Películas ordenadas por valoración del público", peliculas_ordenadas_valoracion)
