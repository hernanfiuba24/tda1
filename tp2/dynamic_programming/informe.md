
# TP2 Informe punto 1

## 1. Solución con programación dinámica

Primero leyendo el archivo de entrada se cargaran todos los item en memoria.

Luego se arma un árbol de decisión por cada item, pues cada item tendrá tantos nodos hijos como items
le anteceden y además cumplen con las restricciones.

Luego se evalúan todos los casos posibles para calcular el óptimo de cada item, se tendra que recorrer
tantos caminos como nodos hijos tenga y a la vez nodos hijos de nodos hijos.
Por lo que en el peor de los casos se tienen 2^(n-2) caminos, para n > 1.

--------------------- acá se debe adjuntar una imagen del árbol -------------------------

para simplificar esto se realiza programación dinámica almacenando soluciones optimas
de subproblemas que se repiten en el árbol de decisión.

En este caso se obtienen previamente los items anteriores validos a cada item.
Luego se comienza a iterar para obtener el valor óptimo de cada item basandose en el valor máximo que entre los óptimos que tienen los items que lo anteceden.

El resultado final será una estructura que contiene el beneficio óptimo de cada item, sólo resta elegir
el máximo entre ellos.

Dado que no especifica, se asume que el resultado devuelto es el valor óptimo sin importar si se usa o no item en un trimestre dado, por lo cual asumimos que pueden haber trimestres en el cual no se usen items debido a las restricciones.
...

## 2. Subproblema del planteo

Como se mencionó anteriormente se tendrá un árbol por cada item, en el cual el cual los items que se encuentren en el trimestre más alto serán aquellos que tienen los árboles más profundos.
En estos árboles tienen nodos en los cuales los óptimos se repiten, esos óptimos en lugar de recalcularlos
se almacenarán para utilizarlos nuevamente.


--------------------- acá se debe adjuntar una imagen del árbol con el subproblema -------------------------

## 3. Relación de recurrencia.

A continuación se presenta la relación de recurrencia utilizada en la solución
de programación dinámica.

```
OPT(0) = 0 												t = 0
OPT(i) = { profit[i] + max( OPT[items_previus[i]] ) }	t > 0
```
En la relación de recurrencia se puede observar	que el óptimo de cada item se basa
en el óptimo de sus anteriores, por eso se define que el óptimo inicial es cero, para
que el el óptimo previo al primer item tenga beneficio cero.


## 4. Pseudocódigo de la solución iterativa

```java
obtener_maximo_beneficio(items)

	n = len(items)
	OPT[n+1]= 0
	anteriores = anteriores(items) //anteriores_permitidos = [n+1][n+1]
	pos_solution = 0

	Desde i = 1 hasta n

		beneficio_maximo_previo = OPT[0]
		previo_maximo = 0
		anteriores_permitidos = anteriores[i]

		Para cada item_previo en anteriores_permitidos
			Si OPT[item_previo] > previo_maximo
				previo_maximo = item_previo

		OPT[i] = items[i].beneficio + OPT[item_previo]

		Si OPT[i] > OPT[pos_solution]:
			pos_solution = i

	Retornar OPT[pos_solution]
```
## 5. Complejidad temporal y espacial de la solución

Considerando que se tienen n items a sembrar y que existen t trimestres con t < n.

Primero se deben obtener todos los item anteriores para cada item, para eso se
realiza una iteración por todos los items y dentro de cada uno se hace una iteración por cada item previo a este por lo que podemos inferir que hacen n*(n-1)...n*1 iteraciones  esto tiene un costo de
O(n*(n-1)) + ... + O(n*1) lo que equivale a O( n*(n-1) + ... + n*1) esto tiene un costo polinómico.

Luego se hace una iteración por cada item para buscar el beneficio óptimo de cada item para ello se tiene que hacer otra iteración sobre todos los elementos previos para obtener aquel que tenga el beneficio óptimo ,luego se obtiene el máximo de de todos los óptimos.
En este caos nuevamente se hacen n*(n-1)...n*1 iteraciones esto tiene un costo de O(n*(n-1)) + ... + O(n*1) lo que equivale a O( n*(n-1) + ... + n*1) esto tiene un costo polinómico.

Sumando ambos costos se tiene que el costo final es polinómico,
Por lo tanto tiene una complejidad temporal polinómica.

Para la evaluación de la complejidad espacial se utilizan tres estructura de datos
una para el almacenamiento de los items y tiene un tamaño n, otra para los previos, siendo este de tamaño n*n, y finalmente una estructura para almacenar los óptimos de cada item tiendo un tamaño n.
Por lo tanto se tiene un costo de O(n), O(n*n) y O(n) respectivamente.
Si sumamos todos obtenemos que O(n + n*n + n) está acotado por O(n*n).
Por lo tanto tiene una complejidad espacial cuadrática.

## 6. Programe su solución
	La solución programada se encuentra en el archivo main.py junto con multiples sets de datos
	de la forma data_*.txt.
	La ejecución del programa se realiza mediante el siguiente comando:
	python3 main2.py data_v2.txt
