--NOTAS DE COSAS INTERESANTES QUE ESTUVE NOTANDO A MEDIDA QUE IBA RESOLVIENDO ESTE EJERCICIO:
--  " Ctrl + ñ + Ctrl + , " para abrir una nueva terminar en bash. 
--  debo escribir "copilot" en esta nueva terminal para usar Copilot CLI (aprender a usar)
--  Usar el comando "cd [directorio]" en la terminal para llegar al directorio que tiene los .hs de interés.
--  escribir "ghci" en la terminal para activar el intérprete de Haskell
--  escribir ":quit" para salir del intérprete.
--  :l ['nombre del archivo'.hs]
--  :r para recargar un archivo que ya había sido interpretado, usar luego de modificar un .hs y antes de ejecutar.
--  escribir en la terminal la siguiente sintaxis:"nombre_de_la_función argumento"

{--Ejercicio 1.

a) Implementar la función parcial f :: Integer -> Integer definida por extensión de la siguiente manera:

    f(1) = 8
    f(4) = 131
    f(16) = 16

    y cuya especificación es:

    problema f (n : Z) : Z {
        requiere: {n = 1 ∨ n = 4 ∨ n = 16}
        asegura: {(n = 1 → res = 8) ∧ (n = 4 → res = 131) ∧ (n = 16 → res = 16)}
    }--}

f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

{-- 
b) Análogamente, especificar e implementar la función parcial g :: Integer -> Integer

    g(8) = 16
    g(16) = 4
    g(131) = 1
--}

g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1


{-- 
c) A partir de las funciones definidas en los ítems a) y b), implementar las funciones parciales h = f ◦ g y k = g ◦ f

"""--}

{-- h :: Integer -> Integer
h 131 = 8
h 16 = 131
h 8 = 16

k :: Integer -> Integer 
k 1 = 16
k 16 = 4
k 4 = 1 --}

h :: Integer -> Integer
h = f . g

k :: Integer -> Integer
k = g . f



--NOTAS DE COSAS INTERESANTES QUE ESTUVE NOTANDO A MEDIDA QUE IBA RESOLVIENDO ESTE EJERCICIO:
--  " Ctrl + ñ + Ctrl + , " para abrir una nueva terminar en bash. 
--  debo escribir "copilot" en esta nueva terminal para usar Copilot CLI (aprender a usar)
--  Usar el comando "cd [directorio]" en la terminal para llegar al directorio que tiene los .hs de interés.
--  escribir "ghci" en la terminal para activar el intérprete de Haskell
--  escribir ":quit" para salir del intérprete.
--  :l ['nombre del archivo'.hs]
--  :r para recargar un archivo que ya había sido interpretado, usar luego de modificar un .hs y antes de ejecutar.
--  escribir en la terminal la siguiente sintaxis:"nombre_de_la_función argumento"
