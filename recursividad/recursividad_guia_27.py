
#! EJERCICIO 27

#! El valor 1 376 256 pertenece a una sucesión geométrica cuya razón es 4, implementar un algorit-
#! mo para mostrar todos los valores de la sucesión hacia atrás hasta el valor de a1= 5,25.

def imprimir_sucesion_geometrica(valor, razon, a1):
    if valor < a1:
        return
    print(valor)
    imprimir_sucesion_geometrica(valor / razon, razon, a1)

# Ejemplo de uso:
valor_inicial = 1376256  # Término dado de la sucesión geométrica
razon = 4  # Razón de la sucesión geométrica
a1 = 5.25  # Primer término de la sucesión geométrica

imprimir_sucesion_geometrica(valor_inicial, razon, a1)
