import turtle
from random import randint

t = turtle.Turtle()
t.shape('turtle')
t.speed(3)

a = 1
b = 5
numero = randint(a, b)
respuesta = int(input("Adivina un numero del " + str(a) + " al " + str(b) + ": "))

if respuesta == numero:
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(141)
    print("Correcto! la respuesta era " + str(numero))
else:
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    print("La respuesta correcta era " + str(numero))

turtle.done()
