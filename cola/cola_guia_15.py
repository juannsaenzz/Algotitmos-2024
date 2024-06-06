
#! EJERCICIO 15

#! Suponga que se escapa hacia el planeta tierra en un Caza TIE robado –huyendo de un Destruc-
#! tor Estelar y necesita localizar la base rebelde más cercana– y se tiene una cola con informa-
#! ción de las bases rebeldes en la tierra de las cuales conoce su nombre, número de flota aérea,
#! coordenadas de latitud y longitud. Desarrolle un algoritmo que permita resolver las siguientes
#! tareas una vez que aterrice:

#! a. determinar cuál es la base rebelde más cercana desde su posición actual.
#! b. para el cálculo de la distancia deberá utilizar la fórmula de Haversine:

#! donde r es el radio medio de la tierra en metros (6371000), φ1 y φ2 las latitudes de los
#! dos puntos –por ejemplo coordenadas actual–, λ1 y λ2 las longitudes de los dos puntos
#! –coordenadas de la base– ambos expresadas en radianes; para convertir de grados a
#! radianes utilice la función math.radians(ángulo coordenada).

#! c. mostrar el nombre y la distancia a la que se encuentran las tres bases más cercanas y deter-
#! minar cual tiene mayor flota aérea.
#! d. determinar la distancia hasta la base rebelde con mayor flota aérea.