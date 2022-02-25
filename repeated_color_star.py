import turtle
import colorsys

sc = turtle.Screen()
sc.setup(600, 600)
spiral = turtle.Turtle()
spiral.speed(0)

sc.bgcolor("black")
h = 0
n = 50
c = 0

for i in range(360):
    col = colorsys.hsv_to_rgb(h, 1, 0.8)
    spiral.forward(i * 10)
    spiral.right(144)
    spiral.color(col)
    h += 1 / n
