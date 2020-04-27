import turtle
from math import sqrt
from random import choice

def coord_list(n, len_side):
  list_of_coords = []

  len_side = len_side / 2
  list_of_coords.append([(0, 0, len_side)])
  y_up = y_down = x_up = 0
  for i in range(1, n):
    len_side = len_side / 2
    list_of_coords.append([])
    for element in list_of_coords[i - 1]:
      x_up = element[0]
      y_up = element[1] + get_h(len_side)
      y_down = y_up - get_h(len_side) * 2
      list_of_coords[i].append((x_up, y_up, len_side))
      list_of_coords[i].append((x_up + len_side, y_down, len_side))
      list_of_coords[i].append((x_up - len_side, y_down, len_side))
  return list_of_coords

def draw_white_t(x, y, l):
  t.up()
  t.setposition(x + l / 2, y)
  t.down()
  t.begin_fill()
  for _ in range(3):
    t.forward(l)
    t.left(120)
  t.end_fill()

def get_h(side):
    return sqrt(side ** 2 - (side / 2) ** 2)

t = turtle.Turtle()
t.pensize(0.1)
t.ht()
t.up()
t.speed(8)

l = 400
h = get_h(l)

t.setposition(-l / 2, -h / 2)
t.down()
t.shape('turtle')
t.st()
n = 0
while n < 1 or n > 7:
  n = int(input('Elige un numero del 1 al 7: '))

t.begin_fill()
for _ in range(3):
    t.forward(l)
    t.left(120)
t.color('black')
t.end_fill()

t.left(180)
t.color('white')

coords = coord_list(n, l)

list_of_colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray']

print('')
for _ in range(len(coords)):
  print('Vuelta numero ' + str(_ + 1))
  for coord in coords[_]:
    t.pencolor(choice(list_of_colors))
    draw_white_t(*coord)
    
print('')
print('Listo!!')
turtle.done()
