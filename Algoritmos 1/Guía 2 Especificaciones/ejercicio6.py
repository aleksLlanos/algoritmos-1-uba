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
-   Ejemplo de información de un estudiante registrado: (Alexander Llanos, Alexander Llanoz, Priscilla ) #no son duplicados
-   Ejemplo de información de cursada: [(Análisis Matemático, 10) , (Física, 6) , (ICSE, 8)] 


b) Especificar el problema que, dado el listado de materias cursadas por un estudiante, indique en qué materia tuvo mayor calificación. ¿Cómo se debe modificar la especificación para devolver el listado de materias en las cuales tuvo mejor calificación?

c) Especificar el problema que, dada una materia y las calificaciones del DC, devuelve todos los estudiantes que cursaron y aprobaron esa materia. ¿Cómo debe modificarse la especificación para que los nombres se devuelvan en orden alfabético? ¿Este cambio reduce o amplía la cantidad de programas que resolverían el problema?

d) Especificar el problema de devolver una secuencia con los promedios de todos los estudiantes."""