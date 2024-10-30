import tkinter as tk

# Configuración de la ventana
root = tk.Tk()
root.title("Juego de Laberinto")
WIDTH, HEIGHT = 400, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Configuración del laberinto
maze = [
    "1111111111111111",
    "1000000000000011",
    "1011111111100011",
    "1000000000100011",
    "1110111010100011",
    "1000100010100011",
    "1011101110100011",
    "1010001000100011",
    "1010111011111011",
    "1000000010000011",
    "1111111111111111"
]
CELL_SIZE = 25
player_position = [1, 1]  # Posición inicial
exit_position = [9, 14]   # Posición de la salida

# Dibujar el laberinto
def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = "black" if cell == "1" else "white"
            canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, 
                                    (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill=color)
    # Dibujar al jugador
    canvas.create_oval(player_position[1] * CELL_SIZE, player_position[0] * CELL_SIZE,
                       (player_position[1] + 1) * CELL_SIZE, (player_position[0] + 1) * CELL_SIZE, 
                       fill="blue", tags="player")
    # Dibujar la salida
    canvas.create_rectangle(exit_position[1] * CELL_SIZE, exit_position[0] * CELL_SIZE,
                            (exit_position[1] + 1) * CELL_SIZE, (exit_position[0] + 1) * CELL_SIZE, 
                            fill="green", tags="exit")

# Movimiento del jugador
def move_player(dx, dy):
    new_x = player_position[1] + dx
    new_y = player_position[0] + dy

    # Verificar que no se salga del laberinto ni choque con muros
    if maze[new_y][new_x] == "0":
        player_position[0] = new_y
        player_position[1] = new_x
        canvas.coords("player", new_x * CELL_SIZE, new_y * CELL_SIZE, 
                      (new_x + 1) * CELL_SIZE, (new_y + 1) * CELL_SIZE)
        
        # Verificar si ha llegado a la salida
        if player_position == exit_position:
            canvas.create_text(WIDTH // 2, HEIGHT // 2, text="¡Has ganado!", font=("Arial", 24), fill="green")

# Controles del jugador
def on_key_press(event):
    if event.keysym == "Up":
        move_player(0, -1)
    elif event.keysym == "Down":
        move_player(0, 1)
    elif event.keysym == "Left":
        move_player(-1, 0)
    elif event.keysym == "Right":
        move_player(1, 0)

# Inicializar el juego
draw_maze()
root.bind("<KeyPress>", on_key_press)
root.mainloop()
