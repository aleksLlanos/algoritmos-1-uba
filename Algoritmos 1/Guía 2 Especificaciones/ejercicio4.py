"""Ejercicio 4. Se desea especificar el problema de reemplazar cada elemento de una secuencia de enteros por su doble y se cuenta con la siguiente especificación:

problema duplicarTodos (s: seq⟨Z⟩) : seq⟨Z⟩ {
    requiere: {True}
    asegura: {resultado tiene la misma cantidad de elementos que s}
}

a) ¿Qué problemas tiene la especificación dada? Dar ejemplos de valores para resultado que satisfagan la especificación pero no sean respuestas correctas.

#JAJAJ el único asegura que tiene garantiza únicamente que tengan la misma cantidad de elementos, no dice nada sobre cuáles elementos deben ser, en qué orden, qué condición deben cumplir ni nadaaa. Te pueden arrojar (2) y devolver (1), o dar (5,3,1) y devolver (4,4,4). Muchas inconsistencias en busca del doble de cada elemento de s en un orden específico, tanto que honestamente me reí porque estaba en mood ultra especificaciones exactas sin huecos legales nivel ultra pro y de la nada veo esto jaja.

b) Indicar cuál/es de los siguientes asegura debería/n ser agregado/s a la especificación. Justificar en cada caso por qué deberían o no ser agregados.

    asegura: {Para cada valor x que pertenece a s, hay algún valor en resultado que es la salida de duplicar(x)}

    #No debería ser agregado, porque admite entradas y salidas así: ([1,2],[4,2]). Donde el doble de cada elemento de s está en resultado pero no en el orden solicitado.

    asegura: {En cada posición de resultado, el valor es mayor al valor en esa misma posición de s}

    #No dice nada sobre duplicar

    asegura: {En cada posición de resultado, el valor es igual a la salida de aplicar duplicar al valor en esa misma posición de s}

    #Esta por si sola es perfecta al añadirse a la especificación ya existente.

    asegura: {Todos los elementos de resultado son números pares}
    
    #no dice nada de duplicar

Nota: el problema duplicar(x) está especificado en el Ejercicio 1."""