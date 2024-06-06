
from random import randint, choice

def hash_legion(value):
    return value[:2]

def hash_numerica(value):
    return value[-3:]

legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

tabla_legiones = {}
table_numerica = {}

for legion in legiones:
    tabla_legiones[legion] = []

for i in range(0, 2000):
    trooper = f'{choice(legiones)}-{randint(1000, 9999)}'
    clave = hash_numerica(trooper)
    if clave not in table_numerica:
        table_numerica[clave] = []

    table_numerica[clave].append(trooper)
    tabla_legiones[hash_legion(trooper)].append(trooper)

# A FN-2187 traitor
list_187 = table_numerica.get('187', [])
if 'FN-2187' in list_187:
    pos_fn_2187 = list_187.index('FN-2187')
    if pos_fn_2187 > -1:
        print(f'Está en la posición {pos_fn_2187}')
else:
    print('No está')
print(len(list_187))
print()

# B mission_assault 781 mission_explore 537
mission_assault = table_numerica.get('781', [])
print('Stormtroopers para misión de asalto:')
for index, trooper in enumerate(mission_assault):
    print(f'{index} - {trooper}')
print()

mission_explore = table_numerica.get('537', [])
print('Stormtroopers para misión de exploración:')
for index, trooper in enumerate(mission_explore):
    print(f'{index} - {trooper}')
print()

# C hoth CT endor TF
mission_hoth = tabla_legiones.get('CT', [])
print('Stormtroopers para misión a Hoth:')
for index, trooper in enumerate(mission_hoth):
    print(f'{index} - {trooper}')
print()

mission_endor = tabla_legiones.get('TF', [])
print('Stormtroopers para misión a Endor:')
for index, trooper in enumerate(mission_endor):
    print(f'{index} - {trooper}')
print()
