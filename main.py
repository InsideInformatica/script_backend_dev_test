import csv

def leer_productos(archivo_productos):
    productos = {}
    with open(archivo_productos, mode="r") as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            sku, precio = row[0].strip(), float(row[1].strip())  
            productos[sku] = precio
    return productos

def leer_inventario(archivo_inventario):
    inventario = {}
    with open(archivo_inventario, mode="r") as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            sku, stock = row[0].strip(), int(row[1].strip())  
            if sku in inventario:
                inventario[sku] += stock
            else:
                inventario[sku] = stock
    return inventario

def generar_resultado(productos, inventario, archivo_salida):
    with open(archivo_salida, mode="w", newline="") as file:
        writer = csv.writer(file)
        
        writer.writerow(["sku     |  precio_final   |  stock_total   |"])
        
        for sku, precio in productos.items():
            if sku in inventario:
                stock_total = inventario[sku]
                precio_final = precio * 1.21  # IVA
               
                writer.writerow([f"  {sku}  |  {precio_final:.2f}  |  {stock_total}  |"])

def main():
    archivo_productos = "productos.csv"
    archivo_inventario = "inventario.csv"
    archivo_salida = "resultado.csv"
    
    productos = leer_productos(archivo_productos)
    inventario = leer_inventario(archivo_inventario)
    generar_resultado(productos, inventario, archivo_salida)

if __name__ == "__main__":
    main()
