
#! EJERCICIO 18

#! Se tienen los usuarios colaboradores de un repositorio de GitHub y de cada uno de estos se tie-
#! ne una lista de los commit realizados, de los cuales se cuenta con su timestamp (en formato fecha
#! y hora), mensaje de commit, nombre de archivo modificado, cantidad de líneas agregadas/elimi-
#! nadas (puede ser positivo o negativo) –suponga que solo puede modificar un archivo en cada
#! commit que se haga–. Desarrollar un algoritmo que permita realizar las siguientes actividades:

#! a. obtener el usuario con mayor cantidad de commits –podría llegar a ser más de uno–;
#! b. obtener el usuario que haya agregado en total mayor cantidad de líneas y el que haya eli-
#! minado menor cantidad de líneas;
#! c. mostrar los usuarios que realizaron cambios sobre el archivo test.py después de las 19:45 sin
#! importar la fecha;
#! d. indicar los usuarios que hayan realizado al menos un commit con cero líneas agregados
#! o eliminadas;
#! e. determinar el nombre del usuario que realizó el último commit sobre el archivo app.py in-
#! dicando toda la información de dicho commit;
#! f. deberá utilizar el TDA lista de lista.

from datetime import datetime

# Estructura de datos: lista de lista
# Cada usuario es una lista [nombre, [lista de commits]]
usuarios = [
    ["Usuario1", [
        [datetime(2024, 6, 1, 10, 30), "Mensaje1", "archivo1.py", 10],
        [datetime(2024, 6, 2, 11, 45), "Mensaje2", "archivo2.py", -5],
        [datetime(2024, 6, 3, 9, 15), "Mensaje3", "archivo1.py", 8],
    ]],
    ["Usuario2", [
        [datetime(2024, 6, 1, 12, 0), "Mensaje4", "archivo3.py", 8],
        [datetime(2024, 6, 2, 13, 20), "Mensaje5", "archivo1.py", 3],
    ]],
    ["Usuario3", [
        [datetime(2024, 6, 1, 15, 45), "Mensaje6", "archivo2.py", -2],
        [datetime(2024, 6, 3, 20, 0), "Mensaje7", "archivo1.py", 5],
    ]],
]

def obtener_usuario_mas_commits(usuarios):
    max_commits = max(len(usuario[1]) for usuario in usuarios)
    return [usuario[0] for usuario in usuarios if len(usuario[1]) == max_commits]

def obtener_usuario_mas_lineas_agregadas(usuarios):
    max_lineas_agregadas = max(sum(commit[3] for commit in usuario[1]) for usuario in usuarios)
    return [usuario[0] for usuario in usuarios if sum(commit[3] for commit in usuario[1]) == max_lineas_agregadas]

def obtener_usuario_menos_lineas_eliminadas(usuarios):
    min_lineas_eliminadas = min(sum(commit[3] for commit in usuario[1]) for usuario in usuarios)
    return [usuario[0] for usuario in usuarios if sum(commit[3] for commit in usuario[1]) == min_lineas_eliminadas]

def obtener_usuarios_cambios_despues_de(usuarios, archivo, hora):
    cambios_despues_de = []
    for usuario in usuarios:
        for commit in usuario[1]:
            if commit[2] == archivo and commit[0].time() > hora:
                cambios_despues_de.append(usuario[0])
                break
    return cambios_despues_de

def obtener_usuarios_con_cero_cambios(usuarios):
    usuarios_con_cero_cambios = []
    for usuario in usuarios:
        for commit in usuario[1]:
            if commit[3] == 0:
                usuarios_con_cero_cambios.append(usuario[0])
                break
    return usuarios_con_cero_cambios

def obtener_ultimo_commit_usuario_sobre(usuarios, archivo):
    ultimo_commit = None
    for usuario in usuarios:
        for commit in usuario[1]:
            if commit[2] == archivo:
                if ultimo_commit is None or commit[0] > ultimo_commit[1][0]:
                    ultimo_commit = [usuario[0]] + commit
    return ultimo_commit

# Ejemplos de uso
print("Usuario(s) con mayor cantidad de commits:", obtener_usuario_mas_commits(usuarios))
print("Usuario que agregó más líneas y el que eliminó menos líneas:", obtener_usuario_mas_lineas_agregadas(usuarios), obtener_usuario_menos_lineas_eliminadas(usuarios))
print("Usuarios que realizaron cambios sobre test.py después de las 19:45:", obtener_usuarios_cambios_despues_de(usuarios, "test.py", datetime.strptime("19:45", "%H:%M").time()))
print("Usuarios que realizaron al menos un commit con cero líneas agregadas o eliminadas:", obtener_usuarios_con_cero_cambios(usuarios))
print("Último commit sobre app.py:", obtener_ultimo_commit_usuario_sobre(usuarios, "app.py"))
