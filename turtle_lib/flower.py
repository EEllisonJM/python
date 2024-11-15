from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        right(90)
        circle(150 - j * 6, 90)
        left(90)
        circle(150 - j * 6, 90)
        right(180)
    circle(40, 2)

done()
