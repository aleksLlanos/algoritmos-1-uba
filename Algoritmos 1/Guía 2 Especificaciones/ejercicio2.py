"""
Ejercicio 2. A partir de las especificaciones del Ejercicio 1, responder las siguientes preguntas:

1. En los problemas raicesCuadradas que utilizan el problema raizCuadrada, ¿Se puede eliminar el requiere "Todos los elementos de s son positivos"? Justificar.

# De poder, se puede, pero generaría muchas inconsistencias. Para empezar, la raíz cuadrada de un número negativo pertenece a los complejos, no a los reales. Entonces la imagen de la función se rompería o devolvería "Nan"    

2. ¿Qué consecuencia tiene en el resultado la diferencia de asegura entre los problemas raicesCuadradasUno y raicesCuadradasDos? Buscar un ejemplo de valor de entrada donde cada problema tenga distinto valor de salida.

3. De acuerdo con la respuesta del ítem anterior, ¿un algoritmo que satisface la especificación de raicesCuadradasUno, también satisface la especificación de raicesCuadradasDos? ¿Y al revés?

4. Explicar en palabras las diferencias entre los problemas raicesCuadradasCinco y raicesCuadradasSeis. ¿Cómo influye el asegura de longitud máxima? Dada la entrada s = ⟨3, 9, 11, 15, 18⟩, ¿es ⟨√3, √9⟩ una salida válida para ambos problemas? Y sea la entrada s = ⟨3, 9, 11⟩, ¿es ⟨√3, √9, √11, √13⟩ una salida válida para el problema raicesCuadradasCinco?

5. ¿Qué cambia en el problema raicesCuadradasCuatro agregar un asegura que diga que resultado tiene la misma longitud que s? Pensar ejemplos de valores de salida que cambien con este nuevo asegura.

6. Si los problemas raicesCuadradasDos y raicesCuadradasTres tienen el mismo resultado para la misma entrada (una secuencia específica de números), ¿quiere decir que son el mismo problema?

7. ¿Qué ocurre si eliminamos los requiere "no hay repetidos"? Dada la entrada s = ⟨4, 1, 1⟩, ¿es ⟨2, 2, 1⟩ una salida válida para el problema raicesCuadradasDos?
"""
