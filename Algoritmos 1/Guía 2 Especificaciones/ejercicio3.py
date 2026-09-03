"""Ejercicio 3. Dada la siguiente especificación del problema de ordenar una secuencia de enteros, en la que se debe tomar una secuencia de números enteros y devolver los mismos elementos ordenados de menor a mayor:

problema ordenar (s: seq⟨Z⟩) : seq⟨Z⟩ {
    requiere: {True}
    asegura: {resultado es una secuencia en la cual cada elemento es estrictamente mayor que el anterior}
}

Responder las siguientes preguntas:

a) Dada s = ⟨4, 3, 5⟩ como secuencia de entrada, ¿es resultado = ⟨3, 4, 5⟩ una solución válida según la especificación?

#Sí. 

b) Dada s = ⟨4, 3, 3, 5⟩ como secuencia de entrada, ¿es resultado = ⟨3, 3, 4, 5⟩ una solución válida según la especificación? Corregir la especificación modificando el requiere.

#No es un resultado válido porque el segundo elemento de la salida no estrictamente mayor al primero. Una forma de arreglarlo es poniendo un requiere que diga algo como "NO hay elementos repetidos en s.


c) Si tomamos s = ⟨4, 3, 5⟩ como secuencia de entrada, ¿es resultado = ⟨3, 4⟩ una solución válida según la especificación? Corregir la especificación modificando el asegura.

#Sí, porque no dice nada sobre la cantidad de elementos que devuelve la salida. Una posible solución sería añadir un asegura que diga algo como "La cantidad de elementos de resultado es la misma que la de s"

d) Si tomamos s = ⟨4, 3, 5⟩ como secuencia de entrada, ¿es resultado = ⟨3, 4, 5, 6⟩ una solución válida según la especificación? Corregir la especificación modificando el asegura.

#Con el asegura que puse anteriormente, no, pero aún se devuelven valores como (1,2,3) cuando ingreso (3,4,5). Una forma de arreglarlo es añadiendo otro asegura que diga "Todos los elementos de s están en resultado"

e) Dada s = ⟨8, 5, 7⟩ como secuencia de entrada, ¿es resultado = ⟨1, 2, 3⟩ una solución válida según la especificación?

#Con el requiere y los dos aseguras que puse, ya no. 

f) Escribir una especificación que permita recibir cualquier secuencia de enteros s como parámetro y garantice que resultado contiene el resultado de ordenar correctamente los elementos de s de menor a mayor.

#Mi especificación final sería: 

problema ordenar (s: seq⟨Z⟩) : seq⟨Z⟩ {
    requiere: {True}
    asegura: {cada elemento de s, aparece en resultado la misma cantidad de veces que apareció en s}
    asegura: {resultado tiene la misma cantidad elementos que s}
    asegura: {sea i un valor entre 0 y len(s)-2, el elemento en la posición i cumple i<=i+1 

    (6,31,-5,6,2) # 5 elementos. 5-2=3
    (-5,2,6,6,31) #la posición 0 la tiene -5, luego la 1 es 2, la 2 es 6, la 3 es 6 y este 6 debe ser menor o igual al que le sigue, al de la posición 4 que es 31. Este 31 no cumple nada, solo ser mayor o igual al anterior.
}

"""

