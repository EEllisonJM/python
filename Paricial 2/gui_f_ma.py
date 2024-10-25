import tkinter # Importar libreria

# Función para calcular la fuerza
def calcular_fuerza():
    masa = float(entrada_masa.get()) # Obtener valor desde la ventana (Masa) 
    aceleracion = float(entrada_aceleracion.get())# Obtener valor desde la ventana (Aceleracion) 
    fuerza = masa * aceleracion
    txt_resultado.config(text=f"Fuerza: {fuerza} N")

# Crear la ventana principal
ventana = tkinter.Tk()
ventana.title("2da Ley de Newton")
ventana.geometry("300x200")  # Dimensiones de la ventana (Base_x_Altura)

# Etiquetas F = m * a
tkinter.Label(ventana, text="F = m * a").pack()
tkinter.Label(ventana, text="Ingrese la masa (kg):").pack()

#Campos de texto
entrada_masa = tkinter.Entry(ventana)
entrada_masa.pack() # Coloca el widget debajo de txt_masa

tkinter.Label(ventana, text="Ingrese la aceleración (m/s²):").pack()

entrada_aceleracion = tkinter.Entry(ventana)
entrada_aceleracion.pack() # Coloca el widget debajo de txt_aceleracion

tkinter.Button(ventana, text="Calcular", command=calcular_fuerza).pack()

txt_resultado = tkinter.Label(ventana, text="Fuerza: ")
txt_resultado.pack() # Coloca el widget debajo de entrada_masa

# Iniciar el bucle principal
ventana.mainloop()
