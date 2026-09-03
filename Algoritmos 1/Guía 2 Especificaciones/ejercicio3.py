"""Ejercicio 3. Dada la siguiente especificación del problema de ordenar una secuencia de enteros, en la que se debe tomar una secuencia de números enteros y devolver los mismos elementos ordenados de menor a mayor:

problema ordenar (s: seq⟨Z⟩) : seq⟨Z⟩ {
    requiere: {True}
    asegura: {resultado es una secuencia en la cual cada elemento es estrictamente mayor que el anterior}
}

Responder las siguientes preguntas:

a) Dada s = ⟨4, 3, 5⟩ como secuencia de entrada, ¿es resultado = ⟨3, 4, 5⟩ una solución válida según la especificación?

b) Dada s = ⟨4, 3, 3, 5⟩ como secuencia de entrada, ¿es resultado = ⟨3, 3, 4, 5⟩ una solución válida según la especificación? Corregir la especificación modificando el requiere.

c) Si tomamos s = ⟨4, 3, 5⟩ como secuencia de entrada, ¿es resultado = ⟨3, 4⟩ una solución válida según la especificación? Corregir la especificación modificando el asegura.

d) Si tomamos s = ⟨4, 3, 5⟩ como secuencia de entrada, ¿es resultado = ⟨3, 4, 5, 6⟩ una solución válida según la especificación? Corregir la especificación modificando el asegura.

e) Dada s = ⟨8, 5, 7⟩ como secuencia de entrada, ¿es resultado = ⟨1, 2, 3⟩ una solución válida según la especificación?

f) Escribir una especificación que permita recibir cualquier secuencia de enteros s como parámetro y garantice que resultado contiene el resultado de ordenar correctamente los elementos de s de menor a mayor."""