
#! EJERCICIO 10

#! Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artis-
#! ta, duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que
#! permita realizar las siguientes actividades:

#! a. obtener la información de la canción más larga;
#! b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
#! c. obtener todas las canciones de la banda Arctic Monkeys;
#! d. mostrar los nombres de las bandas o artistas que solo son de una palabra.

def cancion_mas_larga(canciones):
    """Obtiene la información de la canción más larga."""
    if not canciones:
        return None
    return max(canciones, key=lambda x: x['duracion'])

def top_n_mas_escuchadas(canciones, n):
    """Obtiene el TOP N de canciones más escuchadas."""
    if not canciones:
        return None
    return sorted(canciones, key=lambda x: x['reproducciones'], reverse=True)[:n]

def canciones_por_banda(canciones, banda):
    """Obtiene todas las canciones de una banda específica."""
    return [cancion for cancion in canciones if cancion['banda'] == banda]

def bandas_una_palabra(canciones):
    """Obtiene los nombres de las bandas o artistas que son de una sola palabra."""
    return set([cancion['banda'] for cancion in canciones if len(cancion['banda'].split()) == 1])

# Suponiendo que 'canciones' es una lista de diccionarios con la información de las canciones
# Ejemplo de uso:

canciones = [
    {'nombre': 'Somebody to Love', 'banda': 'Queen', 'duracion': 210, 'reproducciones': 1000000},
    {'nombre': 'Bohemian Rhapsody', 'banda': 'Queen', 'duracion': 356, 'reproducciones': 1500000},
    {'nombre': 'Do I Wanna Know?', 'banda': 'Arctic Monkeys', 'duracion': 275, 'reproducciones': 800000},
    {'nombre': 'R U Mine?', 'banda': 'Arctic Monkeys', 'duracion': 202, 'reproducciones': 1200000},
    # Otras canciones...
]

# a. Obtener la información de la canción más larga
print("Información de la canción más larga:")
print(cancion_mas_larga(canciones))

# b. Obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas
print("TOP 5 de canciones más escuchadas:")
print(top_n_mas_escuchadas(canciones, 5))
print("TOP 10 de canciones más escuchadas:")
print(top_n_mas_escuchadas(canciones, 10))
print("TOP 40 de canciones más escuchadas:")
print(top_n_mas_escuchadas(canciones, 40))

# c. Obtener todas las canciones de la banda Arctic Monkeys
print("Canciones de Arctic Monkeys:")
print(canciones_por_banda(canciones, 'Arctic Monkeys'))

# d. Mostrar los nombres de las bandas o artistas que solo son de una palabra
print("Bandas o artistas de una sola palabra:")
print(bandas_una_palabra(canciones))
