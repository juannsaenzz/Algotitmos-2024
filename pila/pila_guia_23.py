
#! EJERCICIO 23

#! Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
#! obtener la siguiente información sin perder los datos:

#! a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
#! b. calcular el promedio de temperatura (o media) del total de valores;
#! c. determinar la cantidad de valores por encima y por debajo de la media.

from pila import Stack

class TemperaturaStack(Stack):
    def __init__(self):
        super().__init__()

    def agregar_temperatura(self, temperatura):
        self.push(temperatura)

    def obtener_temperaturas(self):
        return self.get_elements()  # Corregido el nombre del método

def obtener_rango_temperatura(pila_temperaturas):
    if pila_temperaturas.size() == 0:
        return None, None

    min_temp = max_temp = pila_temperaturas.on_top()

    # Recorrer la pila para encontrar la temperatura mínima y máxima
    for temperatura in pila_temperaturas.obtener_temperaturas():
        if temperatura < min_temp:
            min_temp = temperatura
        elif temperatura > max_temp:
            max_temp = temperatura

    return min_temp, max_temp


def calcular_promedio_temperatura(pila_temperaturas):
    if pila_temperaturas.size() == 0:
        return None

    suma_temperaturas = sum(pila_temperaturas._elements)
    return suma_temperaturas / pila_temperaturas.size()

def contar_temperaturas_por_encima_y_debajo(pila_temperaturas, promedio):
    if pila_temperaturas.size() == 0:
        return 0, 0
    
    por_encima = por_debajo = 0

    # Contar las temperaturas por encima y por debajo del promedio
    for temperatura in pila_temperaturas._elements:
        if temperatura > promedio:
            por_encima += 1
        elif temperatura < promedio:
            por_debajo += 1

    return por_encima, por_debajo

# Ejemplo de uso:
temperaturas_abril = TemperaturaStack()
temperaturas_abril.agregar_temperatura(20)
temperaturas_abril.agregar_temperatura(22)
temperaturas_abril.agregar_temperatura(25)
temperaturas_abril.agregar_temperatura(18)
temperaturas_abril.agregar_temperatura(21)

min_temp, max_temp = obtener_rango_temperatura(temperaturas_abril)
print("a. Rango de temperatura del mes de abril:")
print("Temperatura mínima:", min_temp)
print("Temperatura máxima:", max_temp)

promedio = calcular_promedio_temperatura(temperaturas_abril)
print("\nb. Promedio de temperatura del mes de abril:", promedio)

por_encima, por_debajo = contar_temperaturas_por_encima_y_debajo(temperaturas_abril, promedio)
print("\nc. Cantidad de días con temperatura por encima y por debajo del promedio:")
print("Días por encima del promedio:", por_encima)
print("Días por debajo del promedio:", por_debajo)
