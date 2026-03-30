
# Pedir datos al usuario
producto = input("Ingrese el nombre del producto: ")
valor = float(input("Ingrese el valor del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

# Operaciones básicas
total = valor * cantidad   # Multiplicación
descuento = total * 0.1    # Ejemplo: 10% de descuento
total_final = total - descuento  # Resta

# Mostrar resultados imprimirlos
print("\n--- Resultado ---")
print("Producto:", producto)
print("Valor unitario:", valor)
print("Cantidad:", cantidad)
print("Total sin descuento:", total)
print("Descuento aplicado:", descuento)
print("Total a pagar:", total_final)


# porcentajes 

print("=== Cálculo de Porcentajes ===")

# Datos ingresados por el usuario
producto = input("Ingrese el nombre del producto: ")
valor = float(input("Ingrese el valor del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

# Total de la compra
total = valor * cantidad

# Ejemplo: calcular un porcentaje de descuento
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (%): "))
descuento = total * (porcentaje_descuento / 100)   # fórmula: total * (porcentaje / 100)
total_final = total - descuento

# Mostrar resultados
print("\n--- Resultado ---")
print("Producto:", producto)
print("Valor unitario:", valor)
print("Cantidad:", cantidad)
print("Total sin descuento:", total)
print("Descuento aplicado:", descuento)
print("Total a pagar:", total_final)

# Ejemplo adicional: calcular porcentaje de IVA
iva = total_final * 0.19   # 19% de IVA
print("IVA (19%):", iva)
print("Total con IVA:", total_final + iva)

#aplique de porcentaje la persona 
print("=== Cálculo de Porcentaje Fijo ===")

# Datos ingresados por el usuario
producto = input("Ingrese el nombre del producto: ")
valor = float(input("Ingrese el valor del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

# Total de la compra
total = valor * cantidad

# Aquí defines tú el porcentaje (ejemplo: 15%)
porcentaje = 154
# Aplicar el porcentaje al total
descuento = total * (porcentaje / 100)
total_final = total - descuento

# Mostrar resultados
print("\n--- Resultado ---")
print("Producto:", producto)
print("Valor unitario:", valor)
print("Cantidad:", cantidad)
print("Total sin descuento:", total)
print(f"Descuento ({porcentaje}%):", descuento)
print("Total a pagar:", total_final)
