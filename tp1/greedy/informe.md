# Informe punto 1

## 1. Objetivo

Encontrar la menor cantidad de intervalos de tiempo de tal forma que todos los intervalos se superpongan con el 
horario de trabajo de todos los empleados.

## 2. Estrategia

Ordenar los empelados por tiempo de inicio de actividades, de tal forma que se encuentre aquellos empleados
que comiencen a realizar su trabajo primero, y encontrar los intervalos de tiempo más chicos que abarquen la mayor cantidad de empleados posible.

## 3. Pseudocódigo de la solución

```java
INTERVALOS = []
EMPLEADOS = ordenar_por_SI(EMPLEADOS,'creciente')
INTERVALO = obtener_intervalo(EMPLEADOS[0])

Para k desde 1 hasta n
	SI (INTERVALO se superpone con EMPLEADOS[k])
		INTERVALO = obtener_interseccion(INTERVALO, EMPLEADOS[k])
		SI (k == n)
			agregar INTERVALO a INTERVALOS
	SINO
		agregar INTERVALO a INTERVALOS
		INTERVALO = obtener_intervalo(EMPLEADOS[k])

Para cada INTERVALO en INTERVALOS
	tiempo = obtener_cualquier_punto(INTERVALO)
	UBICACION_EMPLEADOS = FUNCION_DTI(tiempo)

Para cada EMPLEADO en UBICACION_EMPLEADOS
	imprimir_resultado(EMPLEADO)
```

## 4. Evaluación de la complejidad

```java
INTERVALOS = []
EMPLEADOS = ordenar_por_SI(EMPLEADOS,'creciente')				| O(nlog(n))
INTERVALO = obtener_intervalo(EMPLEADOS[0])					| O(1)

Para k desde 1 hasta n								| O(n)
	SI (INTERVALO se superpone con EMPLEADOS[k])				| O(1)
		INTERVALO = obtener_interseccion(INTERVALO, EMPLEADOS[k])	| O(1)
		SI (k == n)							| O(1)
			agregar INTERVALO a INTERVALOS 				| O(1)
	SINO 									| O(1)
		agregar INTERVALO a INTERVALOS 					| O(1)
		INTERVALO = obtener_intervalo(EMPLEADOS[k])			| O(1)

Para cada INTERVALO en INTERVALOS						| O(m)
	tiempo = obtener_cualquier_punto(INTERVALO)				| O(1)
	UBICACION_EMPLEADOS = FUNCION_DTI(tiempo)				| O(1)

Para cada EMPLEADO en UBICACION_EMPLEADOS					| O(w)
	imprimir_resultado(EMPLEADO)						| O(1)


esto da como resultado :
O(nlog(n)) + O(n) + O(m) + O(w) = O(nlog(n))
```

## 5. Comprobando que es una solución greedy

### 5.1 Descripción del algoritmo

El algoritmo propuesto en cada iteración encoge más el intervalo a medida que se recorren más empledos.

El intervalo inicial es todo el intervalo de trabajo del empleado que tiene menor inicio,
dicho intervalo se interseca con el intervalo de trabajo del siguiente empleado, tomando la intersección
entre ambos y este es el nuevo intervalo de consulta de DTI.

Cuando el intervalo no se interseque con mas empleados se tiene un intervalo de tiempo en el que se hará 
una consulta a DTI.

Si hay más empleados se comienza un nuevo intervalo.

### 5.2 Evaluando que el resultado es óptimo

Como se puede observar en cada iteración el intervalo de tiempo de consulta se hace más chico 
y abarca a más empleados hasta donde sea posible.

Cuando el intervalo deja de intersecarse con más empleado es porque se necesita otro intervalo de consulta.
Esto quiere decir que es imposible hacer la consulta en un único tiempo "t" para poder localizar a todos los
empleados en su horario laboral.

Entonces en cada iteración donde haya una intersección disminuyo en una unidad la cantidad de consultas al
sistema DTI. por lo tanto es una elección greedy.


Supangamos que tenemos una solución óptima Op.
Si la solución propuesta no es óptima entonces INTERVALOS debe tener una cantidad de elementos mayor Op.
entonces #(INTERVALOS) > #(Op)

Lo quiere decir que INTERVALOS tiene al menos 1 intervalo más de tiempo que la solución óptima,

.... pernsar que poner aca---
Pero el algoritmo recorre los empleados ordenados por menor tiempo de inicio y los va intersecando.
y se crea un nuevo intervalo cuando deja de haber intersecciones.
entonces el algoritmo nos retorna la cantidad de empleados que no tienen intersección 

evaluando el caso 
si i es un intervalo que pertenece a O
