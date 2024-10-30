import tkinter # Importar libreria

# Función para saludar
def saludar():
    nombre = entrada_nombre.get()
    txt_resultado.config(text=f"Hola : {nombre}")

# Crear la ventana principal
ventana = tkinter.Tk()
ventana.title("Saludo")
ventana.geometry("300x200")  # Dimensiones de la ventana (Base_x_Altura)

tkinter.Label(ventana, text="Ingresa tu nombre").pack()

#Campos de texto
entrada_nombre = tkinter.Entry(ventana)
entrada_nombre.pack()

tkinter.Button(ventana, text="Saludar", command=saludar).pack()

txt_resultado = tkinter.Label(ventana, text="Hola : ")
txt_resultado.pack() 

# Iniciar el bucle principal
ventana.mainloop()
