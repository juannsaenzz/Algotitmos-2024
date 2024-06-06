
#! EJERCICIO 19

#! Los astilleros de propulsores Kuat, son la mayor corporación de construcción de naves milita-
#! res que provee al imperio galáctico –dentro de sus productos más destacados están los cazas
#! TIE, destructores estelares, transporte acorazado todo terreno (AT-AT), transporte de explo-
#! ración todo terreno (AT-ST), ejecutor táctico todo terreno (AT-TE), entre otros– y nos solicita
#! desarrollar las funciones necesarias para resolver las siguientes necesidades:

#! a. debe procesar los datos de las ventas de naves que están almacenados en un rudimenta-
#! rio archivo de texto, en el cual cada línea tiene los siguientes datos: código del astillero
#! que lo produjo, producto (los mencionados previamente), precio en créditos galácticos, si
#! fue construido con partes recicladas o no (booleano), quien realizo la compra (en algunos
#! casos se desconoce quién realizo la compra y este campo tiene valor desconocido), todos
#! estos datos están separados por “;” en cada línea del archivo;
#! b. cargar los datos procesados en el punto anterior en dos listas, en la primera las ventas de
#! las que se conocen el cliente y la segunda las que no;
#! c. el código del astillero son tres caracteres el primero en una letra mayúscula de la “A” hasta
#! la “K” seguido de dos dígitos;
#! d. obtener el total de ingresos de créditos galácticos y cuantas unidades se vendieron;
#! e. listar los nombres de todos los clientes, los repetidos deberán mostrarse una sola vez, pue-
#! de utilizar una estructura auxiliar para resolverlo;
#! f. realizar un informe de las compras realizadas por Darth Vader;
#! g. se le debe realizar un descuento del 15% a los clientes que compraron naves que fueron
#! fabricadas con partes recicladas, mostrar los clientes y los montos a devolver a cada uno;
#! h. determinar cuánto ingreso genero la producción de naves cuyos modelos contengan la
#! sigla “AT”.

# Función para procesar los datos del archivo de texto
def procesar_datos(archivo):
    ventas_conocidas = []
    ventas_desconocidas = []
    ingresos_totales = 0
    unidades_vendidas = 0
    
    with open(archivo, 'r') as file:
        for line in file:
            datos = line.strip().split(';')
            codigo_astillero = datos[0]
            producto = datos[1]
            precio = float(datos[2])
            partes_recicladas = datos[3] == 'True'
            cliente = datos[4] if len(datos) > 4 else "Desconocido"
            
            venta = {'codigo_astillero': codigo_astillero,
                     'producto': producto,
                     'precio': precio,
                     'partes_recicladas': partes_recicladas,
                     'cliente': cliente}
            
            ingresos_totales += precio
            unidades_vendidas += 1
            
            if cliente == "Desconocido":
                ventas_desconocidas.append(venta)
            else:
                ventas_conocidas.append(venta)
    
    return ventas_conocidas, ventas_desconocidas, ingresos_totales, unidades_vendidas

# Función para obtener los nombres de todos los clientes
def obtener_nombres_clientes(ventas_conocidas):
    nombres_clientes = set()
    for venta in ventas_conocidas:
        nombres_clientes.add(venta['cliente'])
    return list(nombres_clientes)

# Función para realizar un informe de compras de Darth Vader
def informe_darth_vader(ventas_conocidas):
    compras_darth_vader = []
    for venta in ventas_conocidas:
        if venta['cliente'] == 'Darth Vader':
            compras_darth_vader.append(venta)
    return compras_darth_vader

# Función para aplicar un descuento a clientes que compraron naves con partes recicladas
def aplicar_descuento(ventas_conocidas):
    descuentos = {}
    for venta in ventas_conocidas:
        if venta['partes_recicladas']:
            descuento = venta['precio'] * 0.15
            cliente = venta['cliente']
            if cliente in descuentos:
                descuentos[cliente] += descuento
            else:
                descuentos[cliente] = descuento
    return descuentos

# Función para calcular el ingreso generado por la producción de naves con sigla "AT"
def ingreso_naves_AT(ventas_conocidas):
    ingreso_total = 0
    for venta in ventas_conocidas:
        if "AT" in venta['producto']:
            ingreso_total += venta['precio']
    return ingreso_total

# Ejemplo de uso
if __name__ == "__main__":
    # Procesar datos del archivo de texto
    ventas_conocidas, ventas_desconocidas, ingresos_totales, unidades_vendidas = procesar_datos("ventas_naves.txt")
    print("Ventas conocidas:", ventas_conocidas)
    print("Ventas desconocidas:", ventas_desconocidas)
    print("Ingresos totales:", ingresos_totales)
    print("Unidades vendidas:", unidades_vendidas)
    
    # Obtener nombres de todos los clientes
    nombres_clientes = obtener_nombres_clientes(ventas_conocidas)
    print("Nombres de clientes:", nombres_clientes)
    
    # Realizar un informe de compras de Darth Vader
    compras_darth_vader = informe_darth_vader(ventas_conocidas)
    print("Compras de Darth Vader:", compras_darth_vader)
    
    # Aplicar descuento a clientes que compraron naves con partes recicladas
    descuentos = aplicar_descuento(ventas_conocidas)
    print("Descuentos:", descuentos)
    
    # Calcular ingreso generado por producción de naves con sigla "AT"
    ingreso_naves_AT = ingreso_naves_AT(ventas_conocidas)
    print("Ingreso por naves AT:", ingreso_naves_AT)
