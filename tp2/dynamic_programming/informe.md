
# TP2 Informe punto 1

## 1. Solución con programación dinámica

Primero leyendo el archivo de entrada se determinará la cantidad máxima de trimestres
que se deben procesar.

Luego arma se arma un árbol de decisión cuya raíz es la máxima cantidad de
trimestres para plantar.

Se evaluan todos los casos posibles, para calcular el óptimo usando todos los trimestres
de tiempo, esto es el optimo T se calcula como el óptimo T-1 y el óptimo de 1 trimestres,
el óptimo T-2 y el optimo de 2 trimestres, etc a su vez el optimo T-1 se subdive entre el optimo entre el óptimo T-2 y el optimo de 2, y asi se crea el arbol de decisión.

para simplificar esto se realiza programación dinámica almacenando soluciones optimas
de subproblemas que se repiten en el arbol de decisión.

En este caso comienza obteniendo el óptimo usando sólo el primer trimestre dando
esta una solución optima, luego bajo las restricciones aplicadas se optiene una solucion optima
usando la solución optima del paso anterior. esta nueva solucion puede no contener a la solucion del paso anterior.

Dado un periodo t, se obtienen todos los item que pueden ser plantados en ese trimestre,
luego se obtiene el item plantado en el trimestre anterior, se verifican las restricciones
y se obtiene el item optimo para ser plantado en el perido t
Entonces se obtiene el elemento previamente 

...

## 2. Subproblema del planteo

...



## 3. Relación de recurrencia.

A continuación se presenta la relación de recurrencia utilizada en la solución
de programación dinámica.
```
OPT(t) = 0 												t = 0
OPT(t) = max (i / item i e Items AND item i have t and item i is allowed)
				{ profit[i] + OPT(t - i)}				t > 0
```

En la relación de recurrencia se puede observar	que cuando el trimestre es cero
el óptimo de ganancia es cero.

En en caso contrario cuando t es mayor a cero, el óptimo en ganancia se obtiene
entre el máximo entre el óptimo del paso y el óptimo del paso anterior más
la máxima ganancia entre los items cuyo trimestre es t y puede ser usado sin incumplir
la restricción de cultivos consecutivos o de repetir el mismo cultivo.

## 4. Pseudocódigo de la solución iterativa

```java
Desde i = 1 hasta n
OPT[i]= 0

Desde t=1 a T
	max_profit = 0
	Desde j=1 a n
		si previus_item is allowed
			si max_profit < Items[j] + OPT[t-1]
				max_profit = Items[j] + OPT[t-1]
				previus_item = Items[j]
	OPT[t] = max_profit

Retornar OPT[T]
```
## 5. Complejidad temporal y espacial de la solución

Considerando que se tienen n items a sembrar y que existen t trimestres con t < n.

Para la evaluación de la complejidad temporal se debe considerar que inicalmente
se realiza un ordenamiento para obtener el valor de trimestre más alto, esto se realiza
con un costo de O(nlog2n);

Luego se realiza una iteración por todos los trimestres con un costo de O(t)
dentro de esa iteración se realiza otra iteración por todos los items esto se
hace con un costo de O(n), dentro de ésta última iteración se realizan operaciones
con costo O(1).
Por lo tanto todo en conjunto da como resultado un costo O(t*n).

Sumando ambos costos se tiene O(nlog2n) + O(t*n), lo cual está acotado por O(t*n).
Por lo tanto el problema tiene una complejidad Temporal pseudo-polinómico.

Para la evaluación de la complejidad espacial se utilizan tres estructura de datos
una para el almacenamiento de item, siendo este de tamaño n, otra estructura
para la cantidad trimestres y una final para los items seleccionados por cada trimestres,
por lo tanto se tiene un costo de O(n), O(t) y O(t) respectivamente.
Como t < n si sumamos todos obtenemos que O(n+t+t) está acotado por O(n).
Por lo tanto tiene una complejidad espacial lineal.

## 6. Programe su solución
	La solución programada se encuentra en el archivo main2.py junto con el set de datos
	data_v2.txt.
	La ejecución del programa se realiza mediante el siguiente comando:
	python3 main2.py data_v2.txt
