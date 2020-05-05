import turtle

tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("green")

lista_colores = ["plum", "salmon", "dark turquoise", "tan", "olive drab", "gold", "slate blue", "indigo", "khaki", "dark gray"]

# Triángulo.
print(lista_colores)
print(" ")
print("Nota: Para elegir un color de la lista ingresa su posicion la cual siempre empieza desde cero (en este caso del 0 al 9).")
print(" ")
color = int(input("Elige un color: "))
tortuga.color(lista_colores[color])

tortuga.begin_fill()

tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)
tortuga.left(120)

tortuga.end_fill()

tortuga.penup()
tortuga.forward(200)
tortuga.pendown()

# Cuadrado
color = int(input("Elige un color: "))
tortuga.color(lista_colores[color])

tortuga.begin_fill()

tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)

tortuga.end_fill()

tortuga.penup()
tortuga.forward(200)
tortuga.pendown()

# Pentágono
color = int(input("Elige un color: "))
tortuga.color(lista_colores[color])

tortuga.begin_fill()

tortuga.forward(100)
tortuga.left(72)
tortuga.forward(100)
tortuga.left(72)
tortuga.forward(100)
tortuga.left(72)
tortuga.forward(100)
tortuga.left(72)
tortuga.forward(100)
tortuga.left(72)

tortuga.end_fill()

turtle.done()
