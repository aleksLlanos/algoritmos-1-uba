{--Ejercicio 8. Especificar e implementar la función 
sumaDigitos :: Integer ->Integer 
que calcula la suma de dígitos de
un número natural. Para esta función pueden utilizar div y mod.--}

sumaDigitos :: Integer -> Integer
sumaDigitos n 
    | n<10 =n
    | otherwise = (n `mod` 10) + sumaDigitos(n `div` 10)

{--
Ejercicio 9. Especificar e implementar una función 
esCapicua :: Integer -> Bool que dado n ∈ N≥0 determina si n es un número capicúa.
--}

--Esta función cantDigitos es la misma que la del ejercicio 7 de la guía 4, copiada y pegada.
cantDigitos :: Integer -> Integer
cantDigitos n
    | n < 0 = error "n debe ser mayor o igual a 0"
    | n < 10 = 1
    | otherwise = 1 + cantDigitos (n `div` 10)

esCapicua :: Integer -> Bool
esCapicua n = n == invertir n

invertir :: Integer -> Integer 
invertir n
    | n < 10 = n
    | otherwise = (n `mod` 10)*(10^(cantDigitos n - 1)) + invertir (n `div` 10)
