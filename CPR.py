﻿# Course Poursuite avec Rickey par Julien

from tkinter import *
from random import *
from Engine import *

diff = 3
nxt = 7+diff
hp = 6-diff
bg = []
frame = 0

def MiniGame_CPR():
    global diff,nxt,hp,bg,frame
    
    diff = GetVar("difficulte")
    nxt = 7+diff
    hp = 6-diff
    bg = []
    frame = 0
    
    DisableWindow()

    root = Tk()
    root.title("Mini Jeu")

    for i in range(10):
        bg.append(PhotoImage(master=root,file="Data/Autres/CPR/"+str(i)+".png"))

    can = Canvas(root,width=400,height=300)
    can.pack()
    can.create_image(200,150,image="",tags="bg")
    can.create_rectangle(0,0,400/3,300,fill="red",stipple="gray75",tags="t1")
    can.create_rectangle(400/3,0,2*400/3,300,stipple="gray75",fill="red",tags="t2")
    can.create_rectangle(2*400/3,0,400,300,stipple="gray75",fill="red",tags="t3")

    can.itemconfigure("t1",state="hidden")
    can.itemconfigure("t2",state="hidden")
    can.itemconfigure("t3",state="hidden")

    can.create_text(10,20,text="HP : "+str(hp),anchor=W,fill="white",tags="hp")


    def QuitMinigame():
        root.destroy()
        EnableWindow()
        Chargement("save.sav")
    
    root.protocol("WM_DELETE_WINDOW", QuitMinigame)

    def UpdateBg():
        global bg,frame
        can.itemconfigure("bg",image=bg[frame])
        frame+=1
        if frame==len(bg):
            frame=0
        root.after(50,UpdateBg)


    def EnableChoice():
        can.itemconfigure("t1",state="normal")
        can.itemconfigure("t2",state="normal")
        can.itemconfigure("t3",state="normal")

    def DeleteReaction():
        can.delete("reaction")


    def Choice(event):
        global nxt,hp

        current = can.gettags("current")[0]
        if current[1] == str(randint(1,3)):
            can.create_text(200,150,text="Mauvais Chemin !",fill="white",tags="reaction")
            hp-=1
        else:
            can.create_text(200,150,text="Bon Chemin !",fill="white",tags="reaction")
        root.after(1000,DeleteReaction)

        if hp > 0:
            if nxt > 0:
                nxt-=1
                can.itemconfigure("hp",text="HP : "+str(hp))
                can.itemconfigure("t1",state="hidden")
                can.itemconfigure("t2",state="hidden")
                can.itemconfigure("t3",state="hidden")
                root.after(2000,EnableChoice)
        else:
            hp = 6-diff
            nxt=8+diff
            can.itemconfigure("hp",text="HP : "+str(hp))
            can.itemconfigure("t1",state="hidden")
            can.itemconfigure("t2",state="hidden")
            can.itemconfigure("t3",state="hidden")
            root.after(2000,EnableChoice)

    def Check():
        global nxt
        if nxt == 0:
            TableauSuivant("RickeyLandPalais_RickeyPartA_21")
            root.destroy()
            EnableWindow()
            return
        root.after(10,Check)
        

    can.tag_bind("t1","<Button-1>",Choice)
    can.tag_bind("t2","<Button-1>",Choice)
    can.tag_bind("t3","<Button-1>",Choice)
    UpdateBg()
    Check()
    root.after(2000,EnableChoice)

    root.mainloop()