"""Ejercicio 4. ⋆ Dadas las proposiciones lógicas α y β, se dice que α es más fuerte que β si y sólo si α → β es una tautología.
En este caso, también decimos que β es más débil que α. Determinar la relación de fuerza de los siguientes pares de fórmulas:
a) True, False  

# False es más fuerte que True, ya que False → True es una tautología. De hecho, False es la proposición más fuerte que existe, ya que False → α es una tautología para cualquier α.

b) (p ∧ q), (p ∨ q)

# Para que ocurra la primera, ambas deben cumplirse y nada más. Para que ocurra la segunda, pueden se ambas o solo una. Es menos restrictiva. Si planteamos la implicación tenemos

def defino_la_verdad (p,q): 
    return not (p and q) or (p or q)

print(list(defino_la_verdad(p,q) for p in (True,False) for q in (True,False)))

c) True, True

#Se podría decir que ambas son más fuertes que la otra y por ende iguales.

d) p, (p ∧ q)

#La segunda es más fuerte, requiere de más condiciones para cumplirse. La implicación lo abala

e) False, False

#iguales o una más fuerte q la otra

f) p, (p ∨ q)

#La segunda es más fuerte porque es igual que la primera, pero encima puede ser verdadera incluso si la primera es falsa. La implicación lo abala


g) p, q

#iguales

h) p, (p → q) 

#la implicación no abala nada, entonces no hay relación de fuerza."""




def defino_la_verdad (p,q): 
    return not (not p or q) or p
#la implicación lo abala
print(list(defino_la_verdad(p,q) for p in (True,False) for q in (True,False)))

