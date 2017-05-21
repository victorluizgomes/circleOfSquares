import turtle

myTurtle = turtle.Turtle()
myTurtle.speed(500)

screen = turtle.Screen()
screen = turtle.colormode(255)

turtle.bgcolor(150, 150, 150)

def square(leng):
    for i in range(4):
        myTurtle.forward(leng)
        myTurtle.right(90)   

for i in range(72):
    square(150)
    myTurtle.right(5)

myTurtle.right(2.5)

myTurtle.color("white")

for i in range(72):
    square(150)
    myTurtle.right(5)

for i in range(72):
    square(250)
    myTurtle.right(5)

r = 0
g = 100
b = 255

for i in range(2, 510):
    myTurtle.color(r, g, b)
    if(i % 2 == 0):
        square(100)
    else:
        square(200)
    myTurtle.right(7)
    r = r + 1
    b = b - 1
    g = g + 1
    if(g == 255):
        g = 0
    if(b == 0):
        b = 200
    if(r == 255):
        r = 100
