
#! EJERCICIO 17

#! Desarrollar un algoritmo que permita cargar procesos a la cola de ejecución de un procesador,
#! de los cuales se conoce id del proceso y tiempo de ejecución. Resuelva las siguientes situaciones:

#! a. simular la atención de los procesos de la cola transcurriendo su tiempo –utilizando la fun-
#! ción time.sleep (segundos) – hasta que se vacíe la cola.
#! b. considerar que el quantum de tiempo asignado por el procesador a cada proceso es como
#! máximo 4.5 segundos –si el proceso no terminó su ejecución deberá volver a la cola con el
#! tiempo restante para terminar su ejecución–.
#! c. cuando se realiza el cambio de proceso, porque finalizó su ejecución o porque se le agotó el
#! quantum de tiempo, se pueden ingresar nuevos procesos a la cola por el usuario.
#! d. no se aplican criterios de prioridad en los procesos.

import queue
import time

class Proceso:
    def __init__(self, id_proceso, tiempo_ejecucion):
        self.id_proceso = id_proceso
        self.tiempo_ejecucion = tiempo_ejecucion

def cargar_proceso(cola_ejecucion, id_proceso, tiempo_ejecucion):
    proceso = Proceso(id_proceso, tiempo_ejecucion)
    cola_ejecucion.put(proceso)
    print(f"Proceso {id_proceso} cargado en la cola de ejecución.")

def simular_ejecucion(cola_ejecucion):
    while not cola_ejecucion.empty():
        proceso_actual = cola_ejecucion.get()
        tiempo_restante = proceso_actual.tiempo_ejecucion
        print(f"Ejecutando proceso {proceso_actual.id_proceso} por {tiempo_restante} segundos.")
        while tiempo_restante > 0:
            tiempo_sleep = min(tiempo_restante, 4.5)  # Quantum de tiempo máximo de 4.5 segundos
            time.sleep(tiempo_sleep)
            tiempo_restante -= tiempo_sleep
            if tiempo_restante > 0:
                print(f"Proceso {proceso_actual.id_proceso} suspendido. Tiempo restante: {tiempo_restante} segundos.")
            else:
                print(f"Proceso {proceso_actual.id_proceso} terminado.")
        # Se puede ingresar nuevos procesos a la cola por el usuario (no implementado en este ejemplo)

# Crear la cola de ejecución
cola_ejecucion = queue.Queue()

# Cargar procesos a la cola de ejecución
cargar_proceso(cola_ejecucion, 1, 8)
cargar_proceso(cola_ejecucion, 2, 5)
cargar_proceso(cola_ejecucion, 3, 3)

# Simular la ejecución de los procesos en la cola
simular_ejecucion(cola_ejecucion)
