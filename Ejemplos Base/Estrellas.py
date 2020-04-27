import turtle

t = turtle.Turtle()
t.speed(100)

def estrella(tamano, t):
  if tamano <= 0:
    return
  else:
    for figura in range(5):
      t.forward(tamano)
      estrella(tamano/3,t)
      t.left(216)

size = int(input("Ingresa una medida: "))
estrella(size,t)

turtle.done()
