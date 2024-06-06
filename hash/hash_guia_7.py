
#! EJERCICIO 7

#! Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
#! que contemple las siguientes actividades:

#! a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
#! tabla la función hash deberá utilizar el número del Pokémon como clave, mientras que en
#! la tercera el campo clave de la función hash será por el nombre del Pokémon.
#! b. el tamaño de la primera tabla debe ser lo suficientemente grande como para que pueda
#! almacenar todos los distintos tipos de Pokémon, debe manejar las colisiones con alguna
#! función de sondeo;
#! c. el tamaño de cada una de las segundas tablas debe ser 15;
#! d. el algoritmo debe permitir cargar tipos de Pokémon en la primera tabla y crear su respec-
#! tiva segunda tabla, –en el caso de que no exista–;
#! e. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen
#! estos tipos;
#! f. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo, nivel.

class Pokemon:
    def __init__(self, numero, nombre, tipo, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
    
    def __repr__(self):
        return f'Pokemon({self.numero}, {self.nombre}, {self.tipo}, {self.nivel})'

def hash_tipo(tipo, table_size):
    return sum(ord(c) for c in tipo) % table_size

def hash_numero(numero, table_size):
    return numero % table_size

def hash_nombre(nombre, table_size):
    return sum(ord(c) for c in nombre) % table_size

def linear_probe(hash_value, step, table_size):
    return (hash_value + step) % table_size

class TablaHash:
    def __init__(self, table_size, hash_function):
        self.table_size = table_size
        self.table = [None] * table_size
        self.hash_function = hash_function
        self.element_count = 0
    
    def insertar(self, key, value):
        hash_value = self.hash_function(key, self.table_size)
        step = 0
        while self.table[linear_probe(hash_value, step, self.table_size)] is not None:
            step += 1
        self.table[linear_probe(hash_value, step, self.table_size)] = (key, value)
        self.element_count += 1
    
    def buscar(self, key):
        hash_value = self.hash_function(key, self.table_size)
        step = 0
        while self.table[linear_probe(hash_value, step, self.table_size)] is not None:
            if self.table[linear_probe(hash_value, step, self.table_size)][0] == key:
                return self.table[linear_probe(hash_value, step, self.table_size)][1]
            step += 1
        return None

class Pokedex:
    def __init__(self):
        self.tipos = TablaHash(20, hash_tipo)  # Tamaño suficientemente grande para los tipos
        self.numeros = TablaHash(15, hash_numero)
        self.nombres = TablaHash(15, hash_nombre)
    
    def insertar_pokemon(self, pokemon):
        for tipo in pokemon.tipo:
            tabla_tipo = self.tipos.buscar(tipo)
            if tabla_tipo is None:
                tabla_tipo = TablaHash(15, hash_numero)
                self.tipos.insertar(tipo, tabla_tipo)
            tabla_tipo.insertar(pokemon.numero, pokemon)
        
        self.numeros.insertar(pokemon.numero, pokemon)
        self.nombres.insertar(pokemon.nombre, pokemon)
    
    def buscar_por_tipo(self, tipo):
        return self.tipos.buscar(tipo)
    
    def buscar_por_numero(self, numero):
        return self.numeros.buscar(numero)
    
    def buscar_por_nombre(self, nombre):
        return self.nombres.buscar(nombre)

# Crear la pokedex
pokedex = Pokedex()

# Insertar Pokémon
pokedex.insertar_pokemon(Pokemon(1, "Bulbasaur", ["Planta", "Veneno"], 5))
pokedex.insertar_pokemon(Pokemon(4, "Charmander", ["Fuego"], 5))
pokedex.insertar_pokemon(Pokemon(7, "Squirtle", ["Agua"], 5))

# Buscar Pokémon por tipo
print(pokedex.buscar_por_tipo("Planta"))  # Debe imprimir la tabla hash con Bulbasaur
print(pokedex.buscar_por_tipo("Fuego"))   # Debe imprimir la tabla hash con Charmander
print(pokedex.buscar_por_tipo("Agua"))    # Debe imprimir la tabla hash con Squirtle

# Buscar Pokémon por número
print(pokedex.buscar_por_numero(1))  # Debe imprimir el Pokémon Bulbasaur
print(pokedex.buscar_por_numero(4))  # Debe imprimir el Pokémon Charmander
print(pokedex.buscar_por_numero(7))  # Debe imprimir el Pokémon Squirtle

# Buscar Pokémon por nombre
print(pokedex.buscar_por_nombre("Bulbasaur"))  # Debe imprimir el Pokémon Bulbasaur
print(pokedex.buscar_por_nombre("Charmander"))  # Debe imprimir el Pokémon Charmander
print(pokedex.buscar_por_nombre("Squirtle"))  # Debe imprimir el Pokémon Squirtle
