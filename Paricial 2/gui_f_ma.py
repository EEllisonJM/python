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
txt_titulo = tkinter.Label(ventana, text="F = m * a")
txt_masa = tkinter.Label(ventana, text="Ingrese la masa (kg):")
txt_aceleracion = tkinter.Label(ventana, text="Ingrese la aceleración (m/s²):")
txt_resultado = tkinter.Label(ventana, text="Fuerza: ")

#Campos de texto
entrada_masa = tkinter.Entry(ventana)
entrada_aceleracion = tkinter.Entry(ventana)

boton_calcular = tkinter.Button(ventana, text="Calcular Fuerza", command=calcular_fuerza)

txt_titulo.pack() # Coloca el widget en la ventana
txt_masa.pack() # Coloca el widget debajo de txt_titulo
entrada_masa.pack() # Coloca el widget debajo de txt_masa
txt_aceleracion.pack() # Coloca el widget debajo de entrada_masa
entrada_aceleracion.pack() # Coloca el widget debajo de txt_aceleracion
boton_calcular.pack() # Coloca el widget debajo de entrada_aceleracion
txt_resultado.pack() # Coloca el widget debajo de entrada_masa

# Iniciar el bucle principal
ventana.mainloop()
