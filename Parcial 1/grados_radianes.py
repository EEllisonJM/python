import math

def convertir_a_radianes(grados):
    # Fórmula para convertir grados a radianes
    radianes = grados * (math.pi / 180)
    return radianes

# Entrada de datos del usuario
grados = float(input("Ingrese el ángulo en grados: "))

# Convertir a radianes
radianes = convertir_a_radianes(grados)

# Mostrar el resultado
print(f"{grados} grados es igual a {radianes:.4f} radianes")
