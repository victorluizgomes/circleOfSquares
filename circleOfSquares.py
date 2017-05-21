import turtle

# initializes turtle and the speed of the drawing
myTurtle = turtle.Turtle()
myTurtle.speed(500)

# initializes the screen and sets the color more to strings from 0 to 255
screen = turtle.Screen()
screen = turtle.colormode(255)

# sets background color to a darkish gray 
turtle.bgcolor(150, 150, 150)

# defines a function that draws a square
def square(leng):
    for i in range(4):
        myTurtle.forward(leng)
        myTurtle.right(90)   

# draws 72 squares with 150 lenght each and 5 degrees angle from each other
# P.S: 5 * 72 = 360 (making a perfect circle)
for i in range(72):
    square(150)
    myTurtle.right(5)

# make an adtional angle of 2.5 so the next squares
# are not being drawn on top of the previous ones
myTurtle.right(2.5)

myTurtle.color("white") 

# draws another perfect circle but now white instead of black
for i in range(72):
    square(150)
    myTurtle.right(5)

# draws a perfect circle 100 of lenght bigger than before
for i in range(72):
    square(250)
    myTurtle.right(5)

# sets red, green, blue for some interesting colors
r = 0
g = 100
b = 255

# draws 510 squares that alternates to be smaller than the 2 previos circles
# and in between them. it alternates in an angle of 7 which is not divisible by 360.
for i in range(510):
    myTurtle.color(r, g, b)
    if(i % 2 == 0):
        square(100)
    else:
        square(200)
    myTurtle.right(7)
    r = r + 1
    b = b - 1
    g = g + 1
    # it has checks for boundries on red, green and blue variables.
    if(r == 255):
        r = 100
    if(g == 255):
        g = 0
    if(b == 0):
        b = 200
    
