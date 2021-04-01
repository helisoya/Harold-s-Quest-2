# Maison Hantée par Julien

from tkinter import *
from random import *

root = Tk()
can = Canvas(root,width=600,height=300,bg="black")
can.pack()



diff = 1

posX = 0
posY = 0

time = diff*2500


def generateMap():

    border = 10*diff
    max_tunnel = 5*border
    curLength = 0
    randLength = randint(2,5)

    CurX = 0
    CurY = 0

    StartPos = [[0,0]]

    map = [[1 for i in range(border)] for i in range(border)]

    while max_tunnel > 0:


        while curLength < randLength:
            ways = [[1,0],[-1,0],[0,1],[0,-1]]
            if CurX <= 0:
                ways.remove([-1,0])
            if CurX >= border-1:
                ways.remove([1,0])
            if CurY <= 0:
                ways.remove([0,-1])
            if CurY >= border-1:
                ways.remove([0,1])

            move = choice(ways)
            map[CurX][CurY] = 0

            CurX+=move[0]
            CurY+=move[1]
            curLength+=1

        curLength = 0
        randLength = randint(2,5)
        max_tunnel-=1

    map[CurX][CurY] = 2

    return map

map_data = generateMap()



def UpdateAffiche():
    tags = ["up_left","up","up_right","left","right","down_left","down","down_right"]
    for tag in tags:
        col = "lightgray"

        if tag == "up_left":
            if posY == 0 or posX == 0 or map_data[posY-1][posX-1] == 1:
                col ="slategrey"
            elif map_data[posY-1][posX-1] == 2:
                col = "slateblue"

        elif tag == "up":
            if posY == 0 or map_data[posY-1][posX] == 1:
                col ="slategrey"
            elif map_data[posY-1][posX] == 2:
                col = "slateblue"

        elif tag == "up_right":
            if posY == 0 or posX == 10*diff-1 or map_data[posY-1][posX+1] == 1:
                col ="slategrey"
            elif map_data[posY-1][posX+1] == 2:
                col = "slateblue"

        elif tag == "left":
            if posX == 0 or map_data[posY][posX-1] == 1:
                col ="slategrey"
            elif map_data[posY][posX-1] == 2:
                col = "slateblue"

        elif tag == "right":
            if posX == 10*diff-1 or map_data[posY][posX+1] == 1:
                col ="slategrey"
            elif map_data[posY][posX+1] == 2:
                col = "slateblue"

        if tag == "down_left":
            if posY == 10*diff-1 or posX == 0 or map_data[posY+1][posX-1] == 1:
                col ="slategrey"
            elif map_data[posY+1][posX-1] == 2:
                col = "slateblue"

        elif tag == "down":
            if posY == 10*diff-1 or map_data[posY+1][posX] == 1:
                col ="slategrey"
            elif map_data[posY+1][posX] == 2:
                col = "slateblue"

        elif tag == "down_right":
            if posY == 10*diff-1 or posX == 10*diff-1 or map_data[posY+1][posX+1] == 1:
                col ="slategrey"
            elif map_data[posY+1][posX+1] == 2:
                col = "slateblue"

        can.itemconfigure(tag,fill=col)

def Input(event):
    global posX,posY
    if event.keycode == 37: # Gauche
        if posX > 0 and map_data[posY][posX-1] != 1:
            posX-=1
    elif event.keycode == 38: # Haut
        if posY > 0 and map_data[posY-1][posX] != 1:
            posY-=1
    elif event.keycode == 39: # Droite
        if posX < 10*diff-1 and map_data[posY][posX+1] != 1:
            posX+=1
    elif event.keycode == 40: # Bas
        if posY <  10*diff-1 and map_data[posY+1][posX] != 1:
            posY+=1

    if posX < 0:
        posX = 0
    elif posX > 10*diff-1:
        posX = 10*diff
    if posY < 0:
        posY = 0
    elif posY > 10*diff-1:
        posY = 10*diff

    UpdateAffiche()
    can.update()

    if map_data[posY][posX] == 2:
        root.unbind("<Up>")
        root.unbind("<Down>")
        root.unbind("<Right>")
        root.unbind("<Left>")
        can.delete("all")
        can.create_text(300,150,text="BRAVO",fill="red")

def SupprSpook():
    can.itemconfigure("spook",text="")


def UpdateTime():
    global time
    time-=1
    can.itemconfigure("time",text="Temps : "+str(round(time/100)))

    if map_data[posY][posX] == 2:
        return

    if time > 0:
        if randint(1,100-diff*5) == 1:
            can.itemconfigure("spook",text="BOUH !")
            root.after(1000,SupprSpook)
        root.after(5,UpdateTime)
    else:
        root.unbind("<Up>")
        root.unbind("<Down>")
        root.unbind("<Right>")
        root.unbind("<Left>")
        can.delete("all")
        can.create_text(300,150,text="PERDU",fill="red")


def NewGame():
    can.delete("all")
    can.create_rectangle(0,0,100,100,fill="gray",tags="up_left")
    can.create_rectangle(100,0,200,100,fill="gray",tags="up")
    can.create_rectangle(200,0,300,100,fill="gray",tags="up_right")

    can.create_rectangle(0,100,100,200,fill="gray",tags="left")
    can.create_rectangle(100,100,200,200,fill="green",tags="center")
    can.create_rectangle(200,100,300,200,fill="gray",tags="right")

    can.create_rectangle(0,200,200,300,fill="gray",tags="down_left")
    can.create_rectangle(100,200,200,300,fill="gray",tags="down")
    can.create_rectangle(200,200,300,300,fill="gray",tags="down_right")

    can.create_text(450,10,text="Temps : ",fill="white",tags="time")
    can.create_text(450,150,text="",fill="red",tags="spook")

    UpdateAffiche()

    root.bind("<Up>",Input)
    root.bind("<Down>",Input)
    root.bind("<Left>",Input)
    root.bind("<Right>",Input)

    UpdateTime()

can.create_text(300,150,text="Fleches du Clavier pour se déplacer. Trouver la case bleu pour gagner.",fill="white")
root.after(2000,NewGame)

root.mainloop()
