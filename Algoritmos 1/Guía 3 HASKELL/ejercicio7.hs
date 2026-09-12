{--
Ejercicio 7.

a) Implementar la función:
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float

problema distanciaManhattan (p : R × R × R, q : R × R × R) : R {
    requiere: {True}
    asegura: {res = Σ_{i=0}^{2} |p_i − q_i|}
}

Por ejemplo:
distanciaManhattan (2, 3, 4) (7, 3, 8) ⇝ 9
distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4)) ⇝ 12.8
--}

distanciaManhattan ::(Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x1, y1, z1) (x2, y2, z2) = (abs (x1 - x2)) + (abs (y1 - y2)) + (abs (z1 - z2))

{--
b) Reimplementar la función teniendo en cuenta el siguiente tipo: type Punto3D = (Float, Float, Float)
--}

type Punto3D = (Float, Float, Float)

distanciaManhattanPunto3D :: Punto3D -> Punto3D -> Float
distanciaManhattanPunto3D (x1, y1, z1) (x2, y2, z2) = (abs (x1 - x2)) + (abs (y1 - y2)) + (abs (z1 - z2))