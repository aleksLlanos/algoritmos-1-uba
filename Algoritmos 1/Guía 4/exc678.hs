{--
Ejercicio 6. Implementar la función todosDigitosIguales :: Integer -> Bool que determina si todos los dígitos de un número natural son iguales, es decir:

problema todosDigitosIguales (n: Z) : B {
    requiere: {n > 0}
    asegura: {resultado = true ↔ todos los dígitos de n son iguales}
}
--}


--Si n es negativo, la función devuelve un error indicando que n debe ser un número natural. Si n es igual a 0, la función devuelve True, ya que todos los dígitos de 0 son iguales. En caso contrario, se llama a la función auxiliar todosDigitosIgualesAux con el número n y el último dígito de n (obtenido mediante n `mod` 10) como parámetros.

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 0 = error "n debe ser un número natural"
                       | n == 0 = True
                       | otherwise = todosDigitosIgualesAux n (n `mod` 10)

-- Función auxiliar que verifica si todos los dígitos de un número son iguales a un dígito dado, en este caso se va comparando el último digito de n con el último del nuevo dígito que es igual a n sin el último dígito (obtenido mediante n `div` 10). Si el último dígito de n es diferente al dígito dado, la función devuelve False. Si n es igual a 0, significa que se han comparado todos los dígitos y son iguales, por lo que devuelve True. En caso contrario, se llama recursivamente a la función con n sin el último dígito y el mismo dígito dado.
todosDigitosIgualesAux :: Integer -> Integer -> Bool
todosDigitosIgualesAux n d | n == 0 = True
                           | n `mod` 10 /= d = False
                           | otherwise = todosDigitosIgualesAux (n `div` 10) d


{--
Ejercicio 7. Implementar la función iesimoDigito :: Integer -> Integer -> Integer que dado un n ∈ Z mayor o igual a 0 y un i ∈ Z mayor o igual a 1 y menor o igual a la cantidad de dígitos de n, devuelve el i-ésimo dígito de n.

problema iesimoDigito (n: Z, i: Z) : Z {
    requiere: { n ≥ 0 ∧ 1 ≤ i ≤ cantDigitos(n) }
    asegura: { resultado = (n div 10^(cantDigitos(n) − i)) mod 10 }
}

problema cantDigitos (n: Z) : N {
    requiere: { n ≥ 0 }
    asegura: { n = 0 → resultado = 1 }
    asegura: { n ≠ 0 → (n div 10^(resultado − 1) > 0 ∧ n div 10^resultado = 0) }
}
--}

--Este fue mi mayor reto. Pensé en una función que vaya sumando 1 a un contador mientras el número n sea mayor que 0, y en cada iteración se divide de forma enter n entre 10, hasta que n sea igual a 0. En ese momento, el contador tendrá el valor de la cantidad de digitos de n. Si n es negativo, la función devuelve un error indicando que n debe ser mayor o igual a 0. Si n es menor que 10, significa que tiene un solo dígito, por lo que devuelve 1. En caso contrario, se llama recursivamente a la función con n dividido entre 10 y se suma 1 al resultado. 
cantDigitos :: Integer -> Integer
cantDigitos n
    | n < 0 = error "n debe ser mayor o igual a 0"
    | n < 10 = 1
    | otherwise = 1 + cantDigitos (n `div` 10)

  
--Para esta función iesimoDigito, primero se verifica que n sea mayor que 0 y que i esté dentro del rango válido (1 ≤ i ≤ cantDigitos n). Si no se cumplen estas condiciones, la función devuelve un error indicando que los parámetros son inválidos. En caso contrario, se calcula el i-ésimo dígito de n utilizando la fórmula proporcionada en el enunciado: (n `div` (10 ^ (cantDigitos n - i))) `mod` 10.
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i 
    | n > 0 && (1 <= i && i <= cantDigitos n) = (n `div` (10 ^ (cantDigitos n - i))) `mod` 10
    | otherwise = error "Parámetros inválidos"