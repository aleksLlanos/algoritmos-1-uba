"""Ejercicio 7. Contamos con las siguientes especificaciones del problema pares:

problema pares1 (s: seq⟨Z⟩) : seq⟨Z⟩ {
    requiere: {s no tiene elementos repetidos}
    asegura: {Los elementos de resultado son pares y pertenecen a s}
    asegura: {Los elementos de s que son pares, pertenecen a resultado}
    asegura: {resultado no tiene elementos repetidos}
}

problema pares2 (s: seq⟨Z⟩) : seq⟨Z⟩ {
    requiere: {s no tiene elementos repetidos}
    asegura: {Los elementos de resultado son pares y pertenecen a s}
    asegura: {Los elementos de s que son pares, pertenecen a resultado}
    asegura: {resultado no tiene elementos repetidos}
    asegura: {resultado está ordenada de manera creciente}
}

a) Si contamos con un algoritmo P que satisface pares1, ¿satisface P la especificación pares2? Justificar.

#RESPUESTA: 
Antes que nada, me gustaría que notemos como pares2 tiene un asegura más, una postcondición más. 
Ambas especificaciones tienen las mismas precondiciones, pero resultado tiene más condiciones para salir en pares2 que en pares1. El conjunto de posibles sencuencias de entrada es el mismo, pero el de posibles salidas son diferentes. Concretamente, al pares2 establecer un orden específico, estamos descartando todos los otros posibles ordenes de la misma salida. Entonces los "algoritmos" que satisfacen pares2, satisfacen pares1, pero no al revés.

b) Si contamos con un algoritmo P que satisface pares2, ¿satisface P la especificación pares1? Justificar.

#Como argumenté en la respuesta del ítem a), que un algoritmos P satisfaga pares2, significa que satisface pares1. De una misma salida, pares1 admite también cualquier orden de los elementos de esa salida, incluyendo el de orden creciente. Sin embargo este orden creciente es el único que admite pares2.

c) ¿Cuál es la relación de fuerza entre la postcondición de pares1 y la de pares2?

#Como los algoritmos que satisfacen a pares1 son más que los que satisfacen pares2 y, además los que satisfacen pares2, automáticamente satisfacen pares1, puedo decir que la relación de fuerza es que pares2 es más fuerte que pares1, porque es más complicada de cumplir"""