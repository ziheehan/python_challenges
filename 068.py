import turtle
import random
lines = random.randint(5, 20)
for i in range(0, lines) :
    length = random.randint(25,100)
    rotate = random.randint(1, 360)
    turtle.forward(length)
    turtle.right(rotate)
