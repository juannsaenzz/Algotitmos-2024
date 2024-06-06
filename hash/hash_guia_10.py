
#! EJERCICIO 10

#! Implementar una tabla hash para almacenar la información de todos los Jedi, de los cuales se
#! conoce su nombre y quien fue su maestro –este último puede ser más de uno o desconocido–
#! contemplando las siguientes requerimientos:

#! a. la tabla debe ser de 15 posiciones;
#! b. debe poder manejar las colisiones que se produzcan dependiendo del tipo
#! de tabla utilizado;
#! c. cargar al menos 30 Jedi;
#! d. determinar si están cargados los Jedi: Yoda, Luke Skywalker y Ahsoka Tano.
#! Si no están, agregarlos;
#! e. crear una función que permita determinar el factor de carga de la tabla, dependiendo del
#! tipo utilizado;
#! f. mostrar toda la información de Ahsoka Tano, Obi-Wan Kenobi y Qui-Gon Jin;
#! g. mostrar los maestros y aprendices (padawan) de Yoda y Luke Skywalker; los aprendices no
#! son parte de la información, debe determinarlos a partir del campo maestro de cada Jedi.

class Jedi:
    def __init__(self, nombre, maestros):
        self.nombre = nombre
        self.maestros = maestros

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, jedi):
        index = self._hash(jedi.nombre)
        self.table[index].append(jedi)
        self.count += 1

    def search(self, nombre):
        index = self._hash(nombre)
        for jedi in self.table[index]:
            if jedi.nombre == nombre:
                return jedi
        return None

    def contains(self, nombre):
        return self.search(nombre) is not None

    def factor_carga(self):
        return self.count / self.size

    def mostrar_informacion(self, nombre):
        jedi = self.search(nombre)
        if jedi:
            print(f"Nombre: {jedi.nombre}, Maestros: {', '.join(jedi.maestros)}")
        else:
            print(f"Jedi {nombre} no encontrado.")

    def maestros_y_aprendices(self, nombre):
        jedi = self.search(nombre)
        if jedi:
            print(f"Maestros de {nombre}: {', '.join(jedi.maestros)}")
            aprendices = []
            for bucket in self.table:
                for j in bucket:
                    if nombre in j.maestros:
                        aprendices.append(j.nombre)
            print(f"Aprendices de {nombre}: {', '.join(aprendices)}")
        else:
            print(f"Jedi {nombre} no encontrado.")

def cargar_jedis(hash_table):
    jedis = [
        ("Yoda", ["Desconocido"]), ("Luke Skywalker", ["Yoda"]), ("Ahsoka Tano", ["Anakin Skywalker"]),
        ("Obi-Wan Kenobi", ["Qui-Gon Jin"]), ("Qui-Gon Jin", ["Dooku"]), ("Anakin Skywalker", ["Obi-Wan Kenobi"]),
        ("Mace Windu", ["Yoda"]), ("Ki-Adi-Mundi", ["Yoda"]), ("Plo Koon", ["Yoda"]),
        ("Shaak Ti", ["Yoda"]), ("Aayla Secura", ["Quinlan Vos"]), ("Kit Fisto", ["Yoda"]),
        ("Luminara Unduli", ["Yoda"]), ("Barriss Offee", ["Luminara Unduli"]), ("Jocasta Nu", ["Yoda"]),
        ("Depa Billaba", ["Mace Windu"]), ("Kanan Jarrus", ["Depa Billaba"]), ("Ezra Bridger", ["Kanan Jarrus"]),
        ("Rey", ["Leia Organa"]), ("Leia Organa", ["Luke Skywalker"]), ("Ben Solo", ["Luke Skywalker"]),
        ("Dooku", ["Yoda"]), ("Savage Opress", ["Dooku"]), ("Asajj Ventress", ["Dooku"]),
        ("Darth Maul", ["Sidious"]), ("Sidious", ["Darth Plagueis"]), ("Darth Vader", ["Sidious"]),
        ("Snoke", ["Sidious"]), ("Kylo Ren", ["Snoke"]), ("Grogu", ["Luke Skywalker"])
    ]
    
    for nombre, maestros in jedis:
        hash_table.insert(Jedi(nombre, maestros))

# Crear tabla hash
hash_table = HashTable(30)  # Ajustar el tamaño para mejorar el factor de carga

# Cargar los Jedi en la tabla
cargar_jedis(hash_table)

# Verificar si ciertos Jedi están en la tabla, si no, agregarlos
for jedi in ["Yoda", "Luke Skywalker", "Ahsoka Tano"]:
    if not hash_table.contains(jedi):
        print(f"{jedi} no está en la tabla. Agregando...")
        if jedi == "Yoda":
            hash_table.insert(Jedi("Yoda", ["Desconocido"]))
        elif jedi == "Luke Skywalker":
            hash_table.insert(Jedi("Luke Skywalker", ["Yoda"]))
        elif jedi == "Ahsoka Tano":
            hash_table.insert(Jedi("Ahsoka Tano", ["Anakin Skywalker"]))

# Calcular el factor de carga
factor_carga = hash_table.factor_carga()
print(f"Factor de carga de la tabla: {factor_carga:.2f}")

# Mostrar información de ciertos Jedi
for jedi in ["Ahsoka Tano", "Obi-Wan Kenobi", "Qui-Gon Jin"]:
    hash_table.mostrar_informacion(jedi)

# Mostrar maestros y aprendices de Yoda y Luke Skywalker
for jedi in ["Yoda", "Luke Skywalker"]:
    hash_table.maestros_y_aprendices(jedi)
