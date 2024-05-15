
#! EJERCICIO 9

#! Se tiene una lista de los alumnos de un curso, de los que se sabe nombre,
#! apellido y legajo. Por otro lado se tienen las notas de los diferentes parciales
#! que rindió cada uno de ellos con la siguiente información: materia que rindió,
#! nota obtenida y fecha de parcial. Desarrollar un algoritmo que permita realizar
#! la siguientes actividades:
#! a. mostrar los alumnos ordenados alfabéticamente por apellido;
#! b. indicar los alumnos que no desaprobaron ningún parcial;
#! c. determinar los alumnos que tienen promedio mayor a 8,89;
#! d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
#! e. mostrar el promedio de cada uno de los alumnos;
#! f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de
#! datos”;
#! g. indicar el porcentaje de parciales aprobados de un alumno indicado por el
#! usuario;
#! h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra
#! “Base de datos”;
#! i. mostrar todos los alumnos que rindieron en el año 2020;

from lista import by_surname

def show_alumnos(alumnos):
    for alumno in alumnos:
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellido: {alumno['apellido']}")
        print(f"Legajo: {alumno['legajo']}")
        print()

def show_info(alumno):
    print(f"Nombre: {alumno['nombre']}")
    print(f"Apellido: {alumno['apellido']}")
    print(f"Legajo: {alumno['legajo']}")
    print()
    print('Notas:')
    for nota in alumno['notas']:
        print(f"Materia: {nota['materia']}")
        print(f"Nota: {nota['nota']}")
        print(f"Fecha: {nota['fecha']}")
        print()

def promedio(notas):
    if len(notas) == 0:
        return 0
    suma_notas = sum(notas)
    return suma_notas / len(notas)

def porcentaje(cant_parciales, parciales_aprobados):
    return (parciales_aprobados * 100) / cant_parciales

def buscador(alumno_buscado, alumnos):
    alumno_encontrado = None
    for alumno in alumnos:
        if alumno['apellido'] + " " + alumno['nombre'] == alumno_buscado:
            alumno_encontrado = alumno
    return alumno_encontrado

alumnos = [
    {
        'nombre': 'Juan',
        'apellido': 'Saenz',
        'legajo': 'S305832',
        'notas': [
            {
                'materia': 'Algoritmos y Estructuras de Datos',
                'nota': 8,
                'fecha': '12/05/2024',
            },
            {
                'materia': 'Programacion Orientada a Objetos',
                'nota': 7,
                'fecha': '30/08/2023'
            }
        ]
    },
    {
        'nombre': 'Adrian',
        'apellido': 'Perez',
        'legajo': 'P084813',
        'notas': [
            {
                'materia': 'Algoritmos y Estructuras de Datos',
                'nota': 9,
                'fecha': '03/10/2019',
            },
            {
                'materia': 'Base de Datos',
                'nota': 9.50,
                'fecha': '19/06/2020',
            }
        ]
    },
    {
        'nombre': 'Candela',
        'apellido': 'Saenz',
        'legajo': 'S152666',
        'notas': [
            {
                'materia': 'Algoritmos y Estructuras de Datos',
                'nota': 5,
                'fecha': '23/09/2020',
            },
            {
                'materia': 'Base de Datos',
                'nota': 8,
                'fecha': '29/04/2021',
            }
        ]
    },
    {
        'nombre': 'Florencia',
        'apellido': 'Vargas',
        'legajo': 'V284854',
        'notas': [
            {
                'materia': 'Matematica Discreta',
                'nota': 3,
                'fecha': '01/11/2022',
            },
            {
                'materia': 'Calculo',
                'nota': 6,
                'fecha': '29/03/2020',
            }
        ]
    },
    {
        'nombre': 'Pedro',
        'apellido': 'Artusi',
        'legajo': 'A34592O',
        'notas': [
            {
                'materia': 'Base de Datos',
                'nota': 9.20,
                'fecha': '08/08/2020',
            },
            {
                'materia': 'Calculo',
                'nota': 9,
                'fecha': '31/05/2022',
            }
        ]
    },
    {
        'nombre': 'Ana',
        'apellido': 'Monti',
        'legajo': 'M566743',
        'notas': [
            {
                'materia': 'Algoritmos y Estructuras de Datos',
                'nota': 7,
                'fecha': '15/05/2021',
            },
            {
                'materia': 'Base de Datos',
                'nota': 5,
                'fecha': '19/10/2020',
            }
        ]
    },
    {
        'nombre': 'Martin',
        'apellido': 'Lazalde',
        'legajo': 'L827341',
        'notas': [
            {
                'materia': 'Algoritmos y Estructuras de Datos',
                'nota': 8,
                'fecha': '15/02/2022',
            },
            {
                'materia': 'Base de Datos',
                'nota': 9.80,
                'fecha': '27/03/2020',
            }
        ]
    }
]

#! A
print('Lista de alumnos ordenados alfabeticamente: ')
alumnos.sort(key=by_surname)
show_alumnos(alumnos)

#! B
print()
print('Alumnos que no desaprobaron ningun parcial:')
nota_minima = 6
for alumno in alumnos:
    desaprobado = False
    for nota in alumno['notas']:
        if nota['nota'] < nota_minima:
            desaprobado = True
            break
    if not desaprobado:
        print(alumno['apellido'], alumno['nombre'])

#! C
print()
print('Alumnos que tienen promedio mayor a 8.89:')
prom = 8.89
for alumno in alumnos:
    notas_alumno = [nota['nota'] for nota in alumno['notas']]
    promedio_alumno = promedio(notas_alumno)
    if promedio_alumno > prom:
        print(alumno['apellido'] + ' ' + alumno['nombre'])

#! D
print()
print('Toda la informacion de los alumnos cuyos apellidos comienzan con "L":')
for alumno in alumnos:
    if alumno['apellido'][0] == 'L':
        show_info(alumno)

#! E
print()
print('Promedio de cada uno de los alumnos:')
for alumno in alumnos:
    print(f"Promedio de {alumno['apellido']} {alumno['nombre']}: {promedio([nota['nota'] for nota in alumno['notas']])}")

#! F
print()
print('Alumnos que rindieron Algoritmos y Estructuras de Datos:')
materia = 'Algoritmos y Estructuras de Datos'
for alumno in alumnos:
    for nota in alumno['notas']:
        if nota['materia'] == materia:
            print(alumno['apellido'] + ' ' + alumno['nombre'])
            break

#! G
print()
alumno_buscado = input('Ingrese un alumno para buscar (Apellido Nombre): ')
alumno_encontrado = buscador(alumno_buscado, alumnos)
if alumno_encontrado is not None:
    parciales_aprobados = 0
    for nota in alumno_encontrado['notas']:
        if nota['nota'] >= nota_minima:
            parciales_aprobados += 1
    cant_parciales = len(alumno_encontrado['notas'])
    print(f"Porcentaje de parciales aprobados por {alumno_encontrado['apellido']} {alumno_encontrado['nombre']}:")
    print(f'{porcentaje(cant_parciales, parciales_aprobados)}%')
else:
    print('ALUMNO NO ENCONTRADO')

#! H
print()
aprobados_bd = 0
desaprobados_bd = 0
materia2 = 'Base de Datos'
for alumno in alumnos:
    for nota in alumno['notas']:
        if nota['materia'] == materia2:
            if nota['nota'] >= nota_minima:
                aprobados_bd += 1
            else:
                desaprobados_bd += 1

print(f'Cantidad de alumnos aprobados en Base de Datos: {aprobados_bd}')
print(f'Cantidad de alumnos desaprobados en Base de Datos: {desaprobados_bd}')

#! I
print()
print('Alumnos que rindieron en el año 2020:')
año = '2020'
for alumno in alumnos:
    for nota in alumno['notas']:
        if año in nota['fecha']:
            print(alumno['apellido'] + ' ' + alumno['nombre'])
            break