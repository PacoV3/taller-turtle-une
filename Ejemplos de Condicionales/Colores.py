import turtle

colores = ["green","pink","red","blue"]

print("Elige dos colores del 0 al 3: ")
valor_1 = int(input("Color de la primera tortuga: "))
valor_2 = int(input("Color de la segunda tortuga: "))

color_1 = colores[valor_1]
color_2 = colores[valor_2]

# Primera Tortuga
tortuga_uno = turtle.Turtle()
tortuga_uno.shape('turtle')

tortuga_uno.color(color_1)
tortuga_uno.forward(50)

if  color_1 == "blue" or color_1 == "pink":
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

# Segunda Tortuga
tortuga_dos = turtle.Turtle()
tortuga_dos.shape('turtle')

tortuga_dos.color(color_2)
tortuga_dos.forward(60)

if color_2 == "blue" or color_2 == "pink" :
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
