{--
Ejercicio 1. Implementar la función fibonacci :: Integer -> Integer que devuelve el i-ésimo número de Fibonacci.

Recordar que la secuencia de Fibonacci se define como:

    fib(n) = 0                si n = 0
    fib(n) = 1                si n = 1
    fib(n) = fib(n - 1) + fib(n - 2)    en otro caso

problema fibonacci (n : Z) : Z {
    requiere: {n ≥ 0}
    asegura: {resultado = fib(n)}
}
--} 

fibonacci :: Integer -> Integer
fibonacci n | n == 0    = 0
            | n == 1    = 1
            | n > 1 = fibonacci (n - 1) + fibonacci (n - 2) 
            | otherwise = error "n debe ser mayor o igual a 0"

{--
Ejercicio 2. Implementar una función parteEntera :: Float -> Integer según la siguiente especificación:

problema parteEntera (x : R) : Z {
    requiere: {x ≥ 0}
    asegura: {resultado ≤ x < resultado + 1}
}
--}

--parteEntera pero sin floor
parteEntera :: Float -> Integer
parteEntera x | x < 0 = error "x debe ser mayor o igual a 0"
                | otherwise = parteEnteraAux x 0

parteEnteraAux :: Float -> Integer -> Integer
parteEnteraAux x n | x >= 1 = parteEnteraAux (x - 1) (n + 1) --va restando 1 a x y sumando 1 a n hasta que x sea menor que 1. Al final devuelve n que es la parte entera de x
                    | otherwise = n

{--
Ejercicio 3. Especificar e implementar la función esDivisible :: Integer -> Integer -> Bool que dados dos números naturales determinar si el primero es divisible por el segundo. No está permitido utilizar las funciones mod ni div.
--}

esDivisible :: Integer -> Integer -> Bool
esDivisible a b | b == 0 = error "El divisor no puede ser cero"
                 | a < 0 || b < 0 = error "Los números deben ser naturales"
                 | a == 0 = True
                 | a < b = False
                 | otherwise = esDivisible (a - b) b

{--
Ejercicio 4. Especificar e implementar la función sumaImpares :: Integer -> Integer que dado n ∈ N sume los primeros n números impares. Por ejemplo: sumaImpares 3 ❀ 1+3+5 ⇝ 9.
--}

sumaImpares :: Integer -> Integer
sumaImpares n   
    | n < 0 = error "n debe ser un número natural"
    | n == 0 = 0
    | otherwise = sumaImpares (n - 1) + (2 * n - 1)

{--Ejercicio 5. Implementar la función medioFact :: Integer -> Integer que dado n ∈ N calcula n!! = n (n−2)(n−4) · · · .

problema medioFact (n: Z) : Z {
    requiere: { n ≥ 0 }
    asegura: { resultado = ⌊(n−1)/2⌋ Σ (i=0) (n − 2i) }
}

Por ejemplo:

    medioFact 10 ❀ 10 ∗ 8 ∗ 6 ∗ 4 ∗ 2 ❀ 3840.
    medioFact 9 ❀ 9 ∗ 7 ∗ 5 ∗ 3 ∗ 1 ❀ 945.
    medioFact 0 ❀ 1.--}

medioFact' :: Integer -> Integer
medioFact' n | n < 0 = error "n debe ser un número natural"
             | n == 0 = 1
             | otherwise = n * medioFact' (n - 2) 
--Esta función medioFact tiene un problema para números impares porque en la llamada recursiva, cuando n es impar, eventualmente llegará a 1 y luego a -1, lo cual no está definido en la función. Para corregir esto, podemos agregar un caso base para n == 1:
          --  | n == 1 = 1


medioFact :: Integer -> Integer
medioFact n | n < 0 = error "n debe ser un número natural"
            | n == 0 = 1
            | n == 1 = 1
            | otherwise = n * medioFact (n - 2) 