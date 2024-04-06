def convertir_base():
    try:
        numero = int(input("Ingresa el número en base 10: "))
        base = int(input("Ingresa la base a la que quieres convertirlo: "))
        
        if base < 2:
            return "La base debe ser mayor o igual a 2."
        
        if numero == 0:
            return "0"

        representacion = ""
        while numero > 0:
            residuo = numero % base
            representacion = str(residuo) + representacion
            numero //= base
        
        return representacion
    except ValueError:
        return "Debes ingresar números enteros válidos."

# Ejemplo de uso:
resultado = convertir_base()
print("La representación en base es:", resultado)




