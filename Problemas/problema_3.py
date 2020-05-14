import turtle
from random import randint

tortuga = turtle.Turtle()
tortuga.shape("turtle")

longitud = int(input("Longitud de la figura: "))
aleatorio = randint(0,2)

if aleatorio == 0:
  # Cuadrado
  tortuga.color("red")
  tortuga.begin_fill()

  tortuga.forward(longitud)
  tortuga.left(90)
  tortuga.forward(longitud)
  tortuga.left(90)
  tortuga.forward(longitud)
  tortuga.left(90)
  tortuga.forward(longitud)

  tortuga.end_fill()
elif aleatorio == 1:
  # Triángulo
  tortuga.color("blue")
  tortuga.begin_fill()

  tortuga.forward(longitud)
  tortuga.left(120)
  tortuga.forward(longitud)
  tortuga.left(120)
  tortuga.forward(longitud)

  tortuga.end_fill()
else:
  # Rectángulo
  tortuga.color("green")
  tortuga.begin_fill()

  tortuga.forward(longitud)
  tortuga.left(90)
  tortuga.forward(longitud/2)
  tortuga.left(90)
  tortuga.forward(longitud)
  tortuga.left(90)
  tortuga.forward(longitud/2)

  tortuga.end_fill()

turtle.done()
