import System.Win32 (COORD(yPos))
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

{--
e) ambosSonCero: dados dos números racionales, decide si ambos son iguales a 0 (resolverlo con y sin pattern matching).
--}

{--
f) enMismoIntervalo: dados dos números reales, indica si están relacionados por la relación de equivalencia en R cuyas clases de equivalencia son: (-∞, 3], (3, 7] y (7, ∞), o dicho de otra manera, si pertenecen al mismo intervalo.
--}

{--
g) sumaDistintos: que dados tres números enteros calcule la suma sin sumar repetidos (si los hubiera).
--}

{--
h) esMultiploDe: dados dos números naturales, decide si el primero es múltiplo del segundo.
--}

{--
i) digitoUnidades: dado un número entero, extrae su dígito de las unidades.
--}

{--
j) digitoDecenas: dado un número entero mayor a 9, extrae su dígito de las decenas.
--}