"""
Ejercicio 2. A partir de las especificaciones del Ejercicio 1, responder las siguientes preguntas:

1. En los problemas raicesCuadradas que utilizan el problema raizCuadrada, ¿Se puede eliminar el requiere "Todos los elementos de s son positivos"? Justificar.

# De poder, se puede, pero generaría muchas inconsistencias. Para empezar, la raíz cuadrada de un número negativo pertenece a los complejos, no a los reales. Entonces la imagen de la función se rompería o devolvería "Nan"    

2. ¿Qué consecuencia tiene en el resultado la diferencia de asegura entre los problemas raicesCuadradasUno y raicesCuadradasDos? Buscar un ejemplo de valor de entrada donde cada problema tenga distinto valor de salida.

#raicesCuadradasUno tiene un asegura más que raizCUadradaDos. Este asegura establece un orden específico para la salida del programa. Como la segunda especificación no lo tiene, entonces esa misma salida puede ser válida en distintos ordenes para seguir siendo una salida válida. Por lo que si una lista de n elementos es válida en raicesCuadradasUno, entonces esa misma lista de n elementos es válida también para raicesCuadradasDos y también hay n! posibles ordenes válidos para devolver esa lista.


3. De acuerdo con la respuesta del ítem anterior, ¿un algoritmo que satisface la especificación de raicesCuadradasUno, también satisface la especificación de raicesCuadradasDos? ¿Y al revés?

#Sí, una salida de raicesCuadradasUno satisface la salida de raicesCuadradasDos, pero no al revés. La primer especificación admite un solo orden específico de n elementos. en cambio en la segunda hay n! posibles ordenes, de los cuales solo 1 satisface la raicesCuadradasUno, todas las demás no lo hacen. Así que no vale al revés a pesar de haber un solo caso donde sí.


4. Explicar en palabras las diferencias entre los problemas raicesCuadradasCinco y raicesCuadradasSeis. ¿Cómo influye el asegura de longitud máxima? Dada la entrada s = ⟨3, 9, 11, 15, 18⟩, ¿es ⟨√3, √9⟩ una salida válida para ambos problemas? Y sea la entrada s = ⟨3, 9, 11⟩, ¿es ⟨√3, √9, √11, √13⟩ una salida válida para el problema raicesCuadradasCinco?

#Voy a referirme a raicesCuadradasCinco como CINCO y a la otra como SEIS. SEIS y CINCO tiene las mismas especificacione, a excepción de que SEIS tiene un asegura más, el cual establece un número máximo de elemntos para la salida, la misma cantidad de elementos que la entrada. Como cinco no tiene esta condición, una vez que cumpla con sus aseguras, puede poner infinitos elementos infinitamente variados en todos los reales.
La salida ⟨√3, √9⟩ para la entrada ⟨3, 9, 11, 15, 18⟩ es válida para ambas especifcaciones porque cumple con SEIS y no tiene elementos de más, lo cual CINCO también permite. Por lo anterior, ⟨√3, √9, √11, √13⟩ es una salida válida para CINCO cuando (3, 9, 11⟩ es la entrada.



5. ¿Qué cambia en el problema raicesCuadradasCuatro al agregar un asegura que diga que resultado tiene la misma longitud que s? Pensar ejemplos de valores de salida que cambien con este nuevo asegura.

#Llamaré a raicesCUadradasCuatro, CUATRO. Al igual que en CINCO, CUATRO no tiene una longitud máxima para su lista, por que una vez cumplida la aplicación de raizCuadrada a cada elemento positivo de s,puede añadir infinitos elementos reales a la lista. Si agregamos el asegura que propone la consigna, entonces una posible entrada y salida son([-2,-1,1,4],[2,1,0,0]) donde los primeros 2 elementos de la salida son el resultado de aplicar raizCuadrad a los positivos, puestos sin importar el orden y luego se añaden dos reales más cualquiera para igualar la cantidad de elementos.

6. Si los problemas raicesCuadradasDos y raicesCuadradasTres tienen el mismo resultado para la misma entrada (una secuencia específica de números), ¿quiere decir que son el mismo problema?

#No. Los llamaré DOS y TRES respectivamente. TRES asegura que el resultado tendrá al menos un elemento que es resultado de aplicar raizCuadrada a algún elemento de s. En cambio DOS dice que ocurre lo mismo pero CON TODOS. No hace falta explicar más

7. ¿Qué ocurre si eliminamos los requiere "no hay repetidos"? Dada la entrada s = ⟨4, 1, 1⟩, ¿es ⟨2, 2, 1⟩ una salida válida para el problema raicesCuadradasDos?

#SI eliminamos el requiere "no hay repetido", entonces pueden haber repetidos en la entrada. Sí. DOS dice que los elementos de resultado son la salida de aplicar raizCuadrada a TODOS los elementos de la secuencia s, entonces si la secuencia s tiene los elementos (4,1,1), la raíces cuadradas son respectivamenete (2,1,1). Como dice que los elementos de resultado son la salida de aplicar raizCuadrada a TODOS los elementos de s, notarás que 2 es la raíz cuadrada 4 y 1 es la raíz cuadrada del segundo y tercer elemento. La saluda (2,1) o (1,2) ya sería suficiente si no tuvieran que tener los mismos elementos que s, pero como DOS deber tener almenos un elemento más y deben ser si o si raíz de los elementos de s, podés repetir el 2 o el 1, nadie dice nada sobre que no pueden haber repetidos siempre cuando sean raíz cuadrada de los elementos de s y ya hayas cumplido con el último asegura. """
