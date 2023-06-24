#importe a biblioteca
import turtle

#definindo as cores
colors = ['purple', 'blue', 'green', 'pink', 'yellow', 'orange']

#instaciando a biblioteca (turtle) e definindo a cor do background
t = turtle.Pen()
turtle.bgcolor('black')

#os movimentos:
for x in range(200): #você pode escolher o numero de interações
    #definindo a cor
    t.pencolor(colors[x%6])
    #defina a largura
    t.width(x/100+1)
    #movimentando o turtle
    t.forward(x)
    #girando o turtle
    t.left(59)