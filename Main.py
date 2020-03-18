import pygame as py
import numpy as np
import turtle

#Setando o Mapa do Labirinto
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Labirinto")
wn.setup(700, 700)

#Registrando os GIFS
turtle.register_shape("person.gif")
turtle.register_shape("wall.gif")
turtle.register_shape("finish.gif")


#Criando uma Caneta

class Pen (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class Checkpoint (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("finish.gif")
        self.color("red")
        self.penup()
        self.speed(0)

#Criando um Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("person.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0



    def subir(self):
        mover_para_x = player.xcor()
        mover_para_y = player.ycor() +24
        if(mover_para_x, mover_para_y) not in walls:
            self.goto(self.xcor(), self.ycor()+24)
            self.gold += 1
    def descer(self):
        mover_para_x = player.xcor()
        mover_para_y = player.ycor() - 24
        if(mover_para_x, mover_para_y) not in walls:
            self.goto(self.xcor(), self.ycor()-24)
            self.gold += 1
    def esquerda(self):
        mover_para_x = player.xcor() - 24
        mover_para_y = player.ycor()
        if(mover_para_x, mover_para_y) not in walls:
            self.goto(self.xcor() -24, self.ycor())
            self.gold += 1
    def direita(self):
        mover_para_x = player.xcor() +24
        mover_para_y = player.ycor()
        if(mover_para_x, mover_para_y) not in walls:
            self.goto(self.xcor() +24,self.ycor())
            self.gold += 1

class Treasure(turtle.Turtle):
    def __int__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()






#Creat Levels List

levels = [""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XP   X                X",
    "XXXX X		XXXX X  X     X",
    "X    XXXXXXX    X  X  X",
    "XXXX       X  XXX     X",
    "X  X  X    X  X   XXXXX",
    "X  XXXX   XX  X X     X",
    "X  X    X   X X X     X",
    "X  X    XXX X X XXX   X",
    "X      XX          X  X",
	  "XXXX X  X   XXXXX  X  X",
	  "X    X    X           X",
    "XXXXXXXXXXXXXXXXXXXXCXX"
]


treasures = []

levels.append(level_1)

def setup_labirinto(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                #Condição de coordenadas para travar as paredes
                walls.append((screen_x, screen_y))
            if character == "P":
                player.goto(screen_x, screen_y)
            if character == "C":
                checkpoing.goto(screen_x, screen_y)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))





#Class Pen
pen = Pen()
player = Player()
checkpoing = Checkpoint()



#Criando uma Lista de cordenadas para restrição da parede
walls = []

#Setando o Mapa
setup_labirinto(level_1)

#Instancia das Teclas
turtle.listen()
turtle.onkey(player.esquerda, "Left")
turtle.onkey(player.direita, "Right")
turtle.onkey(player.subir, "Up")
turtle.onkey(player.descer, "Down")


wn.tracer(0)

while True:
    if(player.xcor() == 192 and player.ycor()==0):
        print("Quantidade de Movimentos: "+str(player.gold))
        print("YOU WIN")
        if player.gold <= 30:
            print("Você resolveu o Labirinto utilizano o melhor caminho, PARABÉNS!! Você receberá a maior pontuação!!")
        break
    wn.update()



