
#! EJERCICIO 10

#! Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
#! de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
#! resolver las siguientes actividades:

#! a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#! b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
#! la palabra ‘Python’, si perder datos en la cola;
#! c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
#! 11:43 y las 15:57, y determinar cuántas son.

from cola import Queue
from pila import Stack

def eliminar_notificaciones_facebook(cola):
    while cola.size() > 0:
        notificacion = cola.attention()
        if notificacion["app"] != "Facebook":
            cola.arrive(notificacion)
    
    print("\nCola después de eliminar notificaciones de Facebook:")
    for notificacion in cola._Queue__elements:
        print(notificacion)


def mostrar_notificaciones_twitter_python(cola):
    notificaciones_temporales = Queue()
    while cola.size() > 0:
        notificacion = cola.attention()
        if notificacion["app"] == "Twitter" and "Python" in notificacion["mensaje"]:
            print(notificacion)
        else:
            notificaciones_temporales.arrive(notificacion)
    while notificaciones_temporales.size() > 0:
        cola.arrive(notificaciones_temporales.attention())


def contar_notificaciones_entre_horas(cola):
    pila_temporal = Stack()
    while cola.size() > 0:
        notificacion = cola.attention()
        hora = notificacion["hora"]
        if hora >= "11:43" and hora <= "15:57":
            pila_temporal.push(notificacion)
    cantidad = pila_temporal.size()
    return cantidad


# Ejemplo de uso
cola_notificaciones = Queue()
cola_notificaciones.arrive({"hora": "10:30", "app": "Facebook", "mensaje": "Hola"})
cola_notificaciones.arrive({"hora": "12:15", "app": "Twitter", "mensaje": "Python es genial"})
cola_notificaciones.arrive({"hora": "14:30", "app": "Twitter", "mensaje": "Aprendiendo Python"})
cola_notificaciones.arrive({"hora": "15:00", "app": "Facebook", "mensaje": "Nueva publicación"})
cola_notificaciones.arrive({"hora": "16:00", "app": "Twitter", "mensaje": "Python rocks"})
cola_notificaciones.arrive({"hora": "13:00", "app": "Instagram", "mensaje": "Foto del día"})

print("Cola original:")
for notificacion in cola_notificaciones._Queue__elements:
    print(notificacion)

eliminar_notificaciones_facebook(cola_notificaciones)
