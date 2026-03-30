# Crear un diccionario
producto = {
    "nombre": "Camisa",
    "precio": 50000,
    "cantidad": 2
}

# Acceder a valores
print(producto["nombre"])    # Camisa
print(producto["precio"])    # 50000
print(producto["cantidad"])  # 2

#para agregar productos croquis
inventario = {
    "Camisa": {"precio": 50000, "cantidad": 10},
    "Pantalón": {"precio": 80000, "cantidad": 5}
}

# Diccionario de productos
inventario = {
    "Camisa": {"precio": 50000, "cantidad": 2},
    "Pantalón": {"precio": 80000, "cantidad": 1},
    "Zapatos": {"precio": 120000, "cantidad": 3}
}

# Recorrer el diccionario con for
for producto, datos in inventario.items():
    # producto = clave (ejemplo: "Camisa")
    # datos = valor (ejemplo: {"precio": 50000, "cantidad": 2})
    
    # Mostrar información con etiquetas
    print("=== Producto ===")              # etiqueta visual
    print("Nombre:", producto)             # clave
    print("Precio:", datos["precio"])      # valor dentro del diccionario
    print("Cantidad:", datos["cantidad"])  # valor dentro del diccionario
    print("-------------------")            # separador

inventario = {
    "Camisa": {"precio": 50000, "cantidad": 2},
    "Pantalón": {"precio": 80000, "cantidad": 5},
    "Zapatos": {"precio": 120000, "cantidad": 1}
}

# Función para obtener la cantidad
def criterio_cantidad(item):
    return item[1]["cantidad"]

# Función para obtener el precio
def criterio_precio(item):
    return item[1]["precio"]

# Usar las funciones en lugar de lambda
mas_vendido = max(inventario.items(), key=criterio_cantidad)
mas_barato = min(inventario.items(), key=criterio_precio)
mas_caro = max(inventario.items(), key=criterio_precio)

# Ejemplo con for
for producto, datos in inventario.items():
    # Aquí no usamos paréntesis porque Python ya separa la clave y el valor
    print("Producto:", producto)
    print("Precio:", datos["precio"])
    print("Cantidad:", datos["cantidad"])




# Los paréntesis aparecen cuando Python muestra los pares (clave, valor) como tuplas.
# Si desempaquetamos esas tuplas directamente en variables (producto, datos),
# ya no necesitamos escribir los paréntesis en nuestro código.
