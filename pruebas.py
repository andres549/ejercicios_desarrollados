print("\n=== Bucle for con diccionario de productos ===")

inventario = {
    "Camisa": {"precio": 50000, "cantidad": 2},
    "Pantalón": {"precio": 80000, "cantidad": 5},
    "Zapatos": {"precio": 120000, "cantidad": 1}
}

for producto, datos in inventario.items():
    # Etiquetas para mostrar cada dato
    print("=== Producto ===")
    print("Nombre:", producto)
    print("Precio:", datos["precio"])
    print("Cantidad:", datos["cantidad"])
    print("-------------------")
