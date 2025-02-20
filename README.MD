# Prueba tecnica Inside Informatica

Teniendo en cuenta los dos archivos:
- inventario.csv
- productos csv

Se deben filtrar los siguientes datos:

- sku -> columna *N0* sobre ambos archivos
- precio -> columna *N1* sobre productos.csv
- stock -> columna *N1* sobre inventario.csv

Y generar un csv resultante de la siguente manera:

- sku -> sku del producto filtrado
- precio_final -> precio del producto + 21%
- stock_total -> stock total del producto

### Ejemplo de archivo resultante
```csv
sku,precio_final,stock
PS-SL-A287,1512,50,25
```

Se detallan ejemplos de escritura y lectura de archivos csv:

```python
# Lectura de csv
with open("productos.csv", mode="r") as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
```


```python
# Escritura de csv
lines = [
    ["sku", "precio", "stock"], 
    ["123", "25.00", "10"],
    ["456", "15.00", "5"],
    ["789", "30.00", "20"],
]
with open("resultado.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(lines)
```
