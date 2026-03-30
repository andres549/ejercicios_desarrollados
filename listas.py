# Crear una lista
productos = ["Camisa", "Pantalón", "Zapatos"]

# Acceder a elementos por índice
print(productos[0])  # Camisa
print(productos[1])  # Pantalón
print(productos[2])  # Zapatos

# Recorrer la lista con for
for item in productos:
    print("Producto:", item)

print("=== Lista de Productos ===")

# Lista vacía
productos = []

# Definimos cuántos productos queremos ingresar
num_productos = 3

for i in range(num_productos):
    print(f"\nProducto {i+1}:")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    
    # Guardar como tupla (nombre, precio) dentro de la lista
    productos.append((nombre, precio))

# Mostrar lista completa
print("\n--- Lista Final ---")
for nombre, precio in productos:
    print(f"{nombre} -> Precio: {precio}")
