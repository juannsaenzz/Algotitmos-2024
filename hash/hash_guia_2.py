
#! EJERCICIO 2

#! Desarrollar un algoritmo que implemente una tabla hash para una guía de teléfono, los datos
#! que se conocen son número de teléfono, apellido, nombre y dirección de la persona. El campo
#! clave debe ser el número de teléfono.

class Nodo:
    def __init__(self, key, apellido, nombre, direccion):
        self.key = key
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion
        self.next = None

class BSTNode:
    def __init__(self, key, apellido, nombre, direccion):
        self.key = key
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion
        self.left = None
        self.right = None

class TablaHashMejorada:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return int(key) % self.size

    def agregar(self, key, apellido, nombre, direccion):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = BSTNode(key, apellido, nombre, direccion)
        else:
            self.table[index] = self._insertar_bst(self.table[index], key, apellido, nombre, direccion)

    def _insertar_bst(self, root, key, apellido, nombre, direccion):
        if root is None:
            return BSTNode(key, apellido, nombre, direccion)
        if key < root.key:
            root.left = self._insertar_bst(root.left, key, apellido, nombre, direccion)
        elif key > root.key:
            root.right = self._insertar_bst(root.right, key, apellido, nombre, direccion)
        else:
            root.apellido = apellido  # Actualizar datos si la clave ya existe
            root.nombre = nombre
            root.direccion = direccion
        return root

    def obtener(self, key):
        index = self.hash_function(key)
        return self._buscar_bst(self.table[index], key)

    def _buscar_bst(self, root, key):
        if root is None or root.key == key:
            return (root.apellido, root.nombre, root.direccion) if root else None
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
            root.key, root.apellido, root.nombre, root.direccion = temp.key, temp.apellido, temp.nombre, temp.direccion
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

# Agregar contactos a la guía telefónica
tabla_hash.agregar("1234567890", "Gomez", "Juan", "Calle 123")
tabla_hash.agregar("0987654321", "Perez", "Ana", "Avenida 456")
tabla_hash.agregar("5555555555", "Lopez", "Carlos", "Boulevard 789")

# Obtener y mostrar los datos de un contacto
print("1234567890:", tabla_hash.obtener("1234567890"))  # Debería imprimir ('Gomez', 'Juan', 'Calle 123')
print("0987654321:", tabla_hash.obtener("0987654321"))  # Debería imprimir ('Perez', 'Ana', 'Avenida 456')
print("5555555555:", tabla_hash.obtener("5555555555"))  # Debería imprimir ('Lopez', 'Carlos', 'Boulevard 789')
print("1111111111:", tabla_hash.obtener("1111111111"))  # Debería imprimir None

# Borrar un contacto de la guía telefónica
tabla_hash.borrar("5555555555")
print("5555555555 después de borrar:", tabla_hash.obtener("5555555555"))  # Debería imprimir None

