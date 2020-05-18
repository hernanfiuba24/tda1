# Informe punto 2
## 1. Pseudocodigo Proceso A
```python
para cada pieza i del lote:
  cantidad = 1
  para cada pieza j del lote:
    si i != j y vol_i == vol__j:
      cantidad ++
  si cantidad > n/2:
    rotulo = vol_i
descarto el lote
```
## 2. Proceso B

El proceso B introduce una mejora en cuanto al proceso A en el sentido que en el proceso B, cuando uno toma una pieza, solo tiene que recorrer las piezas siguientes hasta encontrar una con diferente volumen. Al estar ordenado podemos dejar de buscar ya que las siguientes piezas tendrán un volumen diferente. Es decir, sólo contamos piezas con el mismo volumen. Sin embargo, el proceso B nos introduce un costo extra que es el de ordenar el lote por volumen.

Finalmente, si la complejidad de ordenar es mayor a la complejidad que quitamos al tener el lote ordenado no podemos considerar como una mejora al proceso B. De hecho, en el peor de los casos si todas las piezas del lote tienen el mismo volumen, la complejidad de B será mayor que la de A.

```python
ordenar el lote por vol
por cada pieza i del lote:
  cantidad = 0
  vol = vol_i
  pieza = i
  hasta que vol_i != vol:
    cantidad ++
    i++
  si cantidad > n/2:
    rotulo = vol
descartar lote
 
    
  
```
