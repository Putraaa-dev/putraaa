import turtle
screen = turtle.Screen()
screen.title("Pohon Fibonacci")
t = turtle.Turtle()
t.speed(0)


def pohon_fibonacci(t, panjang_cabang, kedalaman):
    if kedalaman == 0:
        return
    t.forward(panjang_cabang)
    t.left(30)
    pohon_fibonacci(t, panjang_cabang * 0.6, kedalaman - 1)
    t.right(60)
    pohon_fibonacci(t, panjang_cabang * 0.6, kedalaman - 1)
    t.left(30)
    t.backward(panjang_cabang)


t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")

pohon_fibonacci(t, 100, 5)

t.hideturtle()
turtle.done()
