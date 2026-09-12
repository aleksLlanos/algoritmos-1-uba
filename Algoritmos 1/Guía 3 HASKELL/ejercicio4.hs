import GHC.Internal.Natural (Natural)
{----
Ejercicio 4. Especificar e implementar las siguientes funciones utilizando tuplas para representar pares y ternas de números.
----}

{----
a) productoInterno: calcula el producto interno entre dos tuplas de R × R.
----}

productoInterno :: (Float, Float) -> (Float, Float) -> Float
productoInterno (x1, y1) (x2, y2) = x1 * x2 + y1 * y2

{----
b) esParMenor: dadas dos tuplas de R × R, decide si cada coordenada de la primera tupla es menor a la coordenada correspondiente de la segunda tupla.
----}
esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor (x1, y1) (x2, y2) = x1 < x2 && y1 < y2
{----
c) distancia: calcula la distancia euclídea entre dos puntos de R².
----}

distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (x1, y1) (x2, y2) = ((x1-x2)^2+(y1-y2)^2)**(1/2)


{----
d) sumaTerna: dada una terna de enteros, calcula la suma de sus tres elementos.
----}

sumaTerna :: (Int,Int,Int) -> Int
sumaTerna (x, y, z) = x+y+z

{----
e) sumarSoloMultiplos: dada una terna de números enteros y un natural, calcula la suma de los elementos de la terna que son múltiplos del número natural.

Por ejemplo:

    sumarSoloMultiplos (10, -8, -5) 2 ⇝ 2
    sumarSoloMultiplos (66, 21, 4) 5 ⇝ 0
    sumarSoloMultiplos (-30, 2, 12) 3 ⇝ -18
----}

esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y = x `mod` y == 0


sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (a, b, c) n = 
    (if esMultiploDe a n then a else 0) +
    (if esMultiploDe b n then b else 0) +
    (if esMultiploDe c n then c else 0)


{----
f) posPrimerPar: dada una terna de enteros, devuelve la posición del primer número par si es que hay alguno, o devuelve 4 si son todos impares.
----}


posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x, y, z)
  | x `mod` 2 == 0 = 1
  | y `mod` 2 == 0 = 2
  | z `mod` 2 == 0 = 3 
  | otherwise = 4
  
{----
g) crearPar :: a -> b -> (a, b): a partir de dos componentes, crea un par con esos valores. Debe funcionar para elementos de cualquier tipo.
----}

crearPar :: a -> b -> (a,b)
crearPar x y = (x, y)

{----
h) invertir :: (a, b) -> (b, a): invierte los elementos del par pasado como parámetro. Debe funcionar para elementos de cualquier tipo.
----}

invertir :: (a, b) -> (b, a)
invertir (x, y) = (y, x)

{----
i) Reescribir los ejercicios productoInterno, esParMenor y distancia usando el siguiente renombre de tipos:

    type Punto2D = (Float, Float)
----}

type Punto2D = (Float, Float)

esParMenor' :: Punto2D -> Punto2D -> Bool
esParMenor' (x1, y1) (x2, y2) = x1 < x2 && y1 < y2

productoInterno' :: Punto2D -> Punto2D -> Float
productoInterno' (x1, y1) (x2, y2) = x1 * x2 + y1 * y2

distancia' :: Punto2D -> Punto2D -> Float
distancia' (x1, y1) (x2, y2) = ((x1-x2)^2+(y1-y2)^2)**(1/2)