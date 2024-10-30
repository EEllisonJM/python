import tkinter as tk
import random

# Configuración de la ventana
root = tk.Tk()
root.title("Carrera de Autos")
WIDTH, HEIGHT = 300, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="gray")
canvas.pack()

# Configuración de los autos
car_width, car_height = 40, 80
player_car = canvas.create_rectangle(WIDTH//2 - car_width//2, HEIGHT - car_height - 10, 
                                     WIDTH//2 + car_width//2, HEIGHT - 10, fill="blue")
enemy_car_speed = 5
player_speed = 15
score = 0
enemy_cars = []

# Texto de puntuación
score_text = canvas.create_text(50, 10, text=f"Puntuación: {score}", font=("Arial", 12), fill="white")

def create_enemy_car():
    x_position = random.randint(0, WIDTH - car_width)
    enemy_car = canvas.create_rectangle(x_position, 0, x_position + car_width, car_height, fill="red")
    enemy_cars.append(enemy_car)
    root.after(2000, create_enemy_car)

def move_enemy_cars():
    global score
    for car in enemy_cars:
        canvas.move(car, 0, enemy_car_speed)
        car_pos = canvas.coords(car)
        if car_pos[1] >= HEIGHT:
            canvas.delete(car)
            enemy_cars.remove(car)
            score += 1
            canvas.itemconfig(score_text, text=f"Puntuación: {score}")
        elif check_collision(car_pos):
            game_over()
            return
    root.after(50, move_enemy_cars)

def check_collision(car_pos):
    player_pos = canvas.coords(player_car)
    if (player_pos[2] > car_pos[0] and player_pos[0] < car_pos[2] and 
        player_pos[3] > car_pos[1] and player_pos[1] < car_pos[3]):
        return True
    return False

def move_player(event):
    player_pos = canvas.coords(player_car)
    if event.keysym == "Left" and player_pos[0] > 0:
        canvas.move(player_car, -player_speed, 0)
    elif event.keysym == "Right" and player_pos[2] < WIDTH:
        canvas.move(player_car, player_speed, 0)

def game_over():
    canvas.create_text(WIDTH//2, HEIGHT//2, text="¡Juego Terminado!", font=("Arial", 20), fill="white")
    for car in enemy_cars:
        canvas.delete(car)
    enemy_cars.clear()

# Asignar teclas para mover el auto
root.bind("<Left>", move_player)
root.bind("<Right>", move_player)

# Iniciar el juego
create_enemy_car()
move_enemy_cars()

root.mainloop()
