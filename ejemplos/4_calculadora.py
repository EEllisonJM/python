import tkinter as tk

# Función que agrega números y operadores a la pantalla de la calculadora
def agregar_a_pantalla(contenido):
    pantalla.insert(tk.END, contenido)

# Función que evalúa la expresión en la pantalla
def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Función que borra el contenido de la pantalla
def limpiar_pantalla():
    pantalla.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear el campo de entrada donde se mostrarán los números y el resultado
# pantalla = tk.Entry(ventana, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
pantalla = tk.Entry(ventana)
pantalla.grid(row=0, column=0, columnspan=4)

# Crear los botones numéricos y de operaciones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

# Agregar los botones a la ventana
for (texto, fila, columna) in botones:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=('Arial', 18), command=calcular)
    elif texto == 'C':
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=('Arial', 18), command=limpiar_pantalla)
    else:
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=('Arial', 18),
                          command=lambda texto=texto: agregar_a_pantalla(texto))
    
    boton.grid(row=fila, column=columna)

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()
