
#! EJERCICIO 13

#! Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
#! verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
#! usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
#! las siguientes actividades:

#! a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
#! además mostrar el nombre de dichas películas;
#! b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
#! c. eliminar los modelos de los trajes destruidos mostrando su nombre;
#! d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
#! más de un modelo de traje, estos deben cargarse por separado;
#! e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
#! repetidos en una misma película;
#! f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
#! “Capitan America: Civil War”.

from pila import Stack

def hulkbuster_utilizado(pila):
    peliculas = []
    temp_pila = Stack()

    # Verificar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna película
    hulkbuster_encontrado = False
    while pila.size() > 0:
        traje = pila.pop()
        temp_pila.push(traje)
        if traje[0] == "Mark XLIV":
            hulkbuster_encontrado = True
            peliculas.append(traje[1])  # Agregar el nombre de la película
    # Restaurar la pila original
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    if hulkbuster_encontrado:
        print("El modelo Mark XLIV (Hulkbuster) fue utilizado en las siguientes películas:", peliculas)
    else:
        print("El modelo Mark XLIV (Hulkbuster) no fue utilizado en ninguna película.")

def trajes_dañados(pila):
    print("Modelos de trajes que quedaron dañados:")
    temp_pila = Stack()

    # Mostrar los modelos que quedaron dañados
    while pila.size() > 0:
        traje = pila.pop()
        if traje[2] == "Dañado":
            print(traje[0])  # Mostrar el nombre del modelo
        temp_pila.push(traje)
    # Restaurar la pila original
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

def eliminar_trajes_destruidos(pila):
    print("Modelos de trajes destruidos:")
    temp_pila = Stack()

    # Eliminar los modelos de trajes destruidos
    while pila.size() > 0:
        traje = pila.pop()
        if traje[2] != "Destruido":
            temp_pila.push(traje)
        else:
            print(traje[0])  # Mostrar el nombre del modelo
    # Restaurar la pila original sin los trajes destruidos
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

def agregar_modelo(pila, modelo, pelicula, estado):
    # Verificar si el modelo ya existe en la pila para la película dada
    modelo_existente = False
    temp_pila = Stack()
    while pila.size() > 0:
        traje = pila.pop()
        temp_pila.push(traje)
        if traje[0] == modelo and traje[1] == pelicula:
            modelo_existente = True
    # Restaurar la pila original
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    if not modelo_existente:
        pila.push((modelo, pelicula, estado))

def trajes_en_peliculas(pila, peliculas):
    print("Modelos de trajes utilizados en las películas", peliculas, ":")
    temp_pila = Stack()

    # Mostrar los modelos de trajes utilizados en las películas dadas
    while pila.size() > 0:
        traje = pila.pop()
        temp_pila.push(traje)
        if traje[1] in peliculas:
            print(traje[0])  # Mostrar el nombre del modelo
    # Restaurar la pila original
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

# Ejemplo de uso:
trajes = Stack()
trajes.push(("Mark I", "Iron Man", "Destruido"))
trajes.push(("Mark II", "Iron Man 2", "Destruido"))
trajes.push(("Mark III", "Iron Man", "Impecable"))
trajes.push(("Mark XLIV", "Avengers: Age of Ultron", "Destruido"))

hulkbuster_utilizado(trajes)
trajes_dañados(trajes)
eliminar_trajes_destruidos(trajes)
agregar_modelo(trajes, "Mark LXXXV", "Avengers: Endgame", "Impecable")
trajes_en_peliculas(trajes, ["Spider-Man: Homecoming", "Captain America: Civil War"])
