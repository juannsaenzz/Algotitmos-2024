
#! EJERCICIO 11

#! Nick Fury director de la agencia S.H.I.E.L.D. intenta detener a la organización Hydra y a su
#! líder Red Skull, los agentes de la agencia pueden interceptar los mensajes de Hydra pero están
#! cifrados, por tanto no pueden hacer nada con estos; afortunadamente el Capitán América en
#! una misión encubierta logró determinar las pautas del método de codificación. Ahora Fury
#! nos solicita desarrollar el algoritmo que permita decodificar los mensajes, contemplando las
#! siguientes pautas:

#! a. Las codificación se realiza de la siguiente manera:
#! I. primero se convierte el carácter a su valor en la tabla ASCII y se lo multiplica por 37
#! para transformarlo en un número de cuatro dígitos;
#! II. segundo se calcula un complemento en base al valor del carácter:

#! complemento(caracter) = 79 + caracter - 32, si caracter <= 78
#! complemento(caracter) = 32 + caracter - 79, si caracter > 78

#! III. luego a cada digito obtenido en el punto uno se lo eleva al cuadrado y se le suma
#! un complemento obtenido en el punto anterior y se transforma a carácter;
#! IV. por último se juntan los cuatros caracteres y se le agrega al final el carácter corres-
#! pondiente al complemento.
#! Por ejemplo el carácter R se codifica de la siguiente manera:
#! R = 82, 82 * 37 = 3034, complemento = 32 + 82 – 79 = 35 = “#”
#! 3^2 + 35 = 44 = “,”, 0^2 + 35 = 35 = “#”, 3^2 + 35 = 44 = “,”, 4^2 + 35 = 51 = “3”
#! El resultado final son estos cinco caracteres “,#,3#”;
#! b. deberá utilizar una tabla hash cerrada para almacenar cada una de las cadenas de carac-
#! teres –de cinco caracteres– asociados a cada clave, una buena alternativa para la función
#! hash podría ser la función de Bernstein;
#! c. no se debe decodificar todas las cadenas de caracteres, esto debe hacerse a medida que se
#! necesitan y no están en la tabla;
#! d. ayuda al Capitán América descifrando los siguientes tres mensajes para poder conocer
#! cuáles serán los próximos movimientos de Hydra (los mensajes están almacenados en ar-
#! chivos de texto, que deberá leerlos previamente desde cada archivo, en el siguiente link:
#! https://github.com/belwalter/mensajes_codificados).