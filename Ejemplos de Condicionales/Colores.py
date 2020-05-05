import turtle

colores = ["green","pink","red","blue"]

print("Elige un color: (0 a 3)")
eleccion = int(input("Color de la primera tortuga: "))

eleccion2 = int(input("Color de la segunda tortuga: "))
#Primera Tortuga
tortuga_uno = turtle.Turtle()

tortuga_uno.pencolor(colores[eleccion])
tortuga_uno.forward(50)

if  tortuga_uno.pencolor() == "blue" or tortuga_uno.pencolor() == "pink":
    tortuga_uno.right(60)
    tortuga_uno.forward(100)
    tortuga_uno.right(60)
    tortuga_uno.forward(100)
    tortuga_uno.right(60)
    tortuga_uno.forward(100)
    tortuga_uno.right(60)
    tortuga_uno.forward(100)
    tortuga_uno.right(60)
    tortuga_uno.forward(100)
else:
    tortuga_uno.left(60)
    tortuga_uno.forward(100)

#Segunda Tortuga
tortuga_dos = turtle.Turtle()
tortuga_dos.forward(60)

tortuga_dos.pencolor(colores[eleccion2])
if tortuga_dos.pencolor() == "blue" or tortuga_dos.pencolor() == "pink" :
    tortuga_dos.right(60)
    tortuga_dos.forward(100)
else:
    tortuga_dos.left(60)
    tortuga_dos.forward(100)
    tortuga_dos.left(60)
    tortuga_dos.forward(100)
    tortuga_dos.left(60)
    tortuga_dos.forward(100)
    tortuga_dos.left(60)
    tortuga_dos.forward(100)
    tortuga_dos.left(60)
    tortuga_dos.forward(100)
