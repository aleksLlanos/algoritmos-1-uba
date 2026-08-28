"""Ejercicio 8. ⋆ Usando las reglas de equivalencia determinar si los siguientes pares de fórmulas son equivalentes. Indicar en
cada paso qué regla se utilizó.
a) ((p ∧ p) ∧ p) → p
T rue
#EQUIVALENTES

b) ((¬p ∨ ¬q) ∨ (p ∧ q)) → (p ∧ q)
(p ∧ q)
#NO SON EQUIVALENTES. LA PRIMERA EXPRESIÓN ES IGUAL A: (not(p and q))


c) (p ∨ q) ∧ (p ∨ r)
(¬p → (q ∧ r))
#EQUIVALENTES. Transformé la segunda expresión.

d) ¬(¬p) → (¬(¬p ∧ ¬q))
q
#NO SON EQUIVALENTES. LA PRIMERA EXPRESIÓN ES TAUTOLOGÍA

e) ((T rue ∧ p) ∧ (¬p ∨ F alse)) → ¬(¬p ∨ q)
(p ∧ ¬q)
#NO SON EQUIVALENTES. LA PRIMERA EXPRESIÓN ES TAUTOLOGÍA


f) (p ∨ (¬p ∧ q))
(¬p → q)
#EQUIVALENTES

g) ¬(p ∧ (q ∧ s))
(s → (¬p ∨ ¬q))
#EQUIVALENTES

h) (p → (q ∧ ¬(q → r)))
((¬p ∨ q) ∧ (¬p ∨ (q ∧ ¬r)))
#EQUIVALENTES
"""
