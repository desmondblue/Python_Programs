import turtle           # allows us to use the turtles library
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle


alex.color("green")    # alex has a color
#alex.right(60)         # alex turns 60 degrees right
#alex.left(60)          # alex turns 60 degrees left
        # draws a circle of radius 50
#draws circles
for counter in range(1,5):
    alex.circle(20*counter)

alex.right(120)
alex.color("blue")

for counter in range(1,5):
    alex.circle(20*counter)
alex.right(120)
alex.color("red")

for counter in range(1,5):
    alex.circle(20*counter)
