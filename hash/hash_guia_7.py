
#! EJERCICIO 7

#! Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
#! que contemple las siguientes actividades:

#! a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
#! tabla la función hash deberá utilizar el número del Pokémon como clave, mientras que en
#! la tercera el campo clave de la función hash será por el nombre del Pokémon.
#! b. el tamaño de la primera tabla debe ser lo suficientemente grande como para que pueda
#! almacenar todos los distintos tipos de Pokémon, debe manejar las colisiones con alguna
#! función de sondeo;
#! c. el tamaño de cada una de las segundas tablas debe ser 15;
#! d. el algoritmo debe permitir cargar tipos de Pokémon en la primera tabla y crear su respec-
#! tiva segunda tabla, –en el caso de que no exista–;
#! e. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen
#! estos tipos;
#! f. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo, nivel.