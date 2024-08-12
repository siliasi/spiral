
#life is good Tandeka

import turtle
t  = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(3)
t.speed(13)

col = ('white', 'pink', 'cyan')
for i in range (300):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)