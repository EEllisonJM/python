import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)

# Function to draw a petal
def draw_petal():
    t.color("red")
    t.begin_fill()
    t.circle(100, 60)  # Draw half a circle
    t.left(120)        # Angle for petal shape
    t.circle(100, 60)
    t.left(120)
    t.end_fill()

# Draw the flower with multiple petals
for _ in range(6):  # Number of petals
    draw_petal()
    t.right(60)      # Angle between petals

# Draw the center of the flower
t.color("yellow")
t.begin_fill()
t.circle(50)         # Circle at the center
t.end_fill()

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
