
#! EJERCICIO 9

#! Desarrollar un algoritmo que permita cifrar y descifrar un mensaje carácter a carácter, contem-
#! plando las siguientes pautas:

#! a. Se debe utilizar una tabla hash para guardar los valores de codificación y decodificación
#! respectivamente que se vayan utilizando.
#! b. Se deberá cifrar de la siguiente manera: primero, convertir al valor numérico correspondien-
#! te de la tabla ASCII cada carácter y luego, cada número de dicho valor se deberá rempla-
#! zar por su valor correspondiente según los siguientes valores: 1 – “abd”, 2 – “def”, 3 – “ghi”,
#! 4 –“ jkl”, 5 –“mnñ”, 6 – “opq”, 7 – “rst”, 8 – “uvw”, 9 – “xyz”, 0 – “#?&”, y se debe agregar al final
#! el carácter %. Por ejemplo D = 68 debería quedar de la siguiente manera “opquvw%”.

# Tabla de codificación y decodificación
encoding_table = {
    '1': 'abd', '2': 'def', '3': 'ghi', '4': 'jkl', '5': 'mnñ',
    '6': 'opq', '7': 'rst', '8': 'uvw', '9': 'xyz', '0': '#?&'
}

# Tabla inversa para decodificación
decoding_table = {v: k for k, v in encoding_table.items()}

def encrypt_character(character):
    ascii_value = ord(character)
    ascii_str = str(ascii_value)
    encrypted_str = ''
    for digit in ascii_str:
        encrypted_str += encoding_table[digit]
    encrypted_str += '%'
    return encrypted_str

def encrypt_message(message):
    encrypted_message = ''
    for char in message:
        encrypted_message += encrypt_character(char)
    return encrypted_message

def decrypt_character(encrypted_character):
    encrypted_character = encrypted_character.rstrip('%')
    ascii_str = ''
    for i in range(0, len(encrypted_character), 3):
        chunk = encrypted_character[i:i+3]
        if chunk in decoding_table:
            ascii_str += decoding_table[chunk]
        else:
            raise ValueError(f"Chunk {chunk} no encontrado en la tabla de decodificación.")
    ascii_value = int(ascii_str)
    return chr(ascii_value)

def decrypt_message(encrypted_message):
    decrypted_message = ''
    chunks = encrypted_message.split('%')[:-1]  # split and remove the last empty element
    for chunk in chunks:
        decrypted_message += decrypt_character(chunk + '%')
    return decrypted_message

# Ejemplo de uso
message = "Hola, Rebelde!"
print("Mensaje Original:")
print(message)

# Encriptar el mensaje
encrypted_message = encrypt_message(message)
print("\nMensaje Encriptado:")
print(encrypted_message)

# Desencriptar el mensaje
decrypted_message = decrypt_message(encrypted_message)
print("\nMensaje Desencriptado:")
print(decrypted_message)
