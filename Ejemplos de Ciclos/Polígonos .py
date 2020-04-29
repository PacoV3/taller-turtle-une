import turtle 

polygon = turtle.Turtle()

num_sides = int(input("Numero de lados: "))
side_length = int(input("Longitud: "))
angle = 360.0 / num_sides 

for i in range(num_sides):
	polygon.forward(side_length)
	polygon.right(angle)

turtle.done()
