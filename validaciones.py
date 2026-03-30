def pedir_numero(mensaje, tipo="int"):
    continuar = "si"

    while continuar == "si":
        valor = input(mensaje).strip()

        # ❌ Validar vacío o espacios
        if valor == "":
            print("❌ No puede estar vacío")
            continue

        try:
            if tipo == "int":
                numero = int(valor)
            else:
                numero = float(valor)

            # ❌ No permitir negativos
            if numero < 0:
                print("❌ No se permiten números negativos")
            else:
                continuar = "no"
                return numero

        except ValueError:
            print("❌ Ingrese un valor válido (solo números)")





            