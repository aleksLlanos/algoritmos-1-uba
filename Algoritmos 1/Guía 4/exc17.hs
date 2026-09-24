import GHC.Base (compareWord)
{--Ejercicio 17. Implementar la función esFibonacci :: Integer -> Bool según la siguiente especificación:

problema esFibonacci (n: Z) : B {
    requiere: { n ≥ 0 }
    asegura: { resultado = true ↔ n es algún valor de la secuencia de Fibonacci definida en el ejercicio 1 }
}
--}

esFibonacci :: Integer -> Bool
esFibonacci n = recorroFibonacci n 0 1
    where
        -- m1 y m2 representan dos números consecutivos de la secuencia de Fibonacci
        recorroFibonacci :: Integer -> Integer -> Integer -> Bool
        recorroFibonacci n m1 m2
            | n == m1   = True
            | n < m1    = False
            | otherwise = recorroFibonacci n m2 (m1 + m2)

{--Ejercicio 18. Implementar una función mayorDigitoPar :: Integer -> Integer según la siguiente especificación:

problema mayorDigitoPar (n: N) : N {
    requiere: { True }
    asegura: { resultado es el mayor de los dígitos pares de n. Si n no tiene ningún dígito par, entonces resultado es -1. }
}
--}

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n
    | n `div` 10 == 0 && even n = n
    | n `m` = mayorDigitoPar (comparoDigitosPares (n`div`10) (n `mod` 10))

comparoDigitosPares :: Integer -> Integer -> Integer
comparoDigitosPares n m
    | n `mod`10 < m = n
    | otherwise = m




