import tkinter as tk
import random
from tkinter import messagebox

# Función para manejar la selección de una carta
def seleccionar_carta(fila, columna):
    global primera_seleccion, segunda_seleccion, botones

    # Si ya se han seleccionado dos cartas, no permitir más selecciones
    if segunda_seleccion is not None:
        return

    # Mostrar el valor de la carta
    botones[fila][columna].config(text=tablero[fila][columna], state="disabled")

    # Registrar la primera y segunda selección
    if primera_seleccion is None:
        primera_seleccion = (fila, columna)
    else:
        segunda_seleccion = (fila, columna)

        # Comparar las dos cartas seleccionadas después de una breve pausa
        ventana.after(500, comparar_cartas)

# Función para comparar las dos cartas seleccionadas
def comparar_cartas():
    global primera_seleccion, segunda_seleccion, botones

    f1, c1 = primera_seleccion
    f2, c2 = segunda_seleccion

    # Si las cartas son iguales, deshabilitarlas permanentemente
    if tablero[f1][c1] == tablero[f2][c2]:
        botones[f1][c1].config(state="disabled")
        botones[f2][c2].config(state="disabled")
    else:
        # Si no son iguales, ocultarlas de nuevo
        botones[f1][c1].config(text="", state="normal")
        botones[f2][c2].config(text="", state="normal")

    # Resetear las selecciones
    primera_seleccion = None
    segunda_seleccion = None

    # Comprobar si se han encontrado todas las parejas
    if todas_las_cartas_encontradas():
        messagebox.showinfo("¡Ganaste!", "¡Has encontrado todas las parejas!")

# Función para verificar si todas las cartas han sido encontradas
def todas_las_cartas_encontradas():
    for fila in botones:
        for boton in fila:
            if boton["state"] != "disabled":
                return False
    return True

# Crear el tablero del juego (4x4) con parejas de números
valores_cartas = list(range(1, 9)) * 2
random.shuffle(valores_cartas)
tablero = [valores_cartas[i:i+4] for i in range(0, 16, 4)]

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Memorama")

# Variables para la primera y segunda selección de cartas
primera_seleccion = None
segunda_seleccion = None

# Crear los botones para representar las cartas
botones = []
for fila in range(4):
    fila_botones = []
    for columna in range(4):
        boton = tk.Button(ventana, text="", width=10, height=5, command=lambda f=fila, c=columna: seleccionar_carta(f, c))
        boton.grid(row=fila, column=columna)
        fila_botones.append(boton)
    botones.append(fila_botones)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
