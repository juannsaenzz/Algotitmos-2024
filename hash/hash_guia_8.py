
#! EJERCICIO 8

#! La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene
#! todas la comunicaciones, por lo que la princesa Leia nos encarga el desarrollo de un algoritmo
#! de encriptación para las comunicaciones rebeldes, que contemple los siguientes requerimientos:

#! a. cada carácter deberá ser encriptado a ocho caracteres;
#! b. se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde
#! el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.

import random
import string

# Inicializar las tablas hash
encryption_table = {}
decryption_table = {}

# Rango de caracteres a encriptar (del 32 al 125 en ASCII)
start_char = 32
end_char = 125

# Generar claves únicas de ocho caracteres
def generate_unique_key(existing_keys):
    while True:
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        if key not in existing_keys:
            return key

# Crear las tablas hash de encriptación y desencriptación
for ascii_code in range(start_char, end_char + 1):
    char = chr(ascii_code)
    encrypted_key = generate_unique_key(encryption_table.values())
    encryption_table[char] = encrypted_key
    decryption_table[encrypted_key] = char

# Mostrar las tablas para verificar
print("Tabla de Encriptación:")
print(encryption_table)
print("\nTabla de Desencriptación:")
print(decryption_table)

# Función para encriptar un mensaje
def encrypt_message(message, encryption_table):
    encrypted_message = ''
    for char in message:
        if char in encryption_table:
            encrypted_message += encryption_table[char]
        else:
            raise ValueError(f"Carácter {char} fuera del rango soportado para encriptación.")
    return encrypted_message

# Función para desencriptar un mensaje
def decrypt_message(encrypted_message, decryption_table):
    decrypted_message = ''
    if len(encrypted_message) % 8 != 0:
        raise ValueError("El mensaje encriptado no tiene una longitud válida.")
    
    for i in range(0, len(encrypted_message), 8):
        encrypted_key = encrypted_message[i:i+8]
        if encrypted_key in decryption_table:
            decrypted_message += decryption_table[encrypted_key]
        else:
            raise ValueError(f"Clave encriptada {encrypted_key} no encontrada en la tabla de desencriptación.")
    return decrypted_message

# Ejemplo de uso
message = "Hola, Rebelde!"
print("\nMensaje Original:")
print(message)

# Encriptar el mensaje
encrypted_message = encrypt_message(message, encryption_table)
print("\nMensaje Encriptado:")
print(encrypted_message)

# Desencriptar el mensaje
decrypted_message = decrypt_message(encrypted_message, decryption_table)
print("\nMensaje Desencriptado:")
print(decrypted_message)
