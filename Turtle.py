# Description: 
# Author: Landon
# Date: Feb 17, 2025 - Feb 26, 2025

# Program Library
import turtle # This library is used to create drawings/graphics with in python.

# Program Constant
t = turtle.Turtle()

# Display for drawing
turtle.setup(width=500, height=500, startx=500, starty=200) # This fuction is used to create the window in which the "turtle" will draw on.

# User Input(s)
while True:

    Shape = input("What shape would you like to draw? (Square, Triangle, Circle, or Star): ").title()
    if Shape != "Square" and Shape != "Triangle" and Shape != "Circle" and Shape != "Star":
        print("   Data Entry Error - Please enter a valid shape.")
    else:
        print("   You have selected to draw a", Shape + ".")

    while True:
        if Shape == "Square":
            t.speed(1)
            t.color("blue")
            
            for i in range(4):
                t.forward(100)
                t.right(90)
        else:
            break

    while True:
        if Shape == "Triangle":
            t.speed(1) 
            t.color("red")
                
            for i in range(3):
                t.forward(100)
                t.right(120)
        else:
            break

    while True:
        if Shape == "Circle":
            t.speed(1)     
            t.color("green")
            t.circle(100)
        else:
            break

    while True:
        if Shape == "Star":
            t.speed(1)                
            t.color("yellow")
                            
            for i in range(5):
                t.forward(100)
                t.right(144)
        else:
            break