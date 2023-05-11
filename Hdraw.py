import turtle

# create a turtle object
t = turtle.Turtle()

# draw the house structure
t.penup()
t.goto(-100, 0)
t.pendown()
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)

# draw the roof
t.penup()
t.goto(-100, 200)
t.pendown()
t.left(45)
t.forward(141.4)
t.left(90)
t.forward(141.4)

# draw the door
t.penup()
t.goto(-40, 0)
t.pendown()
t.setheading(0)
t.forward(40)
t.left(90)
t.forward(80)
t.left(90)
t.forward(40)

# draw the window
t.penup()
t.goto(60, 100)
t.pendown()
t.setheading(0)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)

# hide the turtle cursor
t.hideturtle()

# keep the window open until closed manually
turtle.done()
