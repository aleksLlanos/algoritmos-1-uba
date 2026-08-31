"""Ejercicio 1. Dadas las siguientes especificaciones, dar valores de entrada y salida que cumplan con los requiere y asegura respectivamente:

a) problema duplicar (x: Z) : Z {
    requiere: {True}
    asegura: {resultado es el doble de x}
}

#Acepta enteros, devuelve enteros. 
El requiere es como una condición que debe cumplir el input del usuario. En este caso es True, lo que significa que acepta cualquier entero.
El asegura es como una condición que debe cumplir el output del usuario en relación con el input. En este caso es que el resultado debe ser el doble de x. Una posible entrada y salida que cumpla con estas condiciones podría ser: (3, 6) o (-2, -4). En ambos casos, el resultado es el doble del valor de entrada.

b) problema raizCuadrada (x: Z) : R {
    requiere: {x es positivo}
    asegura: {resultado es la raíz cuadrada de x}
}

#Acepta enteros, devuelve reales.
Los enteros ingresados deben ser no negativos.
El programa asegura devolver la raíz cuadrada del input.
Una posible entrada y salida son: (4,2) o (0,0)

c) problema enteroMasCercanoPositivo (x: R) : Z {
    requiere: {True}
    asegura: {resultado es el entero más cercano de x}
    asegura: {resultado es positivo}
}

#Acepta reales, devuelve enteros
El input solo debe ser real, no hay pre condición.
El programa debe devolver el entero positivo más cerano al input.
Una posible entrada y salida son: (9.9 , 10) o (0 , 1) o (5.5 , 6) o (5.5 , 5)

d) problema raicesCuadradasUno (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Todos los elementos de s son positivos}
    requiere: {No hay elementos repetidos en s}
    asegura: {resultado tiene la misma cantidad de elementos que s}
    asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a todos los elementos de la secuencia s}
    asegura: {El orden de la secuencia resultado es el mismo que en la secuencia s, luego de aplicar el problema raizCuadrada}
}

#Acepta una lista de enteros, devuelve una lista de reales. 
Cada elemento de la lista input debe ser no negativo y no debe repetirse a lo largo de la lista.
El programa asegura devolver la misma cantidad de elementos que el input, que cada elemento del output es el output de aplicar "problema raizCuadrada" y puestos en la lista en el mismo orden en el que se aplicó al input.
Posibles entradas y salidas son:([0,2,4,9,16] , [0,√2,2,3,4]) o ([1] , [1]) o ([1,0],[1,0])


e) problema raicesCuadradasDos (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Todos los elementos de s son positivos}
    requiere: {No hay elementos repetidos en s}
    asegura: {resultado tiene la misma cantidad de elementos que s}
    asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a todos los elementos de la secuencia s}
}

#Acepta lista de enteros y devuelve lista de reales. 
Los enteros deben ser positivos y no repetidos en la lista.
EL programa devuelve un output con misma cantidad de elementos que s y cada elemento es el resultado de aplicar problema raizCuadrada a los elementos del input. Nótese como no se dice nada sobre el orden.
Posibles entradas y salidas son: ([0,2,4,9,16] , [√2,0,4,3,2]) o ([1] , [1]) o ([1,0],[1,0])

f) problema raicesCuadradasTres (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Todos los elementos de s son positivos}
    requiere: {No hay elementos repetidos en s}
    asegura: {resultado tiene la misma cantidad de elementos que s}
    asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a uno o varios elementos de la secuencia s}
}

#Acepta lista de enteros, devuelve lista de reales. 
Los enteros deben ser no negativos y no repetidos en la lista.
El programa debe devolver una lista de enteros con la misma cantidad de elementos que el input pero esta vez,
Posibles entradas y salidas: ([0,2,4,9,16], [0,0,0,4,0]) o ([1] , [1]) o ([1,0],[1,0])

g) problema raicesCuadradasCuatro (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Existen elementos de s que son positivos}
    requiere: {No hay elementos repetidos en s}
    asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a todos los elementos de s que son positivos}
}

#Acepta lista enteros, devuelve lista de reales.
Como mínimo debe haber un entero no negativo en el input y ninguno de los enteros se repite en la lista.
EL programa devuelve una lista de enteros que son el resultado de aplicar raizCuadrada a los no negativos enteros.
Entradas, salidas: ([-1,-2,0,2,4,9,16],[0,√2,2,3,4]) o ([-1,1],[1]) o ([1,0],[1,0]) o ([1,0],[0,1])

h) problema raicesCuadradasCinco (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Todos los elementos de s son positivos}
    asegura: {Cada posición de resultado, donde la posición es menor o igual a las de s, es igual a la salida de aplicar raizCuadrada al elemento que se encuentra en esa posición en s}
}

#Acepta lista de enteros, devuelve lista de reales.
Los enteros deben ser positivos y nada más.
El programa debe devolver ehhh, complicado de explicar diferente a lo ya escrito, mejor solo resuelvo.
Entradas, salidas: ([1,1,1,36,4],[1,1,1,6,2,09832109384120984921048091284,49012740217490127,NaN]) o ([9,4],[3])

i) problema raicesCuadradasSeis (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Todos los elementos de s son positivos}
    asegura: {La longitud de resultado es como máximo la misma que s}
    asegura: {Cada posición de resultado, donde la posición es menor o igual a las de s, es igual a la salida de aplicar raizCuadrada al elemento que se encuentra en esa posición en s}
}
#Acepta lista de enteros, devuelve lista de reales.
Los enteros deben ser positivos y nada más.
Los asegura ya son claros, a resolver papurri.
Entradas, salidas: ([1,1,1,36,4],[1,1,1,6,2]) o ([1,1,1,36,4],[1,1,1,6])
"""