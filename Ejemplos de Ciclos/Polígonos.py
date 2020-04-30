import turtle 

polygon = turtle.Turtle()

num_lados = int(input("Numero de lados: "))
longitud = int(input("Longitud: "))
angulo = 360.0 / num_lados 

print('')
for i in range(num_lados):
    print("Lado numero " + str(i + 1))
    polygon.forward(longitud)
    polygon.right(angulo)

turtle.done()