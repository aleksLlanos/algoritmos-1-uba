"""Ejercicio 5. (Frecuencia de bondis) A Ciudad Universitaria (CU) llegan 8 líneas de colectivos: 28, 33, 34, 37, 45, 107, 160 y 166. Con el fin de controlar la frecuencia diaria de cada línea, un grupo de investigación del Departamento de Computación instaló cámaras y un sistema de reconocimiento de imágenes en el ingreso al predio. Durante el día, el sistema identifica el número de línea de cada colectivo que ingresa y lo registra en una secuencia ordenada.

a) Especificar el problema cantidadColectivosDeLinea que a partir de una secuencia de colectivos registrada por el sistema de reconocimiento y el número de una línea que llega a CU, devuelva cuántos colectivos de esa línea ingresaron durante el día.

b) Especificar el problema lineaConMejorFrecuencia que, a partir de dos números de líneas y una secuencia registrada por el sistema, devuelva cuál de las dos líneas tiene mejor frecuencia diaria. Sugerencia: utilizar cantidadColectivosDeLinea.



RESPUESTA DEL ÍTEM a)
problema cantidadColectivosDeLinea (s: seq⟨Z⟩,t: Z ): Z {
    requiere: {Cada elemento de s debe pertenecer al conjunto {28, 33, 34, 37, 45, 107, 160, 166}}
    requiere: {t es un número perteneciente al conjunto {28, 33, 34, 37, 45, 107, 160, 166}}
    asegura: {resultado es la cantidad de veces que t aparece en la s}
}

RESPUESTA DEL ÍTEM b)
problema lineaConMejorFrecuencia (s: seq⟨Z⟩,t: Z,u: Z ): Z {
    requiere: {Cada elemento de s debe pertenecer al conjunto {28, 33, 34, 37, 45, 107, 160, 166}}
    requiere: {t y u son un número perteneciente al conjunto {28, 33, 34, 37, 45, 107, 160, 166}}
    asegura: {resultado es t si cantidadColectivosDeLinea(s,t) es mayor o igual cantidadColectivosDeLinea(s,u)}
    asegura: {resultado es u si cantidadColectivosDeLinea(s,u) es mayor estricto a cantidadColectivosDeLinea(s,t)}
}
"""













lista = [28, 33, 34, 37, 45, 107, 160, 166, 28, 33, 34, 37, 45, 107,28,28,28,12]
num = 28
veces= 0
for i in lista: 
    if num==i:
        veces +=1
    
print(veces)

    