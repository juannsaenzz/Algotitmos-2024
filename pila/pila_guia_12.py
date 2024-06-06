
#! EJERCICIO 12

#! Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
#! que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.

from pila import Stack

def verificar_personajes(pila):
    leia_presente = False
    boba_fett_presente = False
    
    # Pila auxiliar para almacenar temporalmente los datos
    temp_pila = Stack()

    # Iterar sobre la pila para verificar la presencia de Leia Organa y Boba Fett
    while pila.size() > 0:
        nombre = pila.pop()
        temp_pila.push(nombre)
        if nombre == "Leia Organa":
            leia_presente = True
        elif nombre == "Boba Fett":
            boba_fett_presente = True

    # Restaurar la pila original
    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())
    
    return leia_presente, boba_fett_presente

# Ejemplo de uso:
personajes = Stack()
personajes.push("Luke Skywalker")
personajes.push("Leia Organa")
personajes.push("Han Solo")
personajes.push("Darth Vader")
personajes.push("Boba Fett")

leia_presente, boba_fett_presente = verificar_personajes(personajes)

if leia_presente:
    print("Leia Organa está en la pila.")
else:
    print("Leia Organa NO está en la pila.")

if boba_fett_presente:
    print("Boba Fett está en la pila.")
else:
    print("Boba Fett NO está en la pila.")
