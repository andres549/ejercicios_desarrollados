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

print("=== Programa interactivo con while ===")

continuar = "si"  # variable inicial

while continuar == "si":
    # Aquí va la lógica del programa
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad vendida: "))

    # Clasificación simple con condicionales
    if precio < 20000:
        print(f"{producto} es barato.")
    elif precio < 100000:
        print(f"{producto} tiene precio medio.")
    else:
        print(f"{producto} es caro.")

    # Preguntar al usuario si quiere continuar
    continuar = input("¿Desea ingresar otro producto? (si/no): ").lower()

#bucle for
print("=== Bucle for con lista de productos ===")

productos = ["Camisa", "Pantalón", "Zapatos"]

for producto in productos:
    # Etiqueta para mostrar cada producto
    print("Producto:", producto)
""" 
El for recorre cada elemento de la lista. En cada vuelta, la variable producto toma un valor distinto y se imprime con su etiqueta."""

