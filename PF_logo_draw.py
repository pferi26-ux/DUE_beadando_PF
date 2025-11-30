import turtle
import tkinter as tk

def pf_draw_logo(parent):
    canvas = tk.Canvas(parent, width=600, height=120)
    canvas.pack(pady=10)

    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("white")

    t = turtle.RawTurtle(screen)
    t.hideturtle()
    t.speed(10)
    t.pensize(10)

    t.color("black")
    t.up()
    t.goto(-100, -50)
    t.down()
    t.circle(50)

    t.up()
    t.goto(-120, -38)
    t.setheading(0)
    t.color("red")
    t.down()
    t.write("S  service", font=("Arial", 48, "bold"))

    return canvas