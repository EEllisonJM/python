import tkinter as tk
from tkinter import messagebox

# Configuración de la ventana
root = tk.Tk()
root.title("Juego de Gato")
root.geometry("300x350")

# Variables
current_player = "X"
buttons = []

# Función para verificar si hay un ganador
def check_winner():
    # Combinaciones ganadoras
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
        (0, 4, 8), (2, 4, 6)              # diagonales
    ]
    for combo in winning_combinations:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            return True
    return False

# Función para manejar el clic en un botón
def on_button_click(index):
    global current_player
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Fin del Juego", f"¡Jugador {current_player} ha ganado!")
            reset_game()
        elif all(button["text"] != "" for button in buttons):
            messagebox.showinfo("Fin del Juego", "¡Es un empate!")
            reset_game()
        else:
            # Cambiar de jugador
            current_player = "O" if current_player == "X" else "X"

# Función para reiniciar el juego
def reset_game():
    global current_player
    current_player = "X"
    for button in buttons:
        button["text"] = ""

# Crear los botones del tablero
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, command=lambda i=i: on_button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Botón para reiniciar el juego
reset_button = tk.Button(root, text="Reiniciar Juego", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
