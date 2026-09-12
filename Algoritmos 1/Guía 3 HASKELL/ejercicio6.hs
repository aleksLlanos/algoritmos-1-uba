import Distribution.Simple.Utils (xargs)
{--
Ejercicio 6. Usando los siguientes tipos:
--}

{--
type Anio = Integer
type EsBisiesto = Bool
--}


{--
Programar la función bisiesto :: Anio -> EsBisiesto según la siguiente especificación:

problema bisiesto (año : Z) : Bool {
    requiere: {True}
    asegura: {(res = false) ↔ (año no es múltiplo de 4, o bien, año es múltiplo de 100 pero no de 400)}
}

Por ejemplo:
bisiesto 1901 ⇝ False    bisiesto 1904 ⇝ True
bisiesto 1900 ⇝ False    bisiesto 2000 ⇝ True
--}
type Anio = Int
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto anio
    | anio `mod` 4 /= 0 = False
    | anio `mod` 100 == 0 && anio `mod` 400 /= 0 = False
    | otherwise = True


