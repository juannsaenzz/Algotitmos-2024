
#! EJERCICIO 4

#! Desarrollar un algoritmo que implemente una tabla hash para cargar personajes de Star Wars
#! de los que solo se conoce su nombre, contemplando las siguientes actividades:

#! a. la tabla inicialmente será de 20 posiciones;
#! b. deberá permitir el manejo de colisiones;
#! c. cuando el factor de carga de la tabla exceda el 75%, se deberá incrementar el tamaño de la
#! tabla al doble y hacer un rehashing de las claves cargadas.

class HashTable:
    def __init__(self, initial_capacity=20):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(initial_capacity)]
        
    def bernstein_hash(self, key):
        h = 0
        for char in key:
            h = h * 33 + ord(char)
        return h % self.capacity

    def rehash(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_buckets:
            for key in bucket:
                self.insert(key)

    def insert(self, key):
        index = self.bernstein_hash(key)
        bucket = self.buckets[index]
        
        if key not in bucket:
            bucket.append(key)
            self.size += 1
        
        if self.size / self.capacity > 0.75:
            self.rehash()

    def search(self, key):
        index = self.bernstein_hash(key)
        bucket = self.buckets[index]
        return key in bucket

    def delete(self, key):
        index = self.bernstein_hash(key)
        bucket = self.buckets[index]
        
        if key in bucket:
            bucket.remove(key)
            self.size -= 1

    def display(self):
        for index, bucket in enumerate(self.buckets):
            if bucket:
                print(f"Bucket {index}: {bucket}")

# Ejemplo de uso
if __name__ == "__main__":
    star_wars_characters = [
        "Luke Skywalker", "Darth Vader", "Leia Organa", "Han Solo", "Yoda",
        "Obi-Wan Kenobi", "Anakin Skywalker", "Chewbacca", "R2-D2", "C-3PO",
        "Palpatine", "Lando Calrissian", "Boba Fett", "Rey", "Kylo Ren",
        "Finn", "Poe Dameron", "Padmé Amidala", "Mace Windu", "Qui-Gon Jinn"
    ]
    
    hash_table = HashTable()

    for character in star_wars_characters:
        hash_table.insert(character)

    hash_table.display()
    print("Factor de carga:", hash_table.size / hash_table.capacity)

    # Búsqueda de personajes
    print("¿Está Luke Skywalker?", hash_table.search("Luke Skywalker"))
    print("¿Está Darth Vader?", hash_table.search("Darth Vader"))

    # Eliminación de un personaje
    hash_table.delete("Darth Vader")
    print("¿Está Darth Vader después de eliminar?", hash_table.search("Darth Vader"))
