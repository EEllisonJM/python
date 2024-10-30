import tkinter as tk

# Configuración de la ventana
root = tk.Tk()
root.title("Juego de Pong")
WIDTH, HEIGHT = 600, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Configuración de las paletas y la pelota
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
paddle_speed = 20
ball_speed_x, ball_speed_y = 5, 5

# Posiciones iniciales
left_paddle = canvas.create_rectangle(10, HEIGHT//2 - PADDLE_HEIGHT//2, 20, HEIGHT//2 + PADDLE_HEIGHT//2, fill="white")
right_paddle = canvas.create_rectangle(WIDTH - 20, HEIGHT//2 - PADDLE_HEIGHT//2, WIDTH - 10, HEIGHT//2 + PADDLE_HEIGHT//2, fill="white")
ball = canvas.create_oval(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, WIDTH//2 + BALL_SIZE//2, HEIGHT//2 + BALL_SIZE//2, fill="white")

# Puntuación
left_score = 0
right_score = 0
score_text = canvas.create_text(WIDTH // 2, 20, text="0 - 0", font=("Arial", 24), fill="white")

def update_score():
    canvas.itemconfig(score_text, text=f"\nJugador 1 [W/S] - Jugador 2 [⬆️/⬇️]\n{left_score} - {right_score}")

# Movimiento de las paletas
def move_paddle(event):
    if event.keysym == "w":
        canvas.move(left_paddle, 0, -paddle_speed)
    elif event.keysym == "s":
        canvas.move(left_paddle, 0, paddle_speed)
    elif event.keysym == "Up":
        canvas.move(right_paddle, 0, -paddle_speed)
    elif event.keysym == "Down":
        canvas.move(right_paddle, 0, paddle_speed)

# Movimiento de la pelota
def move_ball():
    global ball_speed_x, ball_speed_y, left_score, right_score

    # Mover la pelota
    canvas.move(ball, ball_speed_x, ball_speed_y)
    ball_pos = canvas.coords(ball)
    left_paddle_pos = canvas.coords(left_paddle)
    right_paddle_pos = canvas.coords(right_paddle)

    # Rebote en la parte superior e inferior
    if ball_pos[1] <= 0 or ball_pos[3] >= HEIGHT:
        ball_speed_y *= -1

    # Rebote en las paletas
    if (ball_pos[0] <= left_paddle_pos[2] and left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[3]) or \
       (ball_pos[2] >= right_paddle_pos[0] and right_paddle_pos[1] < ball_pos[3] < right_paddle_pos[3]):
        ball_speed_x *= -1

    # Puntos y reinicio de la pelota
    if ball_pos[0] <= 0:
        right_score += 1
        reset_ball()
    elif ball_pos[2] >= WIDTH:
        left_score += 1
        reset_ball()

    update_score()
    root.after(30, move_ball)

def reset_ball():
    global ball_speed_x, ball_speed_y
    canvas.coords(ball, WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, WIDTH//2 + BALL_SIZE//2, HEIGHT//2 + BALL_SIZE//2)
    ball_speed_x *= -1

# Asignar teclas
root.bind("<KeyPress-w>", move_paddle)
root.bind("<KeyPress-s>", move_paddle)
root.bind("<KeyPress-Up>", move_paddle)
root.bind("<KeyPress-Down>", move_paddle)

# Iniciar el juego
move_ball()
root.mainloop()
