from turtle import Screen
from squares import Squares
import math
import numpy as np
import time

x_centre = 0
y_centre = 0
scale = 1
r = 300 // scale
steps = 1

screen = Screen()
screen.bgcolor("white")
screen.setup(width=1920 // scale, height=1080 // scale)
screen.title("Pendulum")
screen.tracer(0)
square_positions = [(-860 // scale, -420 // scale),
                    (-860 // scale, 420 // scale),
                    (860 // scale, -420 // scale),
                    (860 // scale, 420 // scale)]

upper_circle = Squares((x_centre // scale, y_centre // scale))
upper_circle.shape("circle")
upper_circle.shapesize(stretch_len=2, stretch_wid=2)

lower_circle = Squares((r, 0))
lower_circle.shape("circle")
lower_circle.shapesize(stretch_len=4, stretch_wid=4)

for square in square_positions:
    square = Squares(square)

input_arr = np.linspace(0, 2 * np.pi, 360)
changed = False
counter = 0
while counter < 6:
    for i in range(len(input_arr)):
        screen.update()
        time.sleep(0.001)
        if i % 4 == 0:
            x_centre += steps // scale
        upper_circle.goto((x_centre, y_centre))
        print(f"Degree: {i}°")
        x = r * math.cos(input_arr[i]) + x_centre
        y = r * math.sin(input_arr[i]) + y_centre
        lower_circle.goto((x, y))
    counter += 1

screen.exitonclick()
