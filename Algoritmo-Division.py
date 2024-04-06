def dividir():
    try:
        return float(input("Ingresa el primer número: ")) / float(input("Ingresa el segundo número: "))
    except (ValueError, ZeroDivisionError):
        print("Debes ingresar números válidos y el segundo número no puede ser cero.")

# Ejemplo de uso:
resultado = dividir()
if resultado is not None:
    print("El resultado de la división es:", resultado)