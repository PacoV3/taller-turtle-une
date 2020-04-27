import turtle
t = turtle.Turtle()
t.color("red","yellow")
t.speed(30)
i=0
t.begin_fill()
while True:
  t.forward(200)
  t.left(170)
  i+=1
  if i >36:
    break
t.end_fill()
t.done()