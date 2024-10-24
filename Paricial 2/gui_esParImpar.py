import tkinter 

# Función que calcula si el número ingresado es par o impar (r = "Es Par" | r = "Es impar" )
def esParImpar():
    try:
        # Convertimos el valor ingresado a float y calculamos el módulo 2 para verificar si es par o impar
        resultado = float(n1.get()) % 2
        
        # Si el residuo es 0, significa que el número es par
        if resultado == 0:
            r.config(text="Es par")
        else:
            r.config(text="Es impar")  # Si no, el número es impar
    except ValueError:
        r.config(text="Por favor, ingrese un número válido")  # Manejo de errores si el input no es un número

# Creamos la ventana principal
ventana = tkinter.Tk()

# Creamos una etiqueta (Label) con el texto "INGRESA EL NÚMERO" y se agrega a la ventana usando la funcion (.pack)
tkinter.Label(ventana, text="NÚMERO").pack()

# Creamos un campo de entrada para que el usuario pueda ingresar un número
n1 = tkinter.Entry(ventana) # , justify="center"
n1.pack() # Agregamos a la ventana usando (.pack)

# Creamos un botón que ejecuta la función 'esParImpar' al hacer clic "Calcular"
tkinter.Button(ventana, text="Calcular", command=esParImpar).pack() # Agregar a la ventana usando la función (.pack)

# Creamos una etiqueta con el texto "Resultado" que mostrará si el número es par o impar
r = tkinter.Label(ventana, text="Resultado")
r.pack() # Agregamos la etiqueta r a la ventana usando la función (.pack)

# Iniciamos el bucle principal de la aplicación para que la ventana permanezca abierta
ventana.mainloop()
