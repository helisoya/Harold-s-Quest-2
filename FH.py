# Flappy Harold par Julien

from tkinter import *
from random import *

Y = 150
impulse = 0
key = False

list_mur = []
cooldown = 0
score = 0

reset = False


def MiniGame_FH():
    global Y,impulse,key,list_mur,cooldown,score,reset

    Y = 150
    impulse = 0
    key = False

    list_mur = []
    cooldown = 0
    score = 0

    reset = False


    root = Tk()
    root.title("Flappy Harold")

    can = Canvas(root,width=400,height=300,bg="blue")
    can.pack()

    oiseau = PhotoImage(master=root,file="Data/Autres/FH/oiseau.png")



    def Input_Down(event):
        global impulse,key
        if key == False:
            impulse = 2
            key = True

    def Input_Up(event):
        global key
        key = False

    def Update_Player():
        global Y,impulse,reset
        if impulse>0.0001:
            impulse-=0.01
        else:
            impulse = 0

        Y += 4-3*impulse

        if Y >= 300:
            reset = True
        if Y<=0:
            Y = 0

    class Mur:

        def __init__(self,X,Y,WIDTH,HEIGHT,COLOR):
            self.x = X
            self.y = Y
            self.width = WIDTH
            self.height = HEIGHT
            self.score = True
            self.twin = 0
            self.color = COLOR

        def Update(self):
            global Y,score,reset
            self.x-=5

            if self.x+self.width <= 0:
                return True

            if (self.x <= 85 <= self.x+self.width or self.x <= 115 <= self.x+self.width) and (self.y <= Y-30 <= self.y+self.height or  self.y <= Y+30 <= self.y+self.height):
                reset = True
                return True

            if self.x<= 100 and self.score and self.twin.score:
                self.score = False
                score+=1

            return False


    def MainLoop():
        global Y,list_mur,cooldown,score,reset
        can.delete("all")
        Update_Player()
        can.create_image(100,Y,image=oiseau)

        if cooldown > 0:
            cooldown-=1
        else:
            cooldown=randint(20,100)

            color = [
                "black",
                "red",
                "green",
                "yellow"
            ]
            color = choice(color)

            list_mur.append(Mur(450,0,50,randint(10,100),color))
            list_mur.append(Mur(450,randint(200,290),50,200,color))
            list_mur[-2].twin = list_mur[-1]
            list_mur[-1].twin = list_mur[-2]

        to_remove = []

        for mur in list_mur:
            if mur.Update():
                to_remove.append(mur)
            can.create_rectangle(mur.x,mur.y,mur.x+mur.width,mur.y+mur.height,fill=mur.color)

        for mur in to_remove:
            list_mur.remove(mur)

        can.create_text(20,20,fill="white",anchor=W,text="Score : "+str(score))


        if reset:
            reset=False
            Y = 150
            score=0
            del list_mur [:]

        root.after(15,MainLoop)


    root.bind("<KeyPress>",Input_Down)
    root.bind("<KeyRelease>",Input_Up)

    MainLoop()

    root.mainloop()

