
#! EJERCICIO 17

#! Se cuenta con los vuelos del aeropuerto de Heraklion en Creta, de estos se sabe la siguiente
#! información: empresa, número del vuelo, cantidad de asientos del avión, fecha de salida, des-
#! tino, kms del vuelo. Y además se conoce los datos de cantidades de asientos totales y ocupados
#! por clase (primera y turista). Implemente las funciones necesarias que permitan realizar las
#! siguiente actividades:

#! a. mostrar los vuelos con destino a Atenas, Miconos y Rodas;
#! b. mostrar los vuelos con asientos clase turista disponible;
#! c. mostrar el total recaudado por cada vuelo, considerando clase turista ($75 por kilómetro) y
#! primera clase ($203 por kilómetro);
#! d. mostrar los vuelos programados para una determinada fecha;
#! e. vender un asiento (o pasaje) para un determinado vuelo;
#! f. eliminar un vuelo. Tener en cuenta que si tiene pasajes vendidos, se debe indicar la canti-
#! dad de dinero a devovler;
#! g. mostrar las empresas y los kilómetros de vuelos con destino a Tailandia.

from datetime import datetime

# Función para mostrar los vuelos con destino a los destinos especificados
def vuelos_destino(vuelos, destinos):
    vuelos_destino = []
    for vuelo in vuelos:
        if vuelo['destino'] in destinos:
            vuelos_destino.append(vuelo)
    return vuelos_destino

# Función para mostrar los vuelos con asientos clase turista disponibles
def vuelos_turista_disponible(vuelos):
    vuelos_turista = []
    for vuelo in vuelos:
        if vuelo['asientos_turista_ocupados'] < vuelo['asientos_turista_totales']:
            vuelos_turista.append(vuelo)
    return vuelos_turista

# Función para calcular el total recaudado por cada vuelo
def total_recaudado(vuelos):
    for vuelo in vuelos:
        precio_turista = vuelo['kms'] * 75
        precio_primera = vuelo['kms'] * 203
        total = precio_turista * vuelo['asientos_turista_ocupados'] + precio_primera * vuelo['asientos_primera_ocupados']
        vuelo['total_recaudado'] = total
    return vuelos

# Función para mostrar los vuelos programados para una determinada fecha
def vuelos_por_fecha(vuelos, fecha):
    vuelos_fecha = []
    for vuelo in vuelos:
        if vuelo['fecha_salida'].date() == fecha.date():
            vuelos_fecha.append(vuelo)
    return vuelos_fecha

# Función para vender un asiento para un determinado vuelo
def vender_asiento(vuelos, numero_vuelo, clase):
    for vuelo in vuelos:
        if vuelo['numero'] == numero_vuelo:
            if clase == 'turista' and vuelo['asientos_turista_ocupados'] < vuelo['asientos_turista_totales']:
                vuelo['asientos_turista_ocupados'] += 1
                return True
            elif clase == 'primera' and vuelo['asientos_primera_ocupados'] < vuelo['asientos_primera_totales']:
                vuelo['asientos_primera_ocupados'] += 1
                return True
            else:
                return False
    return False

# Función para eliminar un vuelo
def eliminar_vuelo(vuelos, numero_vuelo):
    for vuelo in vuelos:
        if vuelo['numero'] == numero_vuelo:
            if vuelo['asientos_turista_ocupados'] == 0 and vuelo['asientos_primera_ocupados'] == 0:
                vuelos.remove(vuelo)
                return "El vuelo ha sido eliminado."
            else:
                total_reembolso = (vuelo['asientos_turista_ocupados'] * 75 + vuelo['asientos_primera_ocupados'] * 203)
                vuelos.remove(vuelo)
                return f"El vuelo ha sido eliminado. Total de reembolso: {total_reembolso}"
    return "Vuelo no encontrado."

# Función para mostrar las empresas y los kilómetros de vuelos con destino a un país
def vuelos_por_pais(vuelos, pais):
    vuelos_pais = []
    for vuelo in vuelos:
        if pais in vuelo['destino']:
            vuelos_pais.append({'empresa': vuelo['empresa'], 'kms': vuelo['kms']})
    return vuelos_pais

# Datos de prueba
vuelos = [
    {'empresa': 'Iberia', 'numero': 'IB123', 'asientos_turista_totales': 150, 'asientos_turista_ocupados': 100, 'asientos_primera_totales': 20, 'asientos_primera_ocupados': 10, 'fecha_salida': datetime(2024, 6, 10, 8, 0), 'destino': 'Atenas', 'kms': 500},
    {'empresa': 'Ryanair', 'numero': 'FR456', 'asientos_turista_totales': 200, 'asientos_turista_ocupados': 180, 'asientos_primera_totales': 30, 'asientos_primera_ocupados': 25, 'fecha_salida': datetime(2024, 6, 12, 10, 0), 'destino': 'Miconos', 'kms': 600},
    {'empresa': 'Lufthansa', 'numero': 'LH789', 'asientos_turista_totales': 180, 'asientos_turista_ocupados': 170, 'asientos_primera_totales': 25, 'asientos_primera_ocupados': 20, 'fecha_salida': datetime(2024, 6, 15, 12, 0), 'destino': 'Rodas', 'kms': 700}
]

# Prueba de la función vuelos_destino
print("Vuelos con destino a Atenas, Miconos y Rodas:")
destinos = ['Atenas', 'Miconos', 'Rodas']
print(vuelos_destino(vuelos, destinos))

# Prueba de la función vuelos_turista_disponible
print("\nVuelos con asientos clase turista disponibles:")
print(vuelos_turista_disponible(vuelos))

# Prueba de la función total_recaudado
print("\nTotal recaudado por cada vuelo:")
print(total_recaudado(vuelos))

# Prueba de la función vuelos_por_fecha
print("\nVuelos programados para el 12 de junio de 2024:")
fecha = datetime(2024, 6, 12)
print(vuelos_por_fecha(vuelos, fecha))

# Prueba de la función vender_asiento
print("\nVenta de un asiento en el vuelo IB123, clase turista:")
print(vender_asiento(vuelos, 'IB123', 'turista'))

# Prueba de la función eliminar_vuelo
print("\nEliminación del vuelo IB123:")
print(eliminar_vuelo(vuelos, 'IB123'))

# Prueba de la función vuelos_por_pais
print("\nEmpresas y kilómetros de vuelos con destino a Grecia:")
print(vuelos_por_pais(vuelos, 'Grecia'))
