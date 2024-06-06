
#! EJERCICIO 22

#! Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The
#! Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada
#! misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó,
#! costo de la recompensa. Resolver las siguientes actividades:

#! a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno
#! de los cazzarrecompensas;
#! b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
#! quien obtuvo mayor fortuna;
#! c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la
#! que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
#! d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

from pila import Stack

class Bitacora:
    def __init__(self, planeta, objetivo, recompensa):
        self.planeta = planeta
        self.objetivo = objetivo
        self.recompensa = recompensa

def mostrar_planetas_visitados(pila_bitacoras):
    planetas_boba_fett = []
    planetas_din_djarin = []

    # Separar las bitácoras por cazarrecompensas
    while pila_bitacoras.size() > 0:
        bitacora = pila_bitacoras.pop()
        if bitacora.objetivo == "Boba Fett":
            planetas_boba_fett.append(bitacora.planeta)
        elif bitacora.objetivo == "Din Djarin":
            planetas_din_djarin.append(bitacora.planeta)

    # Mostrar los planetas visitados por cada cazarrecompensas
    print("Planetas visitados por Boba Fett:")
    for planeta in planetas_boba_fett:
        print(planeta)
    
    print("\nPlanetas visitados por Din Djarin:")
    for planeta in planetas_din_djarin:
        print(planeta)

def recaudacion_total(pila_bitacoras):
    total_boba_fett = 0
    total_din_djarin = 0

    # Calcular la recaudación total de cada cazarrecompensas
    while pila_bitacoras.size() > 0:
        bitacora = pila_bitacoras.pop()
        if bitacora.objetivo == "Boba Fett":
            total_boba_fett += bitacora.recompensa
        elif bitacora.objetivo == "Din Djarin":
            total_din_djarin += bitacora.recompensa

    return total_boba_fett, total_din_djarin

def mayor_fortuna(total_boba_fett, total_din_djarin):
    if total_boba_fett > total_din_djarin:
        return "Boba Fett"
    elif total_boba_fett < total_din_djarin:
        return "Din Djarin"
    else:
        return "Ambos tienen la misma fortuna"

def numero_mision_han_solo(pila_bitacoras):
    mision = 0

    # Buscar la misión en la que Boba Fett capturó a Han Solo
    while pila_bitacoras.size() > 0:
        mision += 1
        bitacora = pila_bitacoras.pop()
        if bitacora.objetivo == "Boba Fett" and bitacora.planeta == "Tatooine" and bitacora.recompensa == 100000:
            return mision

    return "Han Solo no fue capturado por Boba Fett"

def capturas_realizadas(pila_bitacoras):
    capturas_boba_fett = 0
    capturas_din_djarin = 0

    # Contar las capturas realizadas por cada cazarrecompensas
    while pila_bitacoras.size() > 0:
        bitacora = pila_bitacoras.pop()
        if bitacora.objetivo == "Boba Fett":
            capturas_boba_fett += 1
        elif bitacora.objetivo == "Din Djarin":
            capturas_din_djarin += 1

    return capturas_boba_fett, capturas_din_djarin

# Ejemplo de uso corregido:
bitacoras = Stack()
bitacoras.push(Bitacora("Tatooine", "Boba Fett", 100000))
bitacoras.push(Bitacora("Tatooine", "Din Djarin", 30000))
bitacoras.push(Bitacora("Navarro", "Din Djarin", 50000))
bitacoras.push(Bitacora("Tatooine", "Boba Fett", 50000))

print("a. Planetas visitados por cada cazarrecompensas:")
mostrar_planetas_visitados(bitacoras)

total_boba_fett, total_din_djarin = recaudacion_total(bitacoras)
print("\nb. Recaudación total:")
print("Total recaudado por Boba Fett:", total_boba_fett)
print("Total recaudado por Din Djarin:", total_din_djarin)
print("El cazarrecompensas con mayor fortuna:", mayor_fortuna(total_boba_fett, total_din_djarin))

print("\nc. Número de la misión en la que Boba Fett capturó a Han Solo:", numero_mision_han_solo(bitacoras))

capturas_boba_fett, capturas_din_djarin = capturas_realizadas(bitacoras)
print("\nd. Cantidad de capturas realizadas por cada cazarrecompensas:")
print("Capturas realizadas por Boba Fett:", capturas_boba_fett)
print("Capturas realizadas por Din Djarin:", capturas_din_djarin)
