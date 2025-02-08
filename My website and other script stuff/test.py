import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.color("black")

# Draw a square
for _ in range(4):
    t.goto(0,0)
    t.forward(500)
    t.right(90)

# Draw a circle
#t.penup()
#t.goto(150, 0)  # Move to a new position
#t.pendown()
#t.circle(50)

# Finish
turtle.done()