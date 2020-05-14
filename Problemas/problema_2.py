import turtle

tortuga = turtle.Turtle()
tortuga.shape("turtle")

longitud = int(input("Longitud de las figura: "))

lado_sup_inf = 100
lado_izq_der = 40
angulo = 90

# Cuadrado
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

# Rectángulo
tortuga.begin_fill()

tortuga.forward(lado_sup_inf)
tortuga.left(angulo)
tortuga.forward(lado_izq_der)
tortuga.left(angulo)
tortuga.forward(lado_sup_inf)
tortuga.left(angulo)
tortuga.forward(lado_izq_der)
tortuga.left(angulo)

tortuga.end_fill()

tortuga.penup()
tortuga.forward(200)
tortuga.pendown()

# Triángulo Eq.
tortuga.begin_fill()

tortuga.forward(lado_sup_inf)
tortuga.left(angulo+30)
tortuga.forward(lado_sup_inf)
tortuga.left(angulo+30)
tortuga.forward(lado_sup_inf)

tortuga.end_fill()