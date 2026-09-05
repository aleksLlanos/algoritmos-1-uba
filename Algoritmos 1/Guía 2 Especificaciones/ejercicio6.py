"""Ejercicio 6. (Control de Calificaciones en el Departamento de Ciencias)

En el prestigioso Departamento de Ciencias de una reconocida universidad, un grupo de estudiantes se ha embarcado en su jornada académica, cursando diversas materias bajo el cuidadoso seguimiento del cuerpo docente. En este departamento, cada estudiante ha sido registrado con su respectivo nombre y apellido, asegurándose de que no existan duplicados.

La información relevante de las cursadas de los estudiantes se encuentra almacenada en un sistema que contiene una secuencia de tuplas en formato Materia × Calificación obtenida. Las calificaciones se encuentran en un rango numérico entre 0 y 10.

El Departamento ha establecido una política de aprobación y recursado que dicta que si un estudiante aprueba una materia con una calificación igual o superior a 4, no deberá volver a cursarla, quedando esta materia registrada como aprobada en su expediente académico. Sin embargo, si no logra alcanzar la calificación mínima de aprobación, tendrá la posibilidad de recursar la materia en un futuro intento.

Además, existe en el sistema una estructura de datos llamada CalificacionesDelDC que contiene la información de los estudiantes y las calificaciones en sus cursadas. Esta estructura es una secuencia de tuplas en el formato Alumno × Cursada, donde Alumno es el nombre y apellido del estudiante y Cursada es la secuencia de tuplas mencionada previamente.

Considerando esta información y los siguientes renombres de tipos:

    Renombre Alumno = String
    Renombre Materia = String
    Renombre Cursada = seq⟨Materia × R⟩
    Renombre CalificacionesDelDC = seq⟨Alumno × Cursada⟩

a) Especificar problema promedioDeAlumno (alumno: Alumno, calificaciones: CalificacionesDelDC) : R

#RESPUESTA:
-   Ejemplo de información de un estudiante registrado: (Alexander Llanos, Alexander Llanoz, Priscilla Choque) #no son duplicados
-   Ejemplo de CURSADA: [(Análisis Matemático, 10) , (Física, 6) , (ICSE, 8)] 
-   Ejemplo de CalificacionesDelDC: [
    (Alexander Llanos, [(Análisis Matemático, 10) , (Física, 6) , (ICSE, 8)]),
    (Priscilla Choque, [(Análisis Matemático, 9) , (Física, 9) , (ICSE, 7)])]

problema promedioDeAlumno (alumno: Alumno, calificaciones: CalificacionesDelDC) : R
    requiere: {Existe algún elemento en CalificacionesDelDC cuya primer componente sea igual que Alumno}
    requiere: {El elemento mínimamente existente requerido anteriormente, debe tener como primer elemento de la secuencia a alguna materia }
    asegura: {resultado es el promedio de notas asociadas que Alumno tiene según CalificacionesDelDC}


b) Especificar el problema que, dado el listado de materias cursadas por un estudiante, indique en qué materia tuvo mayor calificación. ¿Cómo se debe modificar la especificación para devolver el listado de materias en las cuales tuvo mejor calificación?

problema materiaMejorCalificada (cursadas: Cursada) : Materia
    requiere: {cursadas no es vacía}
    asegura: {resultado es el primer elemento de la tupla cuyo segundo elemento es mayor o igual a todoes los segundos elementos de las tuplas en cursadas}     


#Para devolver el listado de materias en las cuales tuvo mejor calificación, se puede modificar la especificación de la siguiente manera:

problema materiasMejorCalificadas (cursadas: Cursada) : seq⟨Materia⟩
    requiere: {cursadas no es vacía}  
    asegura: {resultado es la secuencia de primer/os elemento/s de las tuplas cuyo segundo elemento es mayor o igual a todos los segundos elementos de las tuplas en cursadas}
    

c) Especificar el problema que, dada una materia y las calificaciones del DC, devuelve todos los estudiantes que cursaron y aprobaron esa materia. ¿Cómo debe modificarse la especificación para que los nombres se devuelvan en orden alfabético? ¿Este cambio reduce o amplía la cantidad de programas que resolverían el problema?

problema estudiantesAprobados (materia: Materia, calificaciones: CalificacionesDelDC) : seq⟨Alumno⟩
    requiere: {Existe algún elemento en CalificacionesDelDC cuya segunda componente contenga a Materia}
    asegura: {resultado es la secuencia de primer/os elemento/s de los elementos en CalificacionesDelDC cuya segunda componente contenga a Materia con calificación mayor o igual a 4}

#Modificación para devolver los nombres en orden alfabético:
problema problema estudiantesAprobados (materia: Materia, calificaciones: CalificacionesDelDC) : seq⟨Alumno⟩
    requiere: {Existe algún elemento en CalificacionesDelDC cuya segunda componente contenga a Materia}
    asegura: {resultado es la secuencia de primer/os elemento/s de los elementos en CalificacionesDelDC cuya segunda componente contenga a Materia con calificación mayor o igual a 4}
    asegura: {en caso de no estar vacía, resultado está ordenado alfabéticamente, en el mismo orden que aparecerían en un diccionario}

#este cambio reduce la cantidad de programas que resolverían el problema, ya que ahora se asegura un ordenamiento alfabético de los nombres, lo que implica que no todos los programas que devuelvan la secuencia de estudiantes aprobados cumplirían con esta condición adicional.   

d) Especificar el problema de devolver una secuencia con los promedios de todos los estudiantes.

    Renombre Alumno = String
    Renombre Materia = String
    Renombre Cursada = seq⟨Materia × R⟩
    Renombre CalificacionesDelDC = seq⟨Alumno × Cursada⟩

problema promediosDeEstudiantes (calificaciones: CalificacionesDelDC) : (seq(R))
    requiere: {Para cada alumno dentro de calificaciones, la longitud de su cursada debe ser estrictamente mayor a 0}
    asegura: {resultado es una secuencia de números donde resultado[i] es el resultado de aplicar promedioAlumno(alumno,calificaciones), siendo "alumno" el primer elemento de calificaciones[i]} 
    asegura: {resultado tiene la misma cantidad de elementos que CalificacioneDelDC}"""

#Nota: Estaba durmiéndome haciendo el ítem b), pero me puse a jugar un battle simulator de Undyne the undying y me desperté porque siempre siento tensión con minijuego complicados. Además, estoy en la biblioteca de la UTN y no quería que nadie me viera, entonces estab ultra alerta. Estoy feliz y sonriente porque logré mi cometido, perdí, quise gritar como con todo juego por la tensión constante hasta que perdí, pero obviamente tuve que aguantármelo y me causó mucha gracia. Ahora estoy listo para continuar con los ítems c) y d).

