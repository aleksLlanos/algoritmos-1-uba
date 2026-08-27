#Ejercicio 2. ⋆ Determinar el valor de verdad de las siguientes f´ormulas
"""
1 Cuando el valor de verdad de a, b y c es verdadero, mientras que el de x e y es falso.

a) (¬a ∨ b)
b) (c ∨ (y ∧ x) ∨ b)
c) ¬(c ∨ y)
d) (¬(c ∨ y) ↔ (¬c ∧ ¬y))
e) ((c ∨ y) ∧ (x ∨ b))
f) (((c ∨ y) ∧ (x ∨ b)) ↔ (c ∨ (y ∧ x) ∨ b))
g) (¬c ∧ ¬y)

2 Cuando el valor de verdad de a, b y c es falso, mientras que el de x e y es verdadero.

a) (¬a ∨ b)
b) (c ∨ (y ∧ x) ∨ b)
c) ¬(c ∨ y)
d) (¬(c ∨ y) ↔ (¬c ∧ ¬y))
e) ((c ∨ y) ∧ (x ∨ b))
f) (((c ∨ y) ∧ (x ∨ b)) ↔ (c ∨ (y ∧ x) ∨ b))
g) (¬c ∧ ¬y)
"""

#tabltia de verdad para el ejercicio 2
def tabla_de_verdad(a, b, c, x, y):
    # Evaluar cada expresión lógica
    a1 = (not a or b)
    a2 = (c or (y and x) or b)
    a3 = not (c or y)
    a4 = (not (c or y)) == (not c and not y)
    a5 = ((c or y) and (x or b))
    a6 = (((c or y) and (x or b)) == (c or (y and x) or b))
    a7 = (not c and not y)

    # Imprimir los resultados
    print(f"a) {a1}")
    print(f"b) {a2}")
    print(f"c) {a3}")
    print(f"d) {a4}")
    print(f"e) {a5}")
    print(f"f) {a6}")
    print(f"g) {a7}")

#Primer caso.
a,b,c= True, True, True
x,y= False, False
tabla_de_verdad(a, b, c, x, y)

print("\n")  # Salto de línea para separar los casos.
#Segundo caso.
a,b,c= False, False, False
x,y= True, True
tabla_de_verdad(a, b, c, x, y)


