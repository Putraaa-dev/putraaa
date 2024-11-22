import turtle
def Trapesium(ttl, x, y, width):
    ttl.penup()
    ttl.goto(x,y)
    ttl.setheading(0)
    ttl.pendown()
    for count in range (4):
        ttl.forward(width)
        ttl.right(90)
    ttl.penup()

Bob = turtle.Turtle()
Bob.speed(5)
Bob.pensize(3)
Trapesium(Bob, 0, 0, 300)
turtle.done()