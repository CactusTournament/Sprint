# Description: This is a program that shows the uses of the turtle library, which can be used to make drawings.
# Author: Landon - Group 6
# Date: Feb 17, 2025 - Feb 26, 2025

# Program Library
import turtle # This library is used to create drawings/graphics with in python.

# Program Constant
t = turtle.Turtle() # Constant for the turtle object.
# Display for drawing
turtle.setup(width=500, height=500, startx=500, starty=200) # This fuction is used to create the window in which the "turtle" will draw on.

# Art for page (Just for looks)
def print_ascii_title():
    ascii_title = r"""

                        ▀█▀ █░█ █▀█ ▀█▀ █░░ █▀▀
                        ░█░ █▄█ █▀▄ ░█░ █▄▄ ██▄

"""
    print(ascii_title)

def print_ascii_art():
    ascii_art = r"""
                        Thank you for using Turtle.

                              ___-------___                         
                          _-~~             ~~-_                     
                       _-~                    /~-_                  
    /^\__/^\         /~  \                   /    \\                
  /|  O|| O|        /      \_______________/        \\              
 | |___||__|      /       /                \          \\            
 |          \    /      /                    \          \\          
 |   (_______) /______/                        \_________ \\        
 |         / /         \                      /            \\       
  \         \^\\         \                  /               \     / 
    \         ||           \______________/      _-_       //\__//  
      \       ||------_-~~-_ ------------- \ --/~   ~\    || __/    
        ~-----||====/~     |==================|       |/~~~~~       
         (_(__/  ./     /                    \_\      \.            
                (_(___/                         \_____)_)           
    """
    print(ascii_art)

# User Input(s)
print_ascii_title()
while True:
    while True:
        Shape = input("What shape would you like to draw? (Square, Triangle, Circle, or Star): ").title()
        print()
        if Shape in ["Square", "Triangle", "Circle", "Star"]:
            print("   You have selected to draw a", Shape + ".")
            print()
            break
        else:
            print("   Data Entry Error - Please enter a valid shape.")
            print()

    if Shape == "Square":
        t.speed(1) # Controls speed of turtle.
        t.color("blue") # Dictates turtles color.
            
        for i in range(4): # Directions for turtle to make shape.
            t.forward(100)
            t.right(90)

    elif Shape == "Triangle":
        t.speed(1)
        t.color("red")
                
        for i in range(3):
            t.forward(100)
            t.right(120)

    elif Shape == "Circle":
        t.speed(1)
        t.color("green")
        t.circle(100) # Function apart of the turtle library specificly made to make circles.

    elif Shape == "Star":
        t.speed(1)
        t.color("yellow")
                            
        for i in range(5):
            t.forward(100)
            t.right(144)

    while True:
        exitprogram = input("Would you like to draw another shape? (Y or N): ").upper()
        print()
        if exitprogram in ["Y", "N"]:
            break
        else:
            print("   Data Entry Error - Please enter a valid response.")
            print()

    if exitprogram != "Y":
        print()
        print_ascii_art()
        break