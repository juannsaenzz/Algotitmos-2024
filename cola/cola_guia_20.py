
#! EJERCICIO 20

#! Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro),
#! que resuelva las siguientes actividades:

#! a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son
#! los siguientes:
#! I. automóviles (tarifa $47);
#! II. camionetas (tarifa $59);
#! III. camiones (tarifa $71);
#! IV. colectivos (tarifa $64).
#! b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
#! c. determinar qué cabina recaudó mayor cantidad de pesos ($).
#! d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.

import random
from queue import Queue

# Función para agregar vehículos aleatoriamente a las cabinas de cobro
def agregar_vehiculos(cabinas):
    tipos_vehiculos = ['automóviles', 'camionetas', 'camiones', 'colectivos']
    for _ in range(30):
        tipo_vehiculo = random.choice(tipos_vehiculos)
        if tipo_vehiculo == 'automóviles':
            tarifa = 47
        elif tipo_vehiculo == 'camionetas':
            tarifa = 59
        elif tipo_vehiculo == 'camiones':
            tarifa = 71
        else:
            tarifa = 64
        cabina = random.choice(cabinas)
        cabina.put((tipo_vehiculo, tarifa))

# Función para realizar la atención de las cabinas
def atender_cabinas(cabinas):
    total_recaudado = [0] * len(cabinas)
    total_vehiculos = [0] * len(cabinas)
    tipos_vehiculos = ['automóviles', 'camionetas', 'camiones', 'colectivos']
    for i, cabina in enumerate(cabinas):
        print(f"Atendiendo cabina {i+1}:")
        while not cabina.empty():
            tipo_vehiculo, tarifa = cabina.get()
            total_recaudado[i] += tarifa
            total_vehiculos[i] += 1
            print(f"Vehículo: {tipo_vehiculo} - Tarifa: ${tarifa}")
        print(f"Total recaudado en cabina {i+1}: ${total_recaudado[i]}")
        print(f"Cantidad de vehículos atendidos en cabina {i+1}: {total_vehiculos[i]}")
        print()

# Función para determinar qué cabina recaudó mayor cantidad de dinero
def cabina_mayor_recaudacion(cabinas):
    total_recaudado = [sum(c.queue[1] for c in cabina.queue) for cabina in cabinas]
    cabina_max_recaudacion = total_recaudado.index(max(total_recaudado)) + 1
    print(f"La cabina con mayor recaudación es la cabina {cabina_max_recaudacion}.")

# Función para determinar cuántos vehículos de cada tipo se atendieron en cada cabina
def vehiculos_por_cabina(cabinas):
    tipos_vehiculos = ['automóviles', 'camionetas', 'camiones', 'colectivos']
    for i, cabina in enumerate(cabinas):
        cantidad_vehiculos = {tipo: sum(1 for v in list(cabina.queue) if v[0] == tipo) for tipo in tipos_vehiculos}
        print(f"En cabina {i+1}: {cantidad_vehiculos}")

# Crear las cabinas de cobro
cabina_1 = Queue()
cabina_2 = Queue()
cabina_3 = Queue()
cabinas = [cabina_1, cabina_2, cabina_3]

# a. Agregar 30 vehículos de manera aleatoria a las cabinas de cobro
agregar_vehiculos(cabinas)

# b. Realizar la atención de las cabinas
atender_cabinas(cabinas)

# c. Determinar qué cabina recaudó mayor cantidad de dinero
cabina_mayor_recaudacion(cabinas)

# d. Determinar cuántos vehículos de cada tipo se atendieron en cada cabina
vehiculos_por_cabina(cabinas)
