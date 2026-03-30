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
