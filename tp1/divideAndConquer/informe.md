# Informe punto 2
## Pseudocodigo Proceso A
```python
para cada pieza i del lote:
  cantidad = 1
  para cada pieza j del lote:
    si i != j y vol_i == vol__j:
      cantidad ++
  si cantidad > n/2:
    rotulo = vol_i
  sino:
    descarto el lote
