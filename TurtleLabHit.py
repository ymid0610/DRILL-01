import turtle
import random

def drunken_move():
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(10,100))
    turtle.stamp()

turtle.shape('turtle')

turtle.onkey(drunken_move, ' ')
turtle.listen()
turtle.mainloop()