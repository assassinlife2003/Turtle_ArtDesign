import turtle
bob = turtle.Turtle()
turtle.colormode(255)
bob.speed(0)
turtle.bgcolor("black")

from designs2 import *
from random import *
from myShape import *
turtle.tracer(0)



bgdesign(bob)
spiny(bob)
spiral(bob)

