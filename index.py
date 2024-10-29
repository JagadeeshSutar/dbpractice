import turtle

# Function to draw a circle
def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

# Function to draw Gandhi's glasses
def draw_glasses():
    turtle.pendown()
    turtle.pensize(3)
    turtle.goto(-35, 10)
    turtle.circle(15)
    turtle.penup()
    
    turtle.goto(35, 10)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()
    
    turtle.goto(-20, 10)
    turtle.pendown()
    turtle.goto(20, 10)
    turtle.penup()

# Function to draw Gandhi's face
def draw_face():
    draw_circle('peachpuff', 100, 0, -100)  # Face
    draw_circle('black', 10, -35, 25)        # Left eye
    draw_circle('black', 10, 35, 25)         # Right eye
    draw_circle('white', 5, -35, 25)         # Left eye reflection
    draw_circle('white', 5, 35, 25)          # Right eye reflection
    draw_circle('brown', 5, 0, -10)          # Nose

# Function to draw the mouth
def draw_mouth():
    turtle.goto(-30, -30)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.circle(30, 120)  # Mouth curve
    turtle.penup()

# Function to draw the ears
def draw_ears():
    draw_circle('peachpuff', 20, -110, -80)  # Left ear
    draw_circle('peachpuff', 20, 110, -80)   # Right ear

# Function to draw Gandhi's headgear
def draw_headgear():
    turtle.goto(0, 0)
    turtle.setheading(90)
    turtle.pendown()
    turtle.circle(100, 180)  # Half circle for headgear
    turtle.penup()

# Set up the turtle
turtle.speed(5)  # Speed of drawing
turtle.title("Mahatma Gandhi Drawing")

# Draw the representation
draw_face()
draw_glasses()
draw_mouth()
draw_ears()
draw_headgear()

# Hide the turtle and finish
turtle.hideturtle()
turtle.done()
