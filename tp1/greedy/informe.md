# Informe punto 1


## 1. Pseudocódigo de la solución

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
	EMPLEADOS = FUNCION_DTI(tiempo)
	agregar EMPLEADOS a UBICACION_EMPLEADOS

Para cada EMPLEADO en UBICACION_EMPLEADOS
	imprimir_resultado(EMPLEADO)
```

## 2. Tipo de algoritmo y Justificación

### 2.1 Objetivo

Realizar la menor cantidad de llamadas al sistema DTI de forma que se pueda obtener
la ubicación de todos los empleados en su horario laboral.

### 2.2 Estrategia

Todos los empleados tienen un horario laboral definido por Ti y Tf
(Ti tiempo de inicio y Tf tiempo de fin).
Para realizar la mínima cantidad de consultas al sistema DTI, se debe encontrar
el o los valores de tiempo en el que se debe realizar la o las consultas al sistema.
Se deben intersecar todos los horarios laborales de los empleados para hallar los tiempos
de consulta y seleccionar aquellos valores de tiempo que haga mínima la cantidad de consultas.
Lo que confiere un costo de NxN.

Para minimizar este costo Se propone ordenar los empleados por tiempo de inicio
de actividades (Ti), de tal forma que al recorrer se hagan según más temprano ingresen
al trabajo y se va a ir intersectando con el horario del siguiente empleado hasta que no
se puede intersecar más. lo que crea una consulta, se realiza
nuevamente el proceso de intersección hasta que no haya más empleados.


### 2.3 Justificación

Se puede observar que en cada iteración el intervalo de tiempo de consulta se
hace más chico o se mantiene y va abarcando a más empleados hasta donde sea
posible.
Cuando el intervalo deja de intersecarse con más empleados, se elige un valor de
tal intervalo para hacer la consulta. y al dejar de intesecarse es porque se
necesita otro intervalo de consulta obligatoriamente del cual se tomará otro valor.
Esto quiere decir que es imposible hacer la consulta en un único tiempo "t" para poder
localizar a todos los empleados en su horario laboral.

Entonces, en cada iteración se selecciona un óptimo local de todo el intervalo inicial
(el intervalo se hace más chico) esta es una elección Greedy dado que esta elección
persiste hasta que dicho intervalo deje de intersecarse.

## 3. Evaluación de la complejidad

### 3.1 Evaluación de la complejidad Temporal
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
	EMPLEADOS = FUNCION_DTI(tiempo)							| O(1)
	agregar EMPLEADOS a UBICACION_EMPLEADOS					| O(1)

Para cada EMPLEADO en UBICACION_EMPLEADOS					| O(n)
	imprimir_resultado(EMPLEADO)						| O(1)

```
Interpretación:
Como se puede observar se recibe un vector de n empleados, que posteriormente
es ordenado, esto tiene un costo de O(nlog(n))

luego iterar todos los empleados para obtener los intervalos de consulta
tiene un costo de O(n).

Del proceso anterior se obtuvo un vector con m intervalos de consulta con
1 <= m <= n, esto quiere decir que se tiene al menos un intervalo y a lo sumo n
intervalos.
Luego recorrer todos los intervalos para hacer la consulta tiene un costo de O(m)
con O(1) <= O(m) <= O(n)

Finalmente se itera todas las ubicaciones obtenidas para cada empleado esto tiene
un costo de O(n).

esto da como resultado :
O(nlog(n)) + O(n) + O(m) + O(n) = O(nlog(n))

### 3.2 Evaluación de la complejidad Espacial


##4. Justificación de que es una solución óptima

Supongamos que tenemos una solución óptima (Op). Si la solución propuesta (llamada MIN_DTI)
no es óptima, entonces nuestra solución realiza al menos una consulta mas que Op.
Entonces #consultas(MIN_DTI) > #consultas(Op)

Esto quiere decir que MIN_DTI según el algoritmo tiene al menos un intervalo
de consulta de más.
Pero eso no se puede dar porque al recorrer los empleados (ordenados por inicio de
actividades) se van intersectando con un empleado y si deja de intersecarse es porque es
necesario una nueva consulta al sistema, porque el horario laboral de este último
empleado NO coincide con todos los anteriores.
El proceso se repite y se genera al final k intervalos con k <= n, y cada uno de esos
intervalos son necesarios.
Por lo tanto podemos decir que el número de intervalos es mínimo y la cantidad de consultas
al sistema DTI también.
