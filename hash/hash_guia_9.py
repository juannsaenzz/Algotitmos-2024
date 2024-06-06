
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