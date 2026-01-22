import turtle
import colorsys

# Setup the screen
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)  # Fastest speed

n = 36  # Number of loops
h = 0  # Hue

# The animation loop
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1 / n
    t.color(c)
    t.left(10)
    for j in range(5):  # Draw simple shape
        t.forward(200)
        t.left(144)

    # Check if user closed window to prevent errors
    if not t.getscreen().getcanvas().winfo_exists():
        break

turtle.done()