{- Ejercicio 9. A partir de las siguientes implementaciones en Haskell, describir en lenguaje natural qué hacen y especificarlas. -}

{- a) -}
f1 :: Float -> Float
f1 n | n == 0    = 1
     | otherwise = 0
 
{--
La función f1 recibe un número real n y devuelve 1 si n es igual a 0, y devuelve 0 en cualquier otro caso.
Especificación:
problema f1 (n : R) : R {
    requiere: {True}
    asegura: {(res = 1) ↔ (n = 0)}
    asegura: {(res = 0) ↔ (n ≠ 0)}
--}


{- b) -}
f2 :: Float -> Float
f2 n | n == 1  = 15
     | n == -1 = -15
     | otherwise = error "Valor no permitido"

{--
La función f2 recibe un real n y devuelve 15 si el real es 1 o devuelve -15 si el real es -1
problema f2 (n : R) : R {
    requiere: {True}
    asegura: {(res = 15) ↔ (n = 1)}
    asegura: {(res = -15) ↔  (n = -1)}
}
--}

{- c) -}
f3 :: Float -> Float
f3 n | n <= 9 = 7
     | n >= 9 = 5 -- es lo mismo que n >= 3, ya que si n <= 9 y n >= 3 hay un rango de valores que cumplen ambas condiciones pero solo se cumple la primera, sin leer la segunda.

{--
La función f3 recibe un número real n y devuelve 7 si n es menor o igual a 9, y devuelve 5 si n es mayor o igual a 3.
problema f3 (n : R) : R {
    requiere: {True}
    asegura: {(res = 7) ↔ (n<=9)}
    asegura: {(res = 5) ↔ (n>=3)}

}
--}

{- d) -}
f4 :: Float -> Float -> Float
f4 x y = (x + y)/2

{--
La función f4 recibe dos números reales x e y y devuelve el promedio de ambos.
problema f4 (x : R, y : R) : R {
    requiere: {True}
    asegura: {res = (x + y)/2}
}
--}

{- e) -}
f5 :: (Float, Float) -> Float
f5 (x, y) = (x + y)/2

{--
La función f5 recibe una tupla de dos números reales (x, y) y devuelve el promedio de ambos.
problema f5 (x : R, y : R) : R {
    requiere: {True}
    asegura: {res = (x + y)/2}
}
--}

{- f) -}
f6 :: Float -> Int -> Bool
f6 a b = truncate a == b

{--
La función f6 recibe un número real a y un número entero b, y devuelve True si la parte entera de a es igual a b, y devuelve False en caso contrario.
problema f6 (a : R, b : Z) : B {
    requiere: {True}
    asegura: {(res = True) ↔ (truncate a = b)}
    asegura: {(res = False) ↔ (truncate a ≠ b)}
}
--}