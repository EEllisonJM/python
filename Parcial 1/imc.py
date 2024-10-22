# Calcuar el índice de masa corporal

# Función para calcular el índice de masa corporal
def calcular_imc(peso, altura):
    # Fórmula para calcular el IMC
    imc = peso / (altura ** 2)
    return imc

# Entrada de datos del usuario
peso = float(input("Ingrese su peso (Kg): "))
altura = float(input("Ingrese su altura (m): "))

# Procesos (Cálculo del IMC)
imc = calcular_imc(peso, altura)

# Salidas (Mostrar el resultado)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

# Clasificación del IMC según la OMS
if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")
