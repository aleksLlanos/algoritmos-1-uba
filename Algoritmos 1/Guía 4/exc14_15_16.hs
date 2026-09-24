{--Ejercicio 14. Especificar e implementar una función 
sumaPotencias :: Integer -> Integer -> Integer -> Integer
que dados tres naturales q, n, m sume todas las potencias de la forma q^(a+b) con 1 ≤ a ≤ n y 1 ≤ b ≤ m.
--}

-- q^(a+b)
-- a = [1 ; n]
-- b = [1 ; m]

-- Lo primero que se me ocurre es crear 2 funciones auxiliares, una que calcule la suma de q^(a+b) para un a fijo y un b que varíe de 1 a m, y otra que sume todas esas sumas para todos los a desde 1 hasta n.
sumaPotenciasAfijo :: Integer -> Integer -> Integer -> Integer
sumaPotenciasAfijo q n m 
    | m == 0 = 0
    | otherwise = q^n * q^m + sumaPotenciasAfijo q n (m-1)

sumaPotenciasAvaria :: Integer -> Integer -> Integer -> Integer
sumaPotenciasAvaria q n m
    | n == 0 = 0
    | otherwise = sumaPotenciasAfijo q n m + sumaPotenciasAvaria q (n-1) m

{--
Ejercicio 15. Implementar una función sumaRacionales :: Integer -> Integer -> Float que dados dos naturales n, m sume todos los números racionales de la forma p/q con 1 ≤ p ≤ n y 1 ≤ q ≤ m, es decir:

problema sumaRacionales (n : N, m : N) : R {
    requiere: { True }
    asegura: { resultado = Σ (p = 1 hasta n) Σ (q = 1 hasta m) p / q }
}
--}

sumaPfijo :: Integer -> Integer -> Float
sumaPfijo n m
    | m == 0 = 0
    | otherwise = fromIntegral n/fromIntegral m + sumaPfijo n (m-1)


sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n m 
    | n == 0 = 0
    | otherwise = sumaPfijo n m + sumaRacionales (n-1) m

-- Ejercicio 16. Recordemos que un entero p > 1 es primo si y sólo si no existe un entero k tal que 1 < k < p y k divida a p.

-- a) Implementar menorDivisor :: Integer -> Integer que calcule el menor divisor (mayor que 1) de un natural n pasado como parámetro.
menorDivisor :: Integer -> Integer
menorDivisor n 
    | n <= 1    = error "El número debe ser mayor que 1"
    | otherwise = buscarDivisor n 2

buscarDivisor :: Integer -> Integer -> Integer
buscarDivisor n d
    | d * d > n      = n  -- Si d supera la raíz cuadrada de n, entonces n es primo y su menor divisor es él mismo, por contradicción matemática.
    | n `mod` d == 0 = d  -- Si el resto es 0, encontramos el menor divisor
    | otherwise      = buscarDivisor n (d + 1) -- Probamos con el siguiente

-- b) Implementar la función esPrimo :: Integer -> Bool que indica si un número natural pasado como parámetro es primo.

-- es este caso usé a la función menorDivisor para 
esPrimo :: Integer -> Bool
esPrimo p
    | p <= 1 = False 
    | menorDivisor p == p = True
    | otherwise = False
    
-- c) Implementar la función sonCoprimos :: Integer -> Integer -> Bool que dados dos números naturales indica si no tienen algún divisor en común mayor estricto que 1.

sonCoprimos :: Integer -> Integer -> Bool 
sonCoprimos n m
    | n == m    = False -- (Excepto si ambos son 1, ojo con ese caso límite)
    | otherwise = buscarDivisorComun n m 2

buscarDivisorComun :: Integer -> Integer -> Integer -> Bool
buscarDivisorComun n m d
    |d>n || d>m = True  -- ¿Cuál es el límite donde d ya es demasiado grande y devuelves True?
    | n `mod` d == 0 && m `mod` d == 0 = False -- ¿Qué condición matemática con 'mod' debe cumplir d para que devuelvas False?
    | otherwise = buscarDivisorComun n m (d + 1)

-- d) Implementar la función nEsimoPrimo :: Integer -> Integer

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n
  | n <= 0    = error "n debe ser mayor o igual a 1"
  | otherwise = buscarPrimo n 2
  where
    buscarPrimo :: Integer -> Integer -> Integer
    buscarPrimo faltantes candidato
      | esPrimo candidato && faltantes == 1 = candidato
      | esPrimo candidato                   = buscarPrimo (faltantes - 1) (candidato + 1)
      | otherwise                           = buscarPrimo faltantes (candidato + 1)


