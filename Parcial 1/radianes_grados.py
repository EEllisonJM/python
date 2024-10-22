import math

def convertir_a_grados(radianes):
    # Fórmula para convertir radianes a grados
    grados = radianes * (180 / math.pi)
    return grados

# Entrada de datos del usuario
radianes = float(input("Ingrese el ángulo en radianes: "))

# Convertir a grados
grados = convertir_a_grados(radianes)

# Mostrar el resultado
print(f"{radianes} radianes es igual a {grados:.4f} grados")
