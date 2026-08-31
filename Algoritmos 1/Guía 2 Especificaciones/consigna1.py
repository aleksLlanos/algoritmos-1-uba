"""Ejercicio 1. Dadas las siguientes especificaciones, dar valores de entrada y salida que cumplan con los requiere y asegura respectivamente:

a) problema duplicar (x: Z) : Z {
    requiere: {True}
    asegura: {resultado es el doble de x}
}

b) problema raizCuadrada (x: Z) : R {
    requiere: {x es positivo}
    asegura: {resultado es la raíz cuadrada de x}
}


c) problema enteroMasCercanoPositivo (x: R) : Z {
    requiere: {True}
    asegura: {resultado es el entero más cercano de x}
    asegura: {resultado es positivo}
}

d) problema raicesCuadradasUno (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Todos los elementos de s son positivos}
    requiere: {No hay elementos repetidos en s}
    asegura: {resultado tiene la misma cantidad de elementos que s}
    asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a todos los elementos de la secuencia s}
    asegura: {El orden de la secuencia resultado es el mismo que en la secuencia s, luego de aplicar el problema raizCuadrada}
}

e) problema raicesCuadradasDos (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Todos los elementos de s son positivos}
    requiere: {No hay elementos repetidos en s}
    asegura: {resultado tiene la misma cantidad de elementos que s}
    asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a todos los elementos de la secuencia s}
}

Página 1 de 5 Compilado el 2025/08/19

f) problema raicesCuadradasTres (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Todos los elementos de s son positivos}
    requiere: {No hay elementos repetidos en s}
    asegura: {resultado tiene la misma cantidad de elementos que s}
    asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a uno o varios elementos de la secuencia s}
}

g) problema raicesCuadradasCuatro (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Existen elementos de s que son positivos}
    requiere: {No hay elementos repetidos en s}
    asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a todos los elementos de s que son positivos}
}

h) problema raicesCuadradasCinco (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Todos los elementos de s son positivos}
    asegura: {Cada posición de resultado, donde la posición es menor o igual a las de s, es igual a la salida de aplicar raizCuadrada al elemento que se encuentra en esa posición en s}
}

i) problema raicesCuadradasSeis (s: seq⟨Z⟩) : seq⟨R⟩ {
    requiere: {Todos los elementos de s son positivos}
    asegura: {La longitud de resultado es como máximo la misma que s}
    asegura: {Cada posición de resultado, donde la posición es menor o igual a las de s, es igual a la salida de aplicar raizCuadrada al elemento que se encuentra en esa posición en s}
}"""
