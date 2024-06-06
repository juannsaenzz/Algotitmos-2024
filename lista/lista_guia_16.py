
#! EJERCICIO 16

#! Se deben administrar las actividades de un proyecto de software, de estas se conoce su costo,
#! tiempo de ejecución, fecha de inicio, fecha de fin estimada, fecha de fin efectiva y persona a
#! cargo. Desarrollar un algoritmo que realice las siguientes actividades:

#! a. tiempo promedio de tareas;
#! b. costo total del proyecto;
#! c. actividades realizadas por una determinada persona;
#! d. mostrar la información de las tareas a realizar entre dos fechas dadas;
#! e. mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo;
#! f. indicar cuántas tareas le quedan pendientes a una determinada persona, indicada por
#! el usuario.

from datetime import datetime, timedelta

# Función para calcular el tiempo promedio de tareas
def tiempo_promedio_tareas(actividades):
    total_tiempos = sum(actividad['tiempo_ejecucion'] for actividad in actividades)
    return total_tiempos / len(actividades)

# Función para calcular el costo total del proyecto
def costo_total_proyecto(actividades):
    return sum(actividad['costo'] for actividad in actividades)

# Función para listar las actividades realizadas por una persona determinada
def actividades_por_persona(actividades, persona):
    return [actividad for actividad in actividades if actividad['persona_a_cargo'] == persona]

# Función para mostrar las tareas a realizar entre dos fechas dadas
def tareas_entre_fechas(actividades, fecha_inicio, fecha_fin):
    return [actividad for actividad in actividades if fecha_inicio <= actividad['fecha_inicio'] <= fecha_fin]

# Función para mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo
def tareas_finalizadas_en_tiempo(actividades):
    finalizadas_tiempo = [actividad for actividad in actividades if actividad['fecha_fin_efectiva'] is not None and actividad['fecha_fin_efectiva'] <= actividad['fecha_fin_estimada']]
    finalizadas_fuera_tiempo = [actividad for actividad in actividades if actividad['fecha_fin_efectiva'] is not None and actividad['fecha_fin_efectiva'] > actividad['fecha_fin_estimada']]
    return finalizadas_tiempo, finalizadas_fuera_tiempo

# Función para contar las tareas pendientes de una persona
def tareas_pendientes_persona(actividades, persona):
    tareas_pendientes = [actividad for actividad in actividades if actividad['fecha_fin_efectiva'] is None and actividad['persona_a_cargo'] == persona]
    return len(tareas_pendientes)

# Ejemplo de uso
actividades = [
    {'nombre': 'Desarrollo de interfaz de usuario', 'costo': 2000, 'tiempo_ejecucion': 10, 'fecha_inicio': datetime(2024, 6, 1), 'fecha_fin_estimada': datetime(2024, 6, 15), 'fecha_fin_efectiva': datetime(2024, 6, 14), 'persona_a_cargo': 'Juan'},
    {'nombre': 'Pruebas de integración', 'costo': 1500, 'tiempo_ejecucion': 8, 'fecha_inicio': datetime(2024, 6, 3), 'fecha_fin_estimada': datetime(2024, 6, 17), 'fecha_fin_efectiva': datetime(2024, 6, 20), 'persona_a_cargo': 'María'},
    {'nombre': 'Optimización de algoritmos', 'costo': 3000, 'tiempo_ejecucion': 12, 'fecha_inicio': datetime(2024, 6, 5), 'fecha_fin_estimada': datetime(2024, 6, 20), 'fecha_fin_efectiva': None, 'persona_a_cargo': 'Juan'}
]

# a. Tiempo promedio de tareas
print("Tiempo promedio de tareas:", tiempo_promedio_tareas(actividades))

# b. Costo total del proyecto
print("Costo total del proyecto:", costo_total_proyecto(actividades))

# c. Actividades realizadas por una determinada persona
print("Actividades realizadas por María:")
for actividad in actividades_por_persona(actividades, 'María'):
    print(actividad['nombre'])

# d. Mostrar la información de las tareas a realizar entre dos fechas dadas
fecha_inicio = datetime(2024, 6, 1)
fecha_fin = datetime(2024, 6, 15)
print("Tareas a realizar entre", fecha_inicio.date(), "y", fecha_fin.date())
for actividad in tareas_entre_fechas(actividades, fecha_inicio, fecha_fin):
    print(actividad['nombre'])

# e. Mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo
finalizadas_tiempo, finalizadas_fuera_tiempo = tareas_finalizadas_en_tiempo(actividades)
print("Tareas finalizadas en tiempo:")
for actividad in finalizadas_tiempo:
    print(actividad['nombre'])
print("Tareas finalizadas fuera de tiempo:")
for actividad in finalizadas_fuera_tiempo:
    print(actividad['nombre'])

# f. Indicar cuántas tareas le quedan pendientes a una determinada persona
persona = 'Juan'
print("Tareas pendientes de", persona + ":", tareas_pendientes_persona(actividades, persona))
