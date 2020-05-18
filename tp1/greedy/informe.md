OBJETIVO: Encontrar la menor cantidad de intervalos de tiempo de tal forma que todos los intervalos se superpongan con el 
horario de trabajo de todos los empleados.

Estrategia: Ordenar los empelados por tiempo de inicio de actividades, de tal forma que se encuentre aquellos empleados
que comiencen a realizar su trabajo primero, y encontrar los intervalos de tiempo más chicos que abarquen la mayor cantidad de empleados posible.


INTERVALOS = []
EMPLEADOS = ordenar_por_si(EMPLEADOS,'creciente')						| O(nlog(n))
INTERVALO = obtener_intervalo(EMPLEADOS[0])								| O(1)

Para k desde 1 hasta n													| O(n)
	SI (INTERVALO se superpone con EMPLEADOS[k])						| O(1)
		INTERVALO = obtener_interseccion(INTERVALO, EMPLEADOS[k])		| O(1)
		SI (k == n)														| O(1)
			agregar INTERVALO a INTERVALOS								| O(1)
	SINO 																| O(1)
		agregar INTERVALO a INTERVALOS									| O(1)
		INTERVALO = obtener_intervalo(EMPLEADOS[k])						| O(1)

Para cada INTERVALO EN INTERVALOS										| O(m)
	tiempo = obtener_cualquier_punto(INTERVALO)							| O(1)
	UBICACION_EMPLEADOS = FUNCION_DTI(tiempo)							| O(1)

Para cada EMPLEADO en UBICACION_EMPLEADOS								| O(w)
	imprimir_resultado(EMPLEADO)										| O(1)


esto da como resultado :
O(nlog(n)) + O(n) + O(m) + O(w) = O(nlog(n))


Comprobando que es una solución greedy


Supangamos que tenemos una solución óptima O,
si la solución propuesta es óptima debe tener la misma cantidad de intervalos que O.
