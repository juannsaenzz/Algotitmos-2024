
#! EJERCICIO 3

#! Implementar un tabla hash cerrada para guardar las cátedras de una carrera universitaria de
#! acuerdo a su código, que permita resolver las siguientes actividades:

#! a. cargar cátedras de una carrera de las cuales se conoce nombre, modalidad (anual o cuatri-
#! mestral), cantidad de horas;
#! b. además se deben poder agregar los docentes vinculados con las cátedras;
#! c. debe ser una tabla cerrada;
#! d. debe poder solucionar las colisiones;
#! e. no podrán estar cargadas de manera correlativa de acuerdo a un número.

class Catedra:
    def __init__(self, codigo, nombre, modalidad, horas):
        self.codigo = codigo
        self.nombre = nombre
        self.modalidad = modalidad
        self.horas = horas
        self.docentes = []

class TablaHashCerrada:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = Catedra(None, None, None, None)  # Indicador especial para celdas borradas

    def hash_function(self, key):
        return int(key) % self.size

    def agregar_catedra(self, codigo, nombre, modalidad, horas):
        index = self.hash_function(codigo)
        original_index = index
        while self.table[index] is not None and self.table[index].codigo != codigo:
            if self.table[index] == self.deleted:
                break
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("La tabla hash está llena.")
        self.table[index] = Catedra(codigo, nombre, modalidad, horas)

    def agregar_docente(self, codigo, docente):
        index = self.hash_function(codigo)
        original_index = index
        while self.table[index] is not None:
            if self.table[index].codigo == codigo:
                self.table[index].docentes.append(docente)
                return
            index = (index + 1) % self.size
            if index == original_index:
                break
        raise Exception("Cátedra no encontrada.")

    def obtener_catedra(self, codigo):
        index = self.hash_function(codigo)
        original_index = index
        while self.table[index] is not None:
            if self.table[index].codigo == codigo:
                return self.table[index]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def borrar_catedra(self, codigo):
        index = self.hash_function(codigo)
        original_index = index
        while self.table[index] is not None:
            if self.table[index].codigo == codigo:
                self.table[index] = self.deleted
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False

# Pruebas
# Crear la tabla hash con 28 posiciones
tabla_hash = TablaHashCerrada(28)

# Agregar cátedras
tabla_hash.agregar_catedra("101", "Matemáticas I", "Anual", 120)
tabla_hash.agregar_catedra("102", "Física I", "Cuatrimestral", 90)
tabla_hash.agregar_catedra("103", "Programación I", "Cuatrimestral", 100)

# Agregar docentes a las cátedras
tabla_hash.agregar_docente("101", "Dr. Perez")
tabla_hash.agregar_docente("102", "Ing. Garcia")
tabla_hash.agregar_docente("103", "Lic. Martinez")
tabla_hash.agregar_docente("103", "Ing. Rodriguez")

# Obtener y mostrar los datos de una cátedra
catedra = tabla_hash.obtener_catedra("101")
print("Código 101:", catedra.nombre, catedra.modalidad, catedra.horas, catedra.docentes)

catedra = tabla_hash.obtener_catedra("103")
print("Código 103:", catedra.nombre, catedra.modalidad, catedra.horas, catedra.docentes)

# Borrar una cátedra
tabla_hash.borrar_catedra("102")
catedra = tabla_hash.obtener_catedra("102")
print("Código 102 después de borrar:", catedra)  # Debería imprimir None
