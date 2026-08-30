"""Ejercicio 11. En la salita verde de un jard´ın se sabe que las siguientes circunstancias son ciertas:
a) Si todos conocen a Juan entonces todos conocen a Camila (podemos suponer debido a que siempre caminan juntos).
b) Si todos conocen a Juan, entonces que todos conozcan a Camila implica que todos conocen a Gonzalo.
La pregunta que queremos responder entonces es: ¿es cierto que si todos conocen a Juan entonces todos conocen a Gonzalo?
Resolver utilizando L´ogica Proposicional.

RESPUESTA: Llamo p='todos conocen a Juan', q='todos conocen a Camila', r='todos conocen a Gonzalo'.
De esta forma
a)P entonces Q
b)(P entonces Q) entonces R
Ver: si P entonces Q
Utilizo una demostración por contradicción. Si asumimos que "Ver:" no es cierto y que a) y b) son ciertas, entonces podemos sacar que P=True y R=False. Si P=True entonces de a) deducimos que Q=True. De b) tenemos "True entonces R" pero en este caso R sería false por lo que asumimos al inicio y esta implicación sería falsa, cuando partimos de que es verdadera, entonces hay contradicción. "Ver:" no puede ser falsa, debe ser verdadera.
"""

"""Ejercicio 12. Siempre que Laly y Leo duermen en lo de su abuela, vuelven a su casa con un paquete de galletitas. Si un
d´ıa los vi´eramos llegar con el paquete de galletitas, podr´ıamos sentirnos inclinados a concluir que han dormido en lo de su
abuela. ¿Puede identificar el error en el razonamiento anterior? Pista: Es conocido como falacia de afirmar el consecuente.

LO DICE EL NOMBRE, FALACIA DE CONFIRMACIÓN DEL CONSECUENTE."""
