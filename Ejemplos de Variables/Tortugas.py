import turtle
from random import choice

# Variable con una lista de posibles colores
lista_de_colores = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray']

radio = int(input("De que radio quieres hacer los circulos? "))

t_aleatoria = turtle.Turtle()
t_aleatoria.shape('turtle')

# De la lista de colores elige un color y dibuja un círculo
t_aleatoria.color(choice(lista_de_colores))
t_aleatoria.circle(radio)

# De la lista de colores elige otro color y dibuja un círculo al revés
t_aleatoria.color(choice(lista_de_colores))
t_aleatoria.circle(-radio)

turtle.done()
