import turtle
import math

t = turtle.Turtle()
r = 200
while(1):
    n = int(input(()))
    p = 180*(n-2)/(n*2)
    c = math.cos(math.radians(p))
    l = r * c
    t.reset()
    for i in range(n):
        t.forward(l)
        t.left(180-180*(n-2)/n)
