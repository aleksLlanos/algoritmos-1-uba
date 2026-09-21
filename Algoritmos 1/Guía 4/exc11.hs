{--
Ejercicio 11.

a) Especificar e implementar una función eAprox :: Integer -> Float que aproxime el valor del número e a partir de la siguiente sumatoria:

    e^(n) = Σ (i = 0 hasta n) 1 / i!
--}


--Esta función calcula el factorial de un número entero no negativo.
factorial :: Integer -> Integer --n es un Integer y el resultado de factorial (n - 1) es un Float. Cuando intentas hacer n * factorial (n - 1), estás multiplicando un Integer por un Float, y Haskell no permite mezclar tipos directamente con el operador *.
factorial n
    | n < 0 = error "n debe ser mayor o igual a 0"
    | n == 0 = 1
    | otherwise = n * factorial (n - 1)

eAprox :: Integer -> Float
eAprox n
    | n < 0 = error "n debe ser mayor o igual a 0"
    | n == 0 = 1.0
    | otherwise = 1.0 / fromIntegral (factorial n) + eAprox (n - 1) --acá fromIntegral convierte el resultado de factorial n (que es un Integer) a Float para que la división sea válida.

{--
b) Definir la constante e :: Float como la aproximación de e a partir de los primeros 10 términos de la serie anterior.

¡Atención! A veces ciertas funciones esperan un Float y nosotros tenemos un Int. Para estos casos podemos utilizar la función fromIntegral :: Int -> Float definida en el Preludio de Haskell.
--}

e :: Float 
e = eAprox 10