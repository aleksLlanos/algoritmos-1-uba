#Ejercicio 3. Determinar, utilizando tablas de verdad, si las siguientes f´ormulas son tautolog´ıas, contradicciones o contingencias.
"""
a) (p ∨ ¬p)
b) (p ∧ ¬p)
c) ((¬p ∨ q) ↔ (p → q))

d) ((p ∨ q) → p)
e) (¬(p ∧ q) ↔ (¬p ∨ ¬q))
f) ((¬p ∧ q) ↔ (¬p ∨ ¬q))
g) (p → p)
h) ((p ∧ q) → p)
i) ((p ∧ (q ∨ r)) ↔ ((p ∧ q) ∨ (p ∧ r)))
j) ((p → (q → r)) → ((p → q) → (p → r)))"""

def nueva_tabla_de_verdad(p,q,r):
    # Evaluar cada expresión lógica
    a = (p or not p)
    b = (p and not p)
    c = ((not p or q) == (not p or q))
    d = ((not (p or q))or p)
    e = (not (p and q)) == (not p or not q)
    f = ((not p and q) == (not p or not q))
    g = (not p or p)
    h = ((not (p and q)) or p)
    i = ((p and (q or r)) == ((p and q) or (p and r)))
    j = ( not(not p or (not q or r)) ) or (not(not p or q) or (not p or r))
    

    # Imprimir los resultados
    lista_resultados = [a, b, c, d, e, f, g, h, i, j]
    return lista_resultados

lista_resultado1 = [nueva_tabla_de_verdad(p,q,r) for p in (True,False) for q in (True,False) for r in (True, False)]

"""
lista_resultado2 = [
    nueva_tabla_de_verdad(True, True, True),
    nueva_tabla_de_verdad(True, True, False),
    nueva_tabla_de_verdad(True, False, True),
    nueva_tabla_de_verdad(True, False, False),
    nueva_tabla_de_verdad(False, True, True),
    nueva_tabla_de_verdad(False, True, False),
    nueva_tabla_de_verdad(False, False, True),
    nueva_tabla_de_verdad(False, False, False)
]"""

def guardo_resultados(lista_resultados):
    lista_por_columna = list(zip(*lista_resultados))
    """
        lista_a = [a[0] for a in lista_resultados]
        lista_b = [b[1] for b in lista_resultados]
        lista_c = [c[2] for c in lista_resultados]
        lista_d = [d[3] for d in lista_resultados]
        lista_e = [e[4] for e in lista_resultados]
        lista_f = [f[5] for f in lista_resultados]
        lista_g = [g[6] for g in lista_resultados]
        lista_h = [h[7] for h in lista_resultados]
        lista_i = [i[8] for i in lista_resultados]
        lista_j = [j[9] for j in lista_resultados]
        return lista_a, lista_b, lista_c, lista_d, lista_e, lista_f, lista_g, lista_h, lista_i, lista_j
        """
    return lista_por_columna

def analizo_resultados(lista_por_columna):
    resultados = []
    for columna in lista_por_columna:
        if all(columna):
            resultados.append("Tautología")
        elif not any(columna):
            resultados.append("Contradicción")
        else:
            resultados.append("Contingencia")
    return resultados


print(analizo_resultados(guardo_resultados(lista_resultado1)))