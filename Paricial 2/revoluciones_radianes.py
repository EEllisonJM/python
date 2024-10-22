import math

def convertir_a_radianes(revoluciones):
    # Fórmula para convertir revoluciones a radianes
    radianes = revoluciones * (2 * math.pi)
    return radianes

# Entrada de datos del usuario
revoluciones = float(input("Ingrese el número de revoluciones: "))

# Convertir a radianes
radianes = convertir_a_radianes(revoluciones)

# Mostrar el resultado
print(f"{revoluciones} revoluciones es igual a {radianes:.4f} radianes")
