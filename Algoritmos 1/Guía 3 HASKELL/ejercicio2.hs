import Data.Time.Format.ISO8601 (yearFormat)
import GHC.Internal.Natural (Natural)
{--
Ejercicio 2. Especificar e implementar las siguientes funciones, incluyendo su signatura.
--}

{--
a) absoluto: calcula el valor absoluto de un número entero.
--}
valorAbsoluto :: Integer -> Integer
valorAbsoluto x
  | x >= 0    = x
  | otherwise = -x

{--
b) maximoAbsoluto: devuelve el máximo entre el valor absoluto de dos números enteros.
--}
maxValAbs2 :: Integer -> Integer -> Integer
maxValAbs2 x y
  | valorAbsoluto x >= valorAbsoluto y = valorAbsoluto x
  | otherwise                           = valorAbsoluto y

{--
c) maximo3: devuelve el máximo entre tres números enteros.
--}

maxValAbs3 :: Integer -> Integer -> Integer -> Integer {--f:(ZxZxZ) -> Z--}
maxValAbs3 x y z  {--f(x,y,z)--}
  | maxValAbs2 x y >= valorAbsoluto z = maxValAbs2 x y {--g(x,y,z)--}
  | otherwise                         = valorAbsoluto z   

{--
d) algunoEsCero: dados dos números racionales, decide si alguno es igual a 0 (resolverlo con y sin pattern matching).
--}

{--Sin pattern matching--}
algunoEsCero :: Float -> Float -> Float
algunoEsCero  x y 
  | x == 0 = 1
  | y == 0 = 1
  | otherwise = 0

{--Con pattern Matching--}
algunoEsCero' :: Float -> Float -> Integer
algunoEsCero' 0 _ = 1 {--Acá decimos "si el primer argumento es 0, sin importar el segundo, entonces devolvemos 1"--}
algunoEsCero' _ 0 = 1 {--Acá decimos "si el segundo argumento es 0, sin importar el primero, entonces devolvemos 1"--}
algunoEsCero' _ _ = 0 {--Si la primera y la segunda condición no se cumplen, sin importar los argumentos, entonces devolvemos 0"--}

{--
e) ambosSonCero: dados dos números racionales, decide si ambos son iguales a 0 (resolverlo con y sin pattern matching).
--}

ambosSonCero :: Float -> Float -> Integer
ambosSonCero x y
  | x==0 && y==0 = 1
  | otherwise = 0

ambosSonCero' :: Float -> Float -> Integer
ambosSonCero' 0 0 = 1
ambosSonCero' _ _ = 0 

{--
f) enMismoIntervalo: dados dos números reales, indica si están relacionados por la relación de equivalencia en R cuyas clases de equivalencia son: (-∞, 3], (3, 7] y (7, ∞), o dicho de otra manera, si pertenecen al mismo intervalo.
--}

enMismoIntervalo :: Float -> Float -> Float
enMismoIntervalo x y
  | (x <= 3 && y <= 3) || (x > 3 && x <= 7 && y > 3 && y <= 7) || (x > 7 && y > 7) = 1
  | otherwise = 0

{--
g) sumaDistintos: que dados tres números enteros calcule la suma sin sumar repetidos (si los hubiera).
--}

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z 
  | x /= y && y /= z && x/=z = x+y+z
  | otherwise = 0

{--
h) esMultiploDe: dados dos números naturales, decide si el primero es múltiplo del segundo.
--}

esMultiploDe :: Natural -> Natural -> Bool
esMultiploDe x y
  | y == 0         = False  -- Evita la división por cero si x es múltiplo de 0
  | x `mod` y == 0 = True -- 'mod' devuelve el resto de la división de x entre y. Si el resto es 0, entonces x es múltiplo de y.
  | otherwise      = False

{--
i) digitoUnidades: dado un número entero, extrae su dígito de las unidades.
--}

digitoUnidades :: Integer -> Integer
digitoUnidades x = valorAbsoluto (x `mod` 10) -- `mod` devuelve el resto de la división de x entre 10

{--
j) digitoDecenas: dado un número entero mayor a 9, extrae su dígito de las decenas.
--}

digitoDecenas :: Integer ->Integer
digitoDecenas x
  | x > 9     = valorAbsoluto ((x `div` 10) `mod` 10) -- `div` devuelve el cociente de la división entera de x entre 10, y luego `mod` obtiene el dígito de las decenas.
  | otherwise = error "el número debe ser mayor a 9"


