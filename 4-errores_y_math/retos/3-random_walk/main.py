import turtle
from random import choice

def random_walk(side = 25):
    turtle.speed(5)
    while True:
        turtle.right(choice([0, 90, 180, 270]))
        turtle.forward(side)

random_walk()
