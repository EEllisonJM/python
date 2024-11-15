import tkinter as tk
from tkinter import messagebox
import random

# Lista de palabras para el juego
palabras = ['python', 'programacion', 'ahorcado', 'tecnologia', 'algoritmo']

# Selección aleatoria de palabra
palabra_secreta = random.choice(palabras)
palabra_mostrada = ['_'] * len(palabra_secreta)
intentos = 6

# Función para comprobar la letra ingresada
def comprobar_letra():
    global intentos
    letra = entrada_letra.get().lower()
    
    if letra in palabra_secreta:
        for i, l in enumerate(palabra_secreta):
            if l == letra:
                palabra_mostrada[i] = letra
        label_palabra.config(text=' '.join(palabra_mostrada))
        
        if '_' not in palabra_mostrada:
            messagebox.showinfo("Ganaste", "¡Felicidades, adivinaste la palabra!")
            ventana.destroy()
    else:
        intentos -= 1
        label_intentos.config(text=f"Intentos restantes: {intentos}")
        
        if intentos == 0:
            messagebox.showerror("Perdiste", f"¡Perdiste! La palabra era: {palabra_secreta}")
            ventana.destroy()
    
    entrada_letra.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Juego del Ahorcado")

# Mostrar [Palabra oculta : _ _ _ _ _ _ _ ]
label_palabra = tk.Label(ventana, text=' '.join(palabra_mostrada), font=('Arial', 20))
label_palabra.pack(pady=10)

# Instrucción Label = Etiqueta
label_instruccion = tk.Label(ventana, text="Introduce una letra:", font=('Arial', 14))
label_instruccion.pack()

# Entrada para la letra
entrada_letra = tk.Entry(ventana, font=('Arial', 14), width=5)
entrada_letra.pack(pady=5)

# Botón para comprobar la letra
boton_comprobar = tk.Button(ventana, text="Comprobar letra", command=comprobar_letra, font=('Arial', 14))
boton_comprobar.pack(pady=10)

# Mostrar intentos restantes
label_intentos = tk.Label(ventana, text=f"Intentos restantes: {intentos}", font=('Arial', 14))
label_intentos.pack(pady=10)

# Ejecución de la ventana
ventana.mainloop()
