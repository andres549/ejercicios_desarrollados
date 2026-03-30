print("=== Clasificación por Edad ===")

edad = int(input("Ingrese su edad: "))

# Condicionales sin usar 'and'
if edad < 12:
    print("Eres un niño.")
elif edad < 18:   # aquí ya sabemos que no es menor de 12
    print("Eres un adolescente.")
elif edad < 60:   # aquí ya sabemos que no es menor de 18
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")

print("=== Clasificación de Productos ===")

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad vendida: "))

# Condicionales con if, elif y else
if precio < 20000:
    print(f"{producto} es un producto barato.")
elif precio < 100000:
    print(f"{producto} tiene un precio medio.")
else:
    print(f"{producto} es un producto caro.")

# Otro condicional para la cantidad
if cantidad > 10:
    print(f"{producto} es un producto muy vendido.")
elif cantidad >= 5:
    print(f"{producto} tiene ventas moderadas.")
else:
    print(f"{producto} tiene pocas ventas.")
