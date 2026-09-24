type Serie = ([Char], Integer)     -- (nombre de la serie, cantidad de temporadas)
type Grupo = (Integer, [[Char]])   -- (cantidad de temporadas, nombres de series con esa cantidad)
 
agruparPorCantidadDeTemporadas :: [Serie] -> [Grupo]
agruparPorCantidadDeTemporadas [] = []
agruparPorCantidadDeTemporadas ((nombre, temporadas) : xs) =
    insertarEnGrupos nombre temporadas (agruparPorCantidadDeTemporadas xs)
 
insertarEnGrupos :: [Char] -> Integer -> [Grupo] -> [Grupo]
insertarEnGrupos nombre temporadas [] = [(temporadas, [nombre])]
insertarEnGrupos nombre temporadas ((t, series) : xs)
    | temporadas == t = (t, nombre : series) : xs
    | otherwise        = (t, series) : insertarEnGrupos nombre temporadas xs
 
sumaCuadradosPares :: Int -> Int
sumaCuadradosPares 1 = 0
sumaCuadradosPares n
    | esPar n   = n*n + sumaCuadradosPares (n-1)
    | otherwise = sumaCuadradosPares (n-1)
 
esPar :: Int -> Bool
esPar n = mod n 2 == 0
