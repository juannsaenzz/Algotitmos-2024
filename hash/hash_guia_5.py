
#! EJERCICIO 5

#! Desarrollar un algoritmo que implemente una tabla hash cerrada para administrar los contac-
#! tos de personas de las cuales se conoce nombre, apellido y correo electrónico, contemplando
#! las siguientes pautas:

#! a. El campo clave para generar las posiciones son el apellido y nombre.
#! b. Deberá contemplar una función de sondeo para resolver las colisiones.

class Contacto:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
    
    def __repr__(self):
        return f'Contacto({self.nombre} {self.apellido}, {self.correo})'

def hash_function(apellido, nombre, table_size):
    clave = apellido + nombre
    hash_value = sum(ord(c) for c in clave) % table_size
    return hash_value

def linear_probe(hash_value, step, table_size):
    return (hash_value + step) % table_size

class TablaHash:
    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [None] * table_size
        self.element_count = 0
    
    def insertar(self, contacto):
        hash_value = hash_function(contacto.apellido, contacto.nombre, self.table_size)
        step = 0
        while self.table[linear_probe(hash_value, step, self.table_size)] is not None:
            step += 1
        self.table[linear_probe(hash_value, step, self.table_size)] = contacto
        self.element_count += 1
    
    def buscar(self, apellido, nombre):
        hash_value = hash_function(apellido, nombre, self.table_size)
        step = 0
        while self.table[linear_probe(hash_value, step, self.table_size)] is not None:
            if self.table[linear_probe(hash_value, step, self.table_size)].apellido == apellido and self.table[linear_probe(hash_value, step, self.table_size)].nombre == nombre:
                return self.table[linear_probe(hash_value, step, self.table_size)]
            step += 1
        return None

# Crear la tabla hash
tabla = TablaHash(10)

# Insertar contactos
tabla.insertar(Contacto("Juan", "Perez", "juan.perez@example.com"))
tabla.insertar(Contacto("Ana", "Garcia", "ana.garcia@example.com"))
tabla.insertar(Contacto("Luis", "Lopez", "luis.lopez@example.com"))

# Buscar contactos
print(tabla.buscar("Perez", "Juan"))  # Debe imprimir el contacto de Juan Perez
print(tabla.buscar("Garcia", "Ana"))  # Debe imprimir el contacto de Ana Garcia
print(tabla.buscar("Lopez", "Luis"))  # Debe imprimir el contacto de Luis Lopez
print(tabla.buscar("Perez", "Carlos"))  # Debe imprimir None (no existe)
