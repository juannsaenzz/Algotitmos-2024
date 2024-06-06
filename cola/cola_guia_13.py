
#! EJERCICIO 13

#! Dada una cola de 50000 caracteres generados aleatoriamente realizar las siguientes actividades:

#! a. separarla en dos colas una con dígitos y otra con el resto de los caracteres.
#! b. determinar cuántas letras hay en la segunda cola.
#! c. determinar además si existen los caracteres “?” y “#”.

from cola import Queue
import random

# Crear la cola de caracteres aleatorios
cola_caracteres = Queue()
for _ in range(50000):
    cola_caracteres.arrive(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?#"))

# a. Separar la cola en dos colas: una con dígitos y otra con el resto de los caracteres.
cola_digitos = Queue()
cola_letras = Queue()
cola_resto = Queue()

while cola_caracteres.size() > 0:
    caracter = cola_caracteres.attention()
    if caracter.isdigit():
        cola_digitos.arrive(caracter)
    elif caracter.isalpha():
        cola_letras.arrive(caracter)
    else:
        cola_resto.arrive(caracter)

# b. Determinar cuántas letras hay en la segunda cola.
cantidad_letras = cola_letras.size()

# c. Determinar además si existen los caracteres "?" y "#".
existe_signo_interrogacion = False
existe_signo_numeral = False

cola_resto_aux = Queue()

while cola_resto.size() > 0:
    caracter = cola_resto.attention()
    if caracter == "?":
        existe_signo_interrogacion = True
    elif caracter == "#":
        existe_signo_numeral = True
    cola_resto_aux.arrive(caracter)

cola_resto = cola_resto_aux

# Imprimir resultados
print("Cantidad de dígitos:", cola_digitos.size())
print("Cantidad de letras en la segunda cola:", cantidad_letras)
print("¿Existe el signo '?' en la cola de restantes?:", existe_signo_interrogacion)
print("¿Existe el signo '#' en la cola de restantes?:", existe_signo_numeral)
