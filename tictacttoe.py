# Author: Evan Glazer


# Import Turtle because thats the library we will be using to display the graphics
# Import math to use math.fabs so we can get the absolute value to make the size of the board nice and the boxes
import turtle
import math

# Board calculations
SIZE = -200
INTERVAL = (int(2*math.fabs(SIZE)/3))

def board():

    # Draw the vertical lines of this board.
    for vert in range(SIZE, SIZE+4*INTERVAL, INTERVAL): # SIZE+4*INTERVAL makes make the 4 lines happen vertically.
        turtle.penup()
        turtle.setpos(vert,SIZE)
        turtle.setheading(90)# This heading keeps the angle 90 to make a perfect box
        turtle.pendown()
        turtle.forward(3*INTERVAL) # This makes the line even with the board and allows 3 lines on the board rather than 1 or 2

    # Draws the horizontal lines of this board.
    for horiz in range(SIZE, SIZE+4*INTERVAL, INTERVAL): # SIZE+4*INTERVAL makes make the 4 lines happen horizontally.
        turtle.penup()
        turtle.setpos(SIZE, horiz)
        turtle.setheading(0)# This heading keeps the angle 0 to make a perfect box else if also 90 it would continue to be a straight line
        turtle.pendown()
        turtle.forward(3*INTERVAL)# This makes the line even with the board and allows 3 lines on the board rather than 1 or 2

board()
