import turtle
wn = turtle.Screen()
tu = turtle.Turtle()
tu1 = turtle.Turtle()
tu2 = turtle.Turtle()
tu3 = turtle.Turtle()
x = 50
tu.hideturtle()
tu1.hideturtle()
tu2.hideturtle()
tu3.hideturtle()
for i in range(0,90):
    tu.speed(10)
    tu1.speed(10)
    tu2.speed(10)
    tu3.speed(10)
    tu.penup()
    tu2.penup()
    tu3.penup()
    tu2.right(90)
    tu3.left(90)
    tu2.forward(x)
    tu.forward(x)
    tu3.forward(x)
    tu2.pendown()
    tu3.pendown()
    tu1.penup()
    tu1.forward(x)
    tu.right(90)
    tu1.left(90)
    tu2.right(90)
    tu3.left(90)
    tu2.forward(x)
    tu3.forward(x)
    tu.pendown()
    tu.forward(x)
    tu1.pendown()
    tu1.forward(x)
    tu2.right(90)
    tu3.left(90)
    tu2.forward(x)
    tu3.forward(x)
    tu.right(90)
    tu1.left(90)
    tu.forward(x)
    tu1.forward(x)
    tu.right(90)
    tu1.left(90)
    tu.penup()
    tu1.penup()
    tu2.right(90)
    tu3.left(90)
    tu2.forward(x)
    tu3.forward(x)
    tu.forward(x)
    tu1.forward(x)
    tu.right(90)
    tu1.left(90)
    tu2.right(90)
    tu3.left(90)
    tu.pendown()
    tu1.pendown()
    x = x + 3
wn.mainloop()