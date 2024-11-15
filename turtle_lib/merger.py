import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Menger Sponge")
t = turtle.Turtle()
t.speed(0)
t.color("white")
t.hideturtle()

# Function to draw a square
def draw_square(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Recursive function to create the Menger Sponge
def menger_sponge(x, y, size, level):
    if level == 0:
        draw_square(x, y, size)
    else:
        new_size = size / 3
        for i in range(3):
            for j in range(3):
                # Skip the center square
                if i == 1 and j == 1:
                    continue
                menger_sponge(x + i * new_size, y - j * new_size, new_size, level - 1)

# Parameters for the Menger Sponge
initial_size = 200  # Size of the initial square
depth = 3  # Depth of recursion (increase for more detail)

# Start drawing the Menger Sponge
menger_sponge(-initial_size / 2, initial_size / 2, initial_size, depth)

# Finish
turtle.done()
