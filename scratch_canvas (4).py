import turtle

length = int(input('enter the value for length'))
breadth = int(input('enter the value for breadth'))
for i in range(0, 2):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(breadth)
    turtle.left(90)
