import tkinter as tk
from tkinter import messagebox

# Función para calcular la fuerza (F = m * a)
def calcular_fuerza():
    try:
        masa = float(entrada_masa.get())
        aceleracion = float(entrada_aceleracion.get())
        if masa <= 0 or aceleracion <= 0:
            raise ValueError("Valores no válidos")
        
        fuerza = masa * aceleracion
        label_resultado.config(text=f"La fuerza es: {fuerza:.2f} N")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora - Segunda Ley de Newton")

# Etiqueta y entrada para la masa
label_masa = tk.Label(ventana, text="Masa (kg):", font=('Arial', 14))
label_masa.pack(pady=5)

entrada_masa = tk.Entry(ventana, font=('Arial', 14))
entrada_masa.pack(pady=5)

# Etiqueta y entrada para la aceleración
label_aceleracion = tk.Label(ventana, text="Aceleración (m/s²):", font=('Arial', 14))
label_aceleracion.pack(pady=5)

entrada_aceleracion = tk.Entry(ventana, font=('Arial', 14))
entrada_aceleracion.pack(pady=5)

# Botón para calcular la fuerza
boton_calcular = tk.Button(ventana, text="Calcular Fuerza", font=('Arial', 14), command=calcular_fuerza)
boton_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="", font=('Arial', 14))
label_resultado.pack(pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
