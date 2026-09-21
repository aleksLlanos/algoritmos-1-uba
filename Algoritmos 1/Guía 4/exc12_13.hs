{--
Ejercicio 12. Para n ∈ N se define la sucesión:

    aₙ = 2 + 1 / (2 + 1 / (... + 1 / (2 + 1/2)))

    (aparece n veces el 2).

Lo cual resulta en la siguiente definición recursiva: a₁ = 2, aₙ = 2 + 1 / aₙ₋₁.

Utilizando esta sucesión, especificar e implementar una función raizDe2Aprox :: Integer -> Float que dado n ∈ N devuelva la aproximación de √2 definida por √2 ≈ aₙ-1.

Por ejemplo:

    raizDe2Aprox 1 ⇝ 1
    raizDe2Aprox 2 ⇝ 1,5
    raizDe2Aprox 3 ⇝ 1,4
--}

--Esta función cumple con la definición recursiva de la sucesión aₙ, solo que el resultado final de esta función es aₙ, no aₙ-1. Por eso, en la función raizDe2Aprox se le resta 1 al resultado de sucesionA.
sucesionA :: Integer -> Float
sucesionA n 
    |n == 1 = 2
    |otherwise = 2 + 1 / sucesionA (n-1)

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n 
    | n <= 0    = error "Solo naturales positivos"
    | otherwise = sucesionA n - 1

{--
Ejercicio 13. Especificar e implementar la siguiente función:

    f(n, m) = Σ (i = 1 hasta n) Σ (j = 1 hasta m) i^j 
--}

--Lo primero que se me ocurre es crear 2 funciones auxiliares, una que calcule la suma de i^j para un i fijo y otra que calcula la suma de todas esas sumas para todos los i desde 1 hasta n.

sumaDePotencias :: Integer -> Integer -> Integer
sumaDePotencias n m 
    | m == 0 = 0
    | otherwise = n^m + sumaDePotencias n (m-1)

--El caso base es n == 0 porque cuando n==1, seguirá a sumaDePotencias 1 m, que es lo que queremos como último paso de la recursión. Por eso, cuando n==0, devolvemos 0.
sumaDeSumaDePotencias :: Integer -> Integer ->Integer
sumaDeSumaDePotencias n m 
    | n == 0 = 0
    | otherwise = sumaDePotencias n m + sumaDeSumaDePotencias (n-1) m

--Especificación:
{--
problema SumaDeSumaDePotencias (n: Z, m: Z) : Z
    requiere: {n >=1 and m >= 1} 
    asegura: {resultado = Σ (i = 1 hasta n) Σ (j = 1 hasta m) i^j}
--}