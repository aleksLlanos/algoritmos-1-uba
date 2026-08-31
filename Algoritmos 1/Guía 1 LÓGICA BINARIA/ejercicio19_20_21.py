"""Ejercicio 19. Sean p, q y r tres variables de las que se sabe que:

. P y Q nunca están indefinidas,
. R se indefine si q es verdadera.

Proponer, para cada ítem, una fórmula que nunca se indefina, utilizando siempre las tres variables. Cada fórmula debe
ser verdadera si y solo sí se cumple que:

a) Al menos una es verdadera. # (P or_L Q) or_L R
b) Ninguna es verdadera. # [(not P) or_L (not Q) or_L (not R)]
c) Exactamente una de las tres es verdadera.
d) Sólo p y q son verdaderas. {[not(P or_estricto Q) and Q] and_L (Q or_L R)}
e) No todas al mismo tiempo son verdaderas.
f) r es verdadera.

UNA PAJA, NO VOLVER A HACER, NO TIENEN MUCHO SENTIDO"""

"""Ejercicio 20. Sean x, y ∈ Z y z una variable proposicional, indique cuáles de las siguientes expresiones, en nuestro lenguaje de especificación, están bien formadas.
a) ((1 = 0) ∨ (x = y)) #CORRECTA
b) (x + 10) = yc) (x ∨ y) #INCORRECTA, no se pueden comparar números con proposiciones.
d) (z ↔ True) ↔ (y = x) #CORRECTA, ya que z es una variable proposicional y True también. El resultado de esa comparación es una proposición, que puede compararse con otra proposición.
e) (z = 0) ∨ (z = 1) #INCORRECTA, se igualan proposiciones y números. 
f) y + (y < 0) #mal, compara números con proposiciones""" 

"""Ejercicio 21. La fórmula ((3 + 7 = π - 8) ∧ T rue) es una fórmula bien formada. ¿Por qué? Justifique su respuesta.

Respuesta: ES UNA FÓRMULA BIEN FORMADA PORQUE IGUALAR NÚMEROS RESULTA EN UNA PROPOSICIÓN CON VALOR BOOLEANO, LUEGO SE LO CONJUGA CON OTRO BOOLEANO, TRUE. Pero, si se quisiera evaluar la fórmula, el resultado sería FALSO, ya que 3 + 7 = 10 y π - 8 ≈ -4.858407346410207, por lo que la igualdad es falsa."""
