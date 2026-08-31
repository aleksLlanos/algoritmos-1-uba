#EL EJERCICIO 9 ES SOLO UN DATO

"""Ejercicio 10. ⋆ Sean las variables proposicionales f, e y m con los siguientes significados:
f ≡“es fin de semana” e ≡“Juan estudia” m ≡“Juan escucha mÚsica”
a) Escribir usando lÓgica proposicional las siguientes oraciones:
1. “Si es fin de semana, Juan estudia o escucha mÚsica, pero no ambas cosas”
2. “Si no es fin de semana entonces Juan no estudia”
3. “Cuando Juan estudia los fines de semana, lo hace escuchando mÚsica”

RESPUESTA A):
1. Si F entonces (o E o M). pero la disyunción estricta es:((E or M) and not(E and M)). Mejorándolo tenemos: not F or ((E or M) and not(E and M))

2. Si not F entonces not E. Es lo mismo que "E entonces F". Con lógica sería: F or not e

3. (E and F) entonces m. Con lógica: not(E and F) or m.

b) Asumiendo que valen las tres proposiciones anteriores, ¿se puede deducir que Juan no estudia? Justificar usando Lógica
Proposicional.

RESPUESTA: Sí. Sé puede deducir que E y F son ambas falsas, indeoendientemente de la semántica de M. En 1. me quedó una implicación con F como consecuente. Para que sea cierta siempre, F=False. Esto hace que para que 2. sera cierta, E=False. Estos 2 valores cumplenla última también, porque queda un antecedente que solo es falso si ambas son falsas, lo cual ya planteamos.

CORRECCIÓN: La respuesta está bien pero la justificación mal. Si planteamos que SÍ ESTUDIA, habrá contradicción, entonces NO estudia. Si hay dudas, fijate vo papu, pero ya lo comprobé en una hojita q seguro ya tiré"""

