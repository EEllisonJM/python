import tkinter as tk
import random

# Configuración de la ventana
root = tk.Tk()
root.title("Juego de Gusanito")
WIDTH, HEIGHT = 400, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Configuración del gusanito
snake = [(20, 20), (10, 20), (0, 20)]  # Posiciones iniciales
snake_direction = "Right"
snake_speed = 100  # Velocidad en milisegundos
score = 0

# Configuración de la comida
food = None

def place_food():
    global food
    x = random.randint(0, (WIDTH - 10) // 10) * 10
    y = random.randint(0, (HEIGHT - 10) // 10) * 10
    food = (x, y)
    canvas.create_oval(x, y, x + 10, y + 10, fill="red", tags="food")

def mover_snake():
    global score
    # Obtener la posición de la cabeza del gusanito
    head_x, head_y = snake[0]

    # Actualizar la posición de la cabeza según la dirección
    if snake_direction == "Up":
        head_y -= 10
    elif snake_direction == "Down":
        head_y += 10
    elif snake_direction == "Left":
        head_x -= 10
    elif snake_direction == "Right":
        head_x += 10

    # Insertar la nueva cabeza y verificar colisiones
    new_head = (head_x, head_y)
    if new_head in snake or head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        game_over()
        return

    # Agregar la nueva cabeza al cuerpo del gusanito
    snake.insert(0, new_head)
    
    # Verificar si el gusanito ha comido la comida
    if new_head == food:
        score += 1
        canvas.delete("food")
        place_food()
    else:
        # Eliminar la cola si no ha comido
        snake.pop()

    # Redibujar el gusanito
    canvas.delete("snake")
    for x, y in snake:
        canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tags="snake")
    
    # Actualizar la puntuación
    canvas.delete("score")
    canvas.create_text(35, 10, text=f"Score: {score}", fill="white", tags="score")

    # Llamar a la función de movimiento de nuevo después de un tiempo
    root.after(snake_speed, mover_snake)

def cambiar_direccion(nueva_direccion):
    global snake_direction
    if (nueva_direccion == "Up" and snake_direction != "Down") or \
       (nueva_direccion == "Down" and snake_direction != "Up") or \
       (nueva_direccion == "Left" and snake_direction != "Right") or \
       (nueva_direccion == "Right" and snake_direction != "Left"):
        snake_direction = nueva_direccion

def game_over():
    canvas.delete("all")
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="red", font=("Arial", 24))
    canvas.create_text(WIDTH // 2, HEIGHT // 2 + 30, text=f"Score: {score}", fill="white", font=("Arial", 16))

# Asignar teclas para cambiar la dirección del gusanito
root.bind("<Up>", lambda event: cambiar_direccion("Up"))
root.bind("<Down>", lambda event: cambiar_direccion("Down"))
root.bind("<Left>", lambda event: cambiar_direccion("Left"))
root.bind("<Right>", lambda event: cambiar_direccion("Right"))

# Iniciar el juego
place_food()
mover_snake()
root.mainloop()
