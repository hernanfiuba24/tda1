# Informe punto 2
## Algunas notas (borrar cuando entregamos)
O(procesoA) = O(n2)
O(procesoB) = O(nlogn) + O(n) (mergesort + recorrer el arreglo una vez)
O(procesoC) = O(nlogn) ?

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

El proceso B introduce una mejora en cuanto al proceso A en el sentido que en el proceso B, cuando uno toma una pieza, solo tiene que recorrer las piezas siguientes hasta encontrar una con diferente volumen. Al estar ordenado podemos dejar de buscar ya que las siguientes piezas tendrán un volumen diferente.Es decir, el proceso B nos quita el hecho de buscar todos los elementos con el mismo volumen que la pieza i, sólo recorremos el lote una vez.


```python
# Asumimos que el lote tiene al menos un elemento
ordenar el lote por vol
i = 0
vol = vol[i]
cantidad = 1
hasta que termine:
  vol = vol[i]
  si cantidad > n/2:
    rotulo = vol
  sino:
    i ++
    
descartar lote
 
    
  
```
