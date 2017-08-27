import turtle
import math

turtle.speed(0)
turtle.hideturtle()

def phyllotaxis (angle = 137.508, cspread = 2):
    angle_rad = math.radians(angle)
    counter = 0

    while True:
        r = cspread * math.sqrt(counter)
        theta = counter * angle_rad

        x = r * math.cos(theta)
        y = r * math.sin(theta)

        turtle.up()
        turtle.setpos(x, y)
        turtle.down()

        change_color = math.floor(counter % 225)
        #turtle.color((100, change_color, 150))
        #turtle.fillcolor((100, change_color, 150))

        turtle.begin_fill()
        turtle.circle(3)
        turtle.end_fill()
        counter += 1
phyllotaxis(137.508, 5)
