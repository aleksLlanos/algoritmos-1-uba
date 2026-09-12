--import Distribution.Simple.Utils (xargs)
--import Distribution.Simple.Utils (xargs)

{--
Ejercicio 5. Implementar la función todosMenores :: (Integer, Integer, Integer) -> Bool
--}

{--
problema f (n : Z) : Z {
    requiere: {True}
    asegura: {(n ≤ 7 → res = n^2) ∧ (n > 7 → res = 2n − 1)}
}
--}

f :: Int -> Int
f x
  | x<=7 = x*x
  | otherwise = 2*x-1


{--
problema g (n : Z) : Z {
    requiere: {True}
    asegura: {Si n es un número par entonces res = n/2, en caso contrario, res = 3n + 1}
}
--}

g :: Int -> Int
g x
  | x `mod` 2 == 0 = x `div` 2
  | otherwise = 3*x+1

{--
problema todosMenores (t : Z × Z × Z) : Bool {
    requiere: {True}
    asegura: {(res = true) ↔ ((f(t0) > g(t0)) ∧ (f(t1) > g(t1)) ∧ (f(t2) > g(t2)))}
}
--}

todosMenores :: (Int, Int, Int) -> Bool 
todosMenores (x, y, z) = f x > g x && f y > g y && f z > g z

