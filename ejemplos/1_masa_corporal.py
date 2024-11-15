import tkinter as tk
from tkinter import messagebox

# Función para calcular el Índice de Masa Corporal (IMC)
def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        if altura <= 0 or peso <= 0:
            raise ValueError("Valores no válidos")
        
        imc = peso / (altura ** 2)
        resultado = f"Tu IMC es: {imc:.2f}"

        if imc < 18.5:
            resultado += " (Bajo peso)"
        elif 18.5 <= imc < 24.9:
            resultado += " (Peso normal)"
        elif 25 <= imc < 29.9:
            resultado += " (Sobrepeso)"
        else:
            resultado += " (Obesidad)"
        
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de IMC")

# Etiqueta y entrada para el peso
label_peso = tk.Label(ventana, text="Peso (kg):")
label_peso.pack(pady=5)

entrada_peso = tk.Entry(ventana, font=('Arial', 14))
entrada_peso.pack(pady=5)

# Etiqueta y entrada para la altura
label_altura = tk.Label(ventana, text="Altura (m):", font=('Arial', 14))
label_altura.pack(pady=5)

entrada_altura = tk.Entry(ventana, font=('Arial', 14))
entrada_altura.pack(pady=5)

# Botón para calcular el IMC
boton_calcular = tk.Button(ventana, text="Calcular IMC", font=('Arial', 14), command=calcular_imc)
boton_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="", font=('Arial', 14))
label_resultado.pack(pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
