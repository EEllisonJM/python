import math

def convertir_a_revoluciones(radianes):
    # Fórmula para convertir radianes a revoluciones
    revoluciones = radianes / (2 * math.pi)
    return revoluciones

# Entrada de datos del usuario
radianes = float(input("Ingrese el ángulo en radianes: "))

# Convertir a revoluciones
revoluciones = convertir_a_revoluciones(radianes)

# Mostrar el resultado
print(f"{radianes} radianes es igual a {revoluciones:.4f} revoluciones")
