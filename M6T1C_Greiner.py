import turtle

wn = turtle.Screen()
jim = turtle.Turtle()


for i in range(10):
    for i in range(4):
        jim.forward(150)
        jim.right(90)
    jim.right(45)

wn.exitoclick()
