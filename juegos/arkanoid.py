import tkinter as tk
import random

# Configuración de la ventana
root = tk.Tk()
root.title("Arkanoid")
WIDTH, HEIGHT = 600, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Configuración de la paleta
paddle_width, paddle_height = 80, 10
paddle = canvas.create_rectangle(WIDTH // 2 - paddle_width // 2, HEIGHT - 30, 
                                 WIDTH // 2 + paddle_width // 2, HEIGHT - 20, fill="white")
paddle_speed = 20

# Configuración de la pelota
ball_size = 15
ball = canvas.create_oval(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, 
                          WIDTH // 2 + ball_size // 2, HEIGHT // 2 + ball_size // 2, fill="red")
ball_speed_x = random.choice([-5, 5])
ball_speed_y = -5

# Configuración de bloques
block_rows, block_columns = 5, 8
block_width = WIDTH // block_columns
block_height = 20
blocks = []

for row in range(block_rows):
    for col in range(block_columns):
        x1 = col * block_width
        y1 = row * block_height
        x2 = x1 + block_width
        y2 = y1 + block_height
        block = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", tags="block")
        blocks.append(block)

# Movimiento de la paleta
def move_paddle(event):
    x = canvas.coords(paddle)
    if event.keysym == "Left" and x[0] > 0:
        canvas.move(paddle, -paddle_speed, 0)
    elif event.keysym == "Right" and x[2] < WIDTH:
        canvas.move(paddle, paddle_speed, 0)

# Movimiento de la pelota
def move_ball():
    global ball_speed_x, ball_speed_y

    # Mover la pelota
    canvas.move(ball, ball_speed_x, ball_speed_y)
    ball_pos = canvas.coords(ball)

    # Rebote en las paredes laterales
    if ball_pos[0] <= 0 or ball_pos[2] >= WIDTH:
        ball_speed_x *= -1

    # Rebote en la parte superior
    if ball_pos[1] <= 0:
        ball_speed_y = abs(ball_speed_y)  # Asegurarse de que baje
    
    # Si la pelota cae fuera de la pantalla
    if ball_pos[3] >= HEIGHT:
        game_over("¡Juego Terminado!")

    # Rebote en la paleta
    paddle_pos = canvas.coords(paddle)
    if (ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and 
        ball_pos[3] >= paddle_pos[1] and ball_pos[1] <= paddle_pos[3]):
        ball_speed_y = -abs(ball_speed_y)  # Asegurarse de que suba
    
    # Colisión con los bloques
    hit_block = canvas.find_overlapping(ball_pos[0], ball_pos[1], ball_pos[2], ball_pos[3])
    for block in hit_block:
        if "block" in canvas.gettags(block):
            canvas.delete(block)
            blocks.remove(block)
            ball_speed_y *= -1
            break

    # Verificar si se han roto todos los bloques
    if not blocks:
        game_over("¡Felicidades! Has ganado")

    # Mover la pelota después de un intervalo
    root.after(30, move_ball)

# Fin del juego
def game_over(message):
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text=message, font=("Arial", 24), fill="white")
    canvas.unbind("<Left>")
    canvas.unbind("<Right>")

# Asignar teclas para mover la paleta
root.bind("<Left>", move_paddle)
root.bind("<Right>", move_paddle)

# Iniciar el movimiento de la pelota
move_ball()

root.mainloop()
