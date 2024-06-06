
#! EJERCICIO 16

#! Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
#! criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
#! siguiente situación:

#! a. cargue tres documentos de empleados (cada documento se representa solamente con
#! un nombre).
#! b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#! c. cargue dos documentos del staff de TI.
#! d. cargue un documento del gerente.
#! e. imprima los dos primeros documentos de la cola.
#! f. cargue dos documentos de empleados y uno de gerente.
#! g. imprima todos los documentos de la cola de impresión.

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            return None

def cargar_documentos(cola, documentos, prioridad):
    for documento in documentos:
        cola.push(documento, prioridad)

def imprimir_primer_documento(cola):
    primer_documento = cola.pop()
    if primer_documento:
        print("Primer documento de la cola:", primer_documento)

def imprimir_primeros_documentos(cola, cantidad):
    for _ in range(cantidad):
        documento = cola.pop()
        if documento:
            print("Documento:", documento)

def imprimir_todos_los_documentos(cola):
    while True:
        documento = cola.pop()
        if documento:
            print("Documento:", documento)
        else:
            break

# Crear la cola de impresión (cola de prioridad)
cola_impresion = PriorityQueue()

# a. Cargar tres documentos de empleados
cargar_documentos(cola_impresion, ["Documento 1 (Empleado)", "Documento 2 (Empleado)", "Documento 3 (Empleado)"], 1)

# b. Imprimir el primer documento de la cola
imprimir_primer_documento(cola_impresion)

# c. Cargar dos documentos del staff de TI
cargar_documentos(cola_impresion, ["Documento 1 (Staff de TI)", "Documento 2 (Staff de TI)"], 2)

# d. Cargar un documento del gerente
cargar_documentos(cola_impresion, ["Documento 1 (Gerente)"], 3)

# e. Imprimir los dos primeros documentos de la cola
imprimir_primeros_documentos(cola_impresion, 2)

# f. Cargar dos documentos de empleados y uno de gerente
cargar_documentos(cola_impresion, ["Documento 4 (Empleado)", "Documento 5 (Empleado)", "Documento 2 (Gerente)"], 1)

# g. Imprimir todos los documentos de la cola de impresión
print("Todos los documentos en la cola de impresión:")
imprimir_todos_los_documentos(cola_impresion)
