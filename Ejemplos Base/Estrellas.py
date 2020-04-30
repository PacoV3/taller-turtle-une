import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(100)


def estrella(tamano, t):
    if tamano <= 0:
        return
    else:
        i = 0
        while i < 5:
            t.forward(tamano)
            estrella(tamano / 3, t)
            t.left(216)
            i = i + 1

size = int(input("Ingresa una medida: "))
estrella(size, t)
turtle.done()
