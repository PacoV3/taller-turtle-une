import turtle

t = turtle.Turtle()
t.shape('turtle')
t.color("red","yellow")
t.speed(30)
i = 0

t.begin_fill()
while i < 36:
	t.forward(200)
	t.left(170)
	i += 1
t.end_fill()

turtle.done()
