#Kiavash Niknam
import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Colorful Triangle with Circles")

# Create turtle
t = turtle.Turtle()
t.speed(3)
t.penup()
t.goto(0, 100)
t.pendown()

# Draw triangle
t.color("blue")
t.fillcolor("yellow")
t.begin_fill()

t.goto(-100, -70)
t.goto(100, -70)
t.goto(0, 100)

t.end_fill()

# Circle positions and colors
circles = [
    (0, 100, "pink"),
    (-100, -70, "lightgreen"),
    (100, -70, "skyblue")
]

# Draw colorful circles
for x, y, color in circles:
    t.penup()
    t.goto(x, y - 20)
    t.pendown()

    t.color("red", color)
    t.begin_fill()
    t.circle(20)
    t.end_fill()

# Finish drawing
t.hideturtle()
turtle.done()
