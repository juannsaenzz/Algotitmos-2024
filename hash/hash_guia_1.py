
#! EJERCICIO 1

#! Desarrollar un algoritmo que permita implementar una tabla hash para representar un diccio-
#! nario que permita resolver las siguientes actividades:

#! a. agregar una palabra y su significado al diccionario;
#! b. determinar si una palabra existe y mostrar su significado;
#! c. borrar una palabra del diccionario;
#! d. la tabla debe tener 28 posiciones y manejar las colisiones con lista enlazadas;
#! e. mejorar el rendimiento de la tabla utilizando árboles binarios de búsqueda.

### Código Completo para Ejecución

# Clase Nodo para la Lista Enlazada
class Nodo:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Clase BSTNode para el Árbol Binario de Búsqueda
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# Clase TablaHash
class TablaHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def agregar(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Nodo(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value  # Actualizar el valor si la clave ya existe
                    return
                current = current.next
            if current.key == key:
                current.value = value  # Actualizar el valor si la clave ya existe
            else:
                current.next = Nodo(key, value)  # Manejar colisión

    def obtener(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def borrar(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False

# Clase TablaHashMejorada
class TablaHashMejorada(TablaHash):
    def __init__(self, size):
        super().__init__(size)
        self.table = [None] * size
    
    def agregar(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = BSTNode(key, value)
        else:
            self.table[index] = self._insertar_bst(self.table[index], key, value)

    def _insertar_bst(self, root, key, value):
        if root is None:
            return BSTNode(key, value)
        if key < root.key:
            root.left = self._insertar_bst(root.left, key, value)
        elif key > root.key:
            root.right = self._insertar_bst(root.right, key, value)
        else:
            root.value = value  # Actualizar el valor si la clave ya existe
        return root

    def obtener(self, key):
        index = self.hash_function(key)
        return self._buscar_bst(self.table[index], key)

    def _buscar_bst(self, root, key):
        if root is None or root.key == key:
            return root.value if root else None
        if key < root.key:
            return self._buscar_bst(root.left, key)
        return self._buscar_bst(root.right, key)

    def borrar(self, key):
        index = self.hash_function(key)
        self.table[index], deleted = self._borrar_bst(self.table[index], key)
        return deleted

    def _borrar_bst(self, root, key):
        if root is None:
            return root, False
        if key < root.key:
            root.left, deleted = self._borrar_bst(root.left, key)
        elif key > root.key:
            root.right, deleted = self._borrar_bst(root.right, key)
        else:
            if root.left is None:
                return root.right, True
            elif root.right is None:
                return root.left, True
            temp = self._min_value_node(root.right)
            root.key, root.value = temp.key, temp.value
            root.right, _ = self._borrar_bst(root.right, temp.key)
            return root, True
        return root, False

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Pruebas
# Crear la tabla hash con 28 posiciones
tabla_hash = TablaHashMejorada(28)

# Agregar palabras y significados
tabla_hash.agregar("hola", "saludo")
tabla_hash.agregar("adios", "despedida")
tabla_hash.agregar("amor", "sentimiento")

# Verificar si una palabra existe y mostrar su significado
print("hola:", tabla_hash.obtener("hola"))  # Debería imprimir "saludo"
print("adios:", tabla_hash.obtener("adios"))  # Debería imprimir "despedida"
print("amor:", tabla_hash.obtener("amor"))  # Debería imprimir "sentimiento"
print("odio:", tabla_hash.obtener("odio"))  # Debería imprimir None

# Borrar una palabra del diccionario
tabla_hash.borrar("amor")
print("amor después de borrar:", tabla_hash.obtener("amor"))  # Debería imprimir None
