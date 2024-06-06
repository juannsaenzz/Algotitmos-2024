
#! EJERCICIO 2O

#! Una empresa meteorológica necesita registrar los datos de sus distintas estaciones en las cua-
#! les recolecta la siguiente información proveniente de sus distintas estaciones de adquisición
#! de datos diariamente, implemente las funciones para satisfacer los siguientes requerimientos:

#! a. se deben poder cargar estaciones meteorológicas, de cada una de estas se sabe su país de
#! ubicación, coordenadas de latitud, longitud y altitud;
#! b. estas estaciones registran mediciones de temperatura, presión, humedad y estado del cli-
#! ma –como por ejemplo soleado, nublado, lloviendo, nevando, etcétera– en distintos lapsos
#! temporales, estos datos deberán guardarse en la lista junto con la fecha y la hora de la me-
#! dición;
#! c. mostrar el promedio de temperatura y humedad de todas las estaciones durante el mes
#! de mayo;
#! d. indicar la ubicación de las estaciones meteorológicas en las que en el día actual está llo-
#! viendo o nevando;
#! e. mostrar los datos de las estaciones meteorológicas que hayan registrado estado del clima
#! tormenta eléctrica o huracanes;
#! f. debe implementar el TDA lista de lista.

from datetime import datetime
from collections import defaultdict

# Lista de estaciones meteorológicas
estaciones_meteorologicas = []

def agregar_estacion(pais, latitud, longitud, altitud):
    """Agrega una nueva estación meteorológica a la lista de estaciones."""
    estacion = {
        'pais': pais,
        'coordenadas': {
            'latitud': latitud,
            'longitud': longitud,
            'altitud': altitud
        },
        'mediciones': []
    }
    estaciones_meteorologicas.append(estacion)

def agregar_medicion(estacion_index, fecha, hora, temperatura, presion, humedad, estado_clima):
    """Agrega una nueva medición a una estación específica."""
    medicion = {
        'fecha': fecha,
        'hora': hora,
        'temperatura': temperatura,
        'presion': presion,
        'humedad': humedad,
        'estado_clima': estado_clima
    }
    estaciones_meteorologicas[estacion_index]['mediciones'].append(medicion)

def promedio_temperatura_humedad(mes):
    """Calcula el promedio de temperatura y humedad para un mes específico."""
    total_temp = 0
    total_humedad = 0
    contador = 0

    for estacion in estaciones_meteorologicas:
        for medicion in estacion['mediciones']:
            fecha = datetime.strptime(medicion['fecha'], '%Y-%m-%d')
            if fecha.month == mes:
                total_temp += medicion['temperatura']
                total_humedad += medicion['humedad']
                contador += 1
    
    if contador == 0:
        return None, None

    promedio_temp = total_temp / contador
    promedio_humedad = total_humedad / contador

    return promedio_temp, promedio_humedad

def estaciones_lluvia_nieve(fecha_actual):
    """Devuelve las estaciones donde está lloviendo o nevando en una fecha específica."""
    estaciones_lloviendo_nevando = []

    for estacion in estaciones_meteorologicas:
        for medicion in estacion['mediciones']:
            if medicion['fecha'] == fecha_actual and (medicion['estado_clima'] == 'lloviendo' or medicion['estado_clima'] == 'nevando'):
                estaciones_lloviendo_nevando.append(estacion)
                break

    return estaciones_lloviendo_nevando

def estaciones_tormenta_huracan():
    """Devuelve las estaciones que han registrado tormenta eléctrica o huracanes."""
    estaciones_tormenta_huracan = []

    for estacion in estaciones_meteorologicas:
        for medicion in estacion['mediciones']:
            if medicion['estado_clima'] in ['tormenta eléctrica', 'huracán']:
                estaciones_tormenta_huracan.append(estacion)
                break

    return estaciones_tormenta_huracan

def show_list(title, list_values):
    """Imprime una lista de estaciones meteorológicas de forma estructurada."""
    print(f"\n{title}")
    for index, elemento in enumerate(list_values):
        print(f"{index}. País: {elemento['pais']}, Coordenadas: {elemento['coordenadas']}, Mediciones: {len(elemento['mediciones'])}")
    print()

# Ejemplos de uso

# a. Cargar estaciones meteorológicas
agregar_estacion('Argentina', -34.6037, -58.3816, 25)
agregar_estacion('Brasil', -23.5505, -46.6333, 760)

# b. Registrar mediciones
agregar_medicion(0, '2024-05-15', '14:00', 20.5, 1013, 60, 'soleado')
agregar_medicion(0, '2024-05-16', '14:00', 18.2, 1012, 70, 'nublado')
agregar_medicion(1, '2024-06-05', '09:00', 22.1, 1010, 80, 'lloviendo')
agregar_medicion(1, '2024-05-12', '10:00', 25.3, 1011, 85, 'tormenta eléctrica')

# c. Promedio de temperatura y humedad durante mayo
promedio_temp, promedio_humedad = promedio_temperatura_humedad(5)
print(f"Promedio de temperatura en mayo: {promedio_temp:.2f}°C")
print(f"Promedio de humedad en mayo: {promedio_humedad:.2f}%")

# d. Ubicación de estaciones con lluvia o nieve hoy
fecha_actual = '2024-06-05'
estaciones_lloviendo_nevando = estaciones_lluvia_nieve(fecha_actual)
show_list(f"Estaciones donde está lloviendo o nevando el {fecha_actual}", estaciones_lloviendo_nevando)

# e. Datos de estaciones con tormenta eléctrica o huracanes
estaciones_tormenta_huracan = estaciones_tormenta_huracan()
show_list("Estaciones con tormenta eléctrica o huracanes", estaciones_tormenta_huracan)
