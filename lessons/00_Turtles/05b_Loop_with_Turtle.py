
"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
for i in range(500):
    tina.forward(150)
    tina.left(90)
    print('Loop Iteration', i)
tina.right(45)
tina.penup()
tina.forward(40)
tina.speed(1)
tina.write(".          That took a long time!")




















































































































































































































































































































































































































































































turtle.exitonclick()                    # Close the window when we click on it
