from turtle import Turtle
from random import randint

laura = Turtle()

laura.color('red')
laura.shape('turtle')

laura.penup()
laura.goto(-160,100)
laura.pendown()

rik = Turtle ()

rik.color ('green')
rik.shape ('turtle')

rik.penup()
rik.goto(-160,70)
rik.pendown()

lauren = Turtle ()

lauren.color ('blue')
lauren.shape ('turtle')

lauren.penup()
lauren.goto(-160,10)
lauren.pendown()

carry = Turtle ()

carry.color ('pink')
carry.shape ('turtle')

carry.penup()
carry.goto(-160,40)
carry.pendown()

for movement in range(100):
    laura.forward(randint(1,15))
    lauren.forward(randint(1,15))
    rik.forward(randint(1,15))
    carry.forward(randint(1,15))

input("Press Enter to close")