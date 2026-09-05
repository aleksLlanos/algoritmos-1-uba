"""Ejercicio 8. Contamos con las siguientes especificaciones del problema sumarAbsMayorA5:

problema sumarAbsMayorA5-version1 (s: seq⟨Z⟩) : Z {
    requiere: {True}
    asegura: {resultado es la sumatoria de todos los elementos de s cuyo valor absoluto es mayor a 5}
}

problema sumarAbsMayorA5-version2 (s: seq⟨Z⟩) : Z {
    requiere: {Todos los elementos de s son positivos}
    asegura: {resultado es la sumatoria de todos los elementos de s cuyo valor absoluto es mayor a 5}
}

problema sumarAbsMayorA5-version3 (s: seq⟨Z⟩) : Z {
    requiere: {Todos los elementos de s son mayores a 10}
    asegura: {resultado es la sumatoria de todos los elementos de s cuyo valor absoluto es mayor a 5}
}

a) ¿Cuál es la relación de fuerza entre los requiere de cada especificación?

#Notemos como el primero admite cualquier entrada. El conjunto de entrada admitida por el segundo es mayor a los del tercero. Es mayor el conjunto de positivos que los de positivos mayores a 10. Entonces el tercero es el más fuerte al ser más restrictivo, el segundo le sigue, y el más débil es el primero.

b) ¿Cuál de las especificaciones tiene el dominio más restringido y cuál menos?

#Basado en el razonamiento anterior y su argumentación correspondiente, es seguro decir que el orden de dominio de más a menos restrictivo es el mismo que el de las relaciones de fuerza. Ya que el requiere de una especificación es una forma de ir poniendo restricciones al dominio.

c) Desde el punto de vista de un programador, ¿qué especificación es más fácil de implementar? Justificar.

#En la primera especificación se admiten enteros que sean negativos, por lo que para prepararse a esta situación, el programador debe crear código que devuelva su valor absoluto analice si es mayor a 5. En la segunda especificación, ya no hay negativos, por lo que no hace falta sacar valores absolutos, pero todavía hay enteros de 0 a 5 que obligarían al programador a evaluar si son mayores a 5. En cambio, en la última especificación, el programador no tiene que hacer evaluaciones de ningún tipo, porque los valores que entran, dado el requiere ya son positivos y mayores a 5, porque son mayores a 10

d) Desde el punto de vista de un usuario, ¿qué contrato es más conveniente? Justificar.

#El usuario se encarga de la entrada, entonces asumiré que el que más le conviene será aquel que no le esté pidiendo tantas cosas, que le resulte más fácil de ingresar datos. Por esta razón, la primera especcificación es la más conveniente porque puede poner la mayor cantidad de entradas sin estar pensando en qué poner y qué no.
 """