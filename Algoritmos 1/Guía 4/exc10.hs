{--
Ejercicio 10. Especificar, implementar y dar el tipo de las siguientes funciones (símil Ejercicio 4 Práctica 2 de Álgebra 1).--}

-- a) f1(n) = Σ (i = 0 hasta n) 2^i, n ∈ N0.
f1 :: Integer -> Integer
f1 0 = 1 
f1 n 
    | n > 0 = 2^n + f1(n-1) --puedo sacar esos paréntesis, pero meh
    | otherwise = error "Parámetros inválidos"

-- b) f2(n, q) = Σ (i = 1 hasta n) q^i, n ∈ N y q ∈ R.

f2 :: Integer -> Float -> Float
f2 1 q = q
f2 n q 
    | n > 1 = q^(n) + f2 (n-1) q
    | otherwise = error "Solo naturales"

-- c) f3(n, q) = Σ (i = 1 hasta 2n) q^i, n ∈ N0 y q ∈ R.

-- Reutiliza la lógica de f3 :: Integer -> Float -> Float
f3 :: Integer -> Float -> Float
f3 n q 
    | n >= 0    = f3_aux (2 * n) q
    | otherwise = error "Parámetros inválidos"

-- Función auxiliar idéntica a f2 pero que contempla el caso base 0
f3_aux :: Integer -> Float -> Float
f3_aux 0 q = 0
f3_aux m q = q^m + f3_aux (m - 1) q


-- d) f4(n, q) = Σ (i = n hasta 2n) q^i, n ∈ N0 y q ∈ R.

-- Creo una función que reciba n y q y que evalúe si n es mayor o igual a 0, y en caso de serlo, llame a una función auxiliar que reciba m = 2n, n y q. 
f4 :: Integer -> Float -> Float
f4 n q
    | n >= 0 = f4_aux (2*n) n q 
    | otherwise = error "Parámetros inválidos"

-- Creo esta función auxiliar con el fin de correctamente restar 1 a m hasta que sea igual a n, y en cada iteración sumar q^m al resultado de la llamada recursiva. En caso de que m sea igual a n, simplemente devuelvo q^n.
f4_aux ::  Integer -> Integer -> Float -> Float
f4_aux m n q 
    | m == n = q^n
    | otherwise = q^m + f4_aux (m-1) n q

