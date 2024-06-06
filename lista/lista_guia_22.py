
#! EJERCICIO 22

#! Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
#! colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
#! actividades enumeradas a continuación:

#! a. listado ordenado por nombre y por especie;
#! b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
#! c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
#! d. mostrar los Jedi de especie humana y twi'lek;
#! e. listar todos los Jedi que comienzan con A;
#! f. mostrar los Jedi que usaron sable de luz de más de un color;
#! g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
#! h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

# Lista de todos los Jedi
jedi_list = [
    {'nombre': 'Ahsoka Tano', 'maestros': ['Anakin Skywalker'], 'sables': ['Verde', 'Azul'], 'especie': 'Togruta'},
    {'nombre': 'Kit Fisto', 'maestros': ['Yoda'], 'sables': ['Verde'], 'especie': 'Nautolano'},
    {'nombre': 'Yoda', 'maestros': [], 'sables': ['Verde'], 'especie': 'Desconocida'},
    {'nombre': 'Luke Skywalker', 'maestros': ['Obi-Wan Kenobi', 'Yoda'], 'sables': ['Verde', 'Azul'], 'especie': 'Humano'},
    {'nombre': 'Anakin Skywalker', 'maestros': ['Obi-Wan Kenobi'], 'sables': ['Azul'], 'especie': 'Humano'},
    {'nombre': 'Qui-Gon Jin', 'maestros': ['Count Dooku'], 'sables': ['Verde'], 'especie': 'Humano'},
    {'nombre': 'Mace Windu', 'maestros': ['Yoda'], 'sables': ['Violeta'], 'especie': 'Humano'},
    {'nombre': 'Aayla Secura', 'maestros': ['Quinlan Vos'], 'sables': ['Azul'], 'especie': "Twi'lek"},
    # Agrega más Jedi según sea necesario
]

# Funciones para resolver los problemas

def ordenar_jedi_por_nombre(lista):
    return sorted(lista, key=lambda jedi: jedi['nombre'])

def ordenar_jedi_por_especie(lista):
    return sorted(lista, key=lambda jedi: jedi['especie'])

def buscar_jedi_por_nombre(lista, nombres):
    return [jedi for jedi in lista if jedi['nombre'] in nombres]

def buscar_padawans(lista, maestros):
    padawans = []
    for jedi in lista:
        if any(maestro in jedi['maestros'] for maestro in maestros):
            padawans.append(jedi)
    return padawans

def buscar_jedi_por_especie(lista, especies):
    return [jedi for jedi in lista if jedi['especie'] in especies]

def listar_jedi_por_inicial(lista, inicial):
    return [jedi for jedi in lista if jedi['nombre'].startswith(inicial)]

def buscar_jedi_con_sables_multiples(lista):
    return [jedi for jedi in lista if len(jedi['sables']) > 1]

def buscar_jedi_con_sables_colores(lista, colores):
    return [jedi for jedi in lista if any(color in jedi['sables'] for color in colores)]

# a. Listado ordenado por nombre y por especie
jedi_ordenados_nombre = ordenar_jedi_por_nombre(jedi_list)
jedi_ordenados_especie = ordenar_jedi_por_especie(jedi_list)
print("Listado de Jedi ordenado por nombre:")
for jedi in jedi_ordenados_nombre:
    print(jedi)

print("\nListado de Jedi ordenado por especie:")
for jedi in jedi_ordenados_especie:
    print(jedi)

# b. Mostrar toda la información de Ahsoka Tano y Kit Fisto
jedi_info = buscar_jedi_por_nombre(jedi_list, ['Ahsoka Tano', 'Kit Fisto'])
print("\nInformación de Ahsoka Tano y Kit Fisto:")
for jedi in jedi_info:
    print(jedi)

# c. Mostrar todos los padawan de Yoda y Luke Skywalker
padawans_yoda_luke = buscar_padawans(jedi_list, ['Yoda', 'Luke Skywalker'])
print("\nPadawans de Yoda y Luke Skywalker:")
for jedi in padawans_yoda_luke:
    print(jedi)

# d. Mostrar los Jedi de especie humana y twi'lek
jedi_humanos_twilek = buscar_jedi_por_especie(jedi_list, ['Humano', "Twi'lek"])
print("\nJedi de especie humana y twi'lek:")
for jedi in jedi_humanos_twilek:
    print(jedi)

# e. Listar todos los Jedi que comienzan con A
jedi_con_a = listar_jedi_por_inicial(jedi_list, 'A')
print("\nJedi que comienzan con A:")
for jedi in jedi_con_a:
    print(jedi)

# f. Mostrar los Jedi que usaron sable de luz de más de un color
jedi_sables_multiples = buscar_jedi_con_sables_multiples(jedi_list)
print("\nJedi que usaron sable de luz de más de un color:")
for jedi in jedi_sables_multiples:
    print(jedi)

# g. Indicar los Jedi que utilizaron sable de luz amarillo o violeta
jedi_sables_amarillo_violeta = buscar_jedi_con_sables_colores(jedi_list, ['Amarillo', 'Violeta'])
print("\nJedi que utilizaron sable de luz amarillo o violeta:")
for jedi in jedi_sables_amarillo_violeta:
    print(jedi)

# h. Indicar los nombres de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron
padawans_quigon_mace = buscar_padawans(jedi_list, ['Qui-Gon Jin', 'Mace Windu'])
print("\nPadawans de Qui-Gon Jin y Mace Windu:")
for jedi in padawans_quigon_mace:
    print(jedi['nombre'])
