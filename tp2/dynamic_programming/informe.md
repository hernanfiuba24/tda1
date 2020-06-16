
# TP2 Informe punto 1

## 1. Solución con programación dinámica

Se plantea realizar un árbol de decisión cuya raíz es el total de hectarias disponible
y se ramifica en sub problemas con una cantidad de hectarias menor al de la raiz.
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
