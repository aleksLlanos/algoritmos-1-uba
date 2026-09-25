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



{--Ejercicio 18. Implementar una función mayorDigitoPar :: Integer -> Integer según la siguiente especificación: 
problema mayorDigitoPar (n: N) : N {
    requiere: { True }
    asegura: { resultado es el mayor de los dígitos pares de n. Si n no tiene ningún dígito par, entonces resultado es -1. }
}
--}
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar i
    | (i `div` 10 == 0) && (i `mod` 2 == 0) = i -- Si es un único dígito par, que lo devuelva
    | (i `div` 10 == 0) = -1 --si es un es único número impar, -1
    | (i `mod` 2 == 0) = comparoDigitos (i `div` 10) (i `mod` 10) --Si tiene más de un dígito, veo si el último es par y si lo es, lo mando a comparoDigitos. Solo se activa si encuentra un par, sino, sigue analizando hasta llegar a los casos
    | otherwise = mayorDigitoPar (i `div` 10)
    where
    comparoDigitos :: Integer -> Integer -> Integer
    comparoDigitos n m --recibo el número sin su último dígito y su último dígito par
        | n == 0 = m -- Caso base dice que n llegará a ser 0 y estará acompañado de su mayor par, devolviendo ese par
        | n `mod` 2 == 0 = comparoDigitos (n `div` 10) (mayorEntre (n`mod`10) m) --si el último dígito es par, hacemos la función acompañado del nuevo mayor par analizado entre el anterior y el último nuevo par
        | otherwise = comparoDigitos (n `div` 10) m -- si no era par, seguimos con el que ya teníamos
        where
        mayorEntre :: Integer -> Integer -> Integer
        mayorEntre n m
            | n<=m = m
            | otherwise = n 
 

