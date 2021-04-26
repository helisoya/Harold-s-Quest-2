# Tir Sur Marchand par Julien

from tkinter import *
from Engine import *

diff = 1
toGo = 100*diff
score = 0
remain = 5

mar_pos = 35
mar_target = 365

def MiniGame_TSM():
    global diff,toGo,score,remain,mar_pos,mar_target
    
    DisableWindow()
    
    diff = GetVar("difficulte")
    toGo = 100*diff
    score = 0
    remain = 5

    mar_pos = 35
    mar_target = 365

    root = Tk()
    root.title("Mini Jeu")

    can = Canvas(root,width=400,height=300,bg="darkgray")
    can.pack()

    img = PhotoImage(master=root,file="Data/Autres/TSM/marchand.png")


    can.create_rectangle(15,100,85,150,fill="blue",tags="marchand")
    can.create_image(35,150,image=img,tags="marchand")
    can.create_rectangle(0,200,400,300,fill="brown")
    can.create_text(100,250,text="Tir sur Marchand !")
    can.create_text(200,240,text="Je peux enfin me défouler \n sur cette enflure ! \n Rickey, PDG",anchor=W)
    can.create_rectangle(190,140,210,160,fill="red",tags="viseur")
    can.create_text(10,20,text="Restant : 5",anchor=W,tags="remain")
    can.create_text(70,20,text="Score : 0",anchor=W,tags="score")
    can.create_text(330,20,text="Objectif : "+str(toGo),anchor=W)
    
    def QuitMinigame():
        root.destroy()
        EnableWindow()
        Chargement("save.sav")
    
    root.protocol("WM_DELETE_WINDOW", QuitMinigame)

    def MoveMarchand():
        global mar_pos, mar_target
        
        if not mar_target-2 < mar_pos < mar_target+2:
            if mar_pos > mar_target:
                mar_pos-=2
                can.move("marchand",-2,0)
            else:
                mar_pos+=2
                can.move("marchand",2,0)
        else:
            if mar_target == 365:
                mar_target = 35
            else:
                mar_target = 365

        root.after(8,MoveMarchand)
        
    def Delete_Reaction():
        can.delete("reaction")

    def Tir(event):
        global score,remain,mar_pos

        if 1 in can.find_overlapping(190,140,210,160):
            score = 0
            remain = 5
            can.itemconfigure("remain",text="Restant : "+str(remain))
            can.itemconfigure("score",text="Score : "+str(score))
            can.create_text(200,20,text="Perdu !",tags="reaction")
            root.after(1000,Delete_Reaction)

        else:
            remain-=1
            if 160 < mar_pos < 270:
                score+=100
            elif 140 < mar_pos < 290:
                score+=75
            elif 120 < mar_pos < 310:
                score+=50
            elif 100 < mar_pos < 330:
                score+=25

            can.itemconfigure("remain",text="Restant : "+str(remain))
            can.itemconfigure("score",text="Score : "+str(score))

            if remain == 0 or score >= toGo:
                if score >= toGo:
                    TableauSuivant("RickeyLandMarchand_Attr_3")
                    root.destroy()
                    EnableWindow() 
                else:
                    score = 0
                    remain = 5
                    can.itemconfigure("remain",text="Restant : "+str(remain))
                    can.itemconfigure("score",text="Score : "+str(score))




    root.bind("<Button-1>",Tir)

    MoveMarchand()

    root.mainloop()
