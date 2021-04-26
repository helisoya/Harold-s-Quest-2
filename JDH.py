# Juste Dance Harold par Julien

from tkinter import *
from random import *
from time import *

from Engine import *



moveDone = True
wrongMove = False
currMove = 0
score = 0
combo = 0
scoreHarold = 0
diff = 3
total = 300+100*diff
anim_Frame = 0
List_Anim = []

def MiniGame_JDH():
    global moveDone,wrongMove,currMove,score,combo,scoreHarold,diff,total,anim_Frame,List_Anim

    moveDone = True
    wrongMove = False
    currMove = 0
    score = 0
    combo = 0
    scoreHarold = 0
    diff = GetVar("difficulte")
    total = 300+100*diff
    anim_Frame = 0
    List_Anim = []

    DisableWindow()

    root = Tk()
    root.title("Mini Jeu")

    can = Canvas(root,width=400,height=300)
    can.pack()
    can.create_rectangle(0,0,400,190,fill="black")
    can.create_rectangle(0,190,400,300,fill="#2800B8")
    can.create_image(200,150,image="",tags="Harold")
    can.create_rectangle(170,200,230,220,tags="bg_touche",fill="lightgray")
    can.create_text(200,210,text="Attention !",tags="touche")
    can.create_text(350,10,text="Premier à : "+str(total),fill="white")
    can.create_text(40,10,text="Vous : 0",tags="score",fill="white")
    can.create_text(40,30,text="Harold : 0",tags="scoreHarold",fill="white")


    def QuitMinigame():
        root.destroy()
        EnableWindow()
        Chargement("save.sav")
    
    root.protocol("WM_DELETE_WINDOW", QuitMinigame)



    for i in range(288):
        nb = str(i)
        while len(nb) < 3:
            nb = "0"+nb
        List_Anim.append(PhotoImage(master=root,file="Data\\Autres\\JDH\\frame_"+nb+"_delay-0.06s.png"))


    def AddReaction(txt):
        can.create_text(200,250,text=txt,tags="reaction",fill="white")
        root.after(300,DeleteReaction)

    def DeleteReaction():
        can.delete("reaction")

    def GetName(code):
        if code == 37:
            return "Gauche"
        if code == 38:
            return "Haut"
        if code == 39:
            return "Droite"
        if code == 40:
            return "Bas"

    def Harold_NextFrame():
        global anim_Frame,score,scoreHarold,total,List_Anim

        anim_Frame+=1
        if anim_Frame >= len(List_Anim):
            anim_Frame = 0
        can.itemconfigure("Harold",image=List_Anim[anim_Frame])

        if score < total and scoreHarold < total:
            root.after(50,Harold_NextFrame)



    def NewTurn():
        global moveDone,currMove,score,wrongMove,combo,scoreHarold,total

        scoreHarold += randint(5,10+5*diff)
        end = False
        if not moveDone:
            score-=10
            if score <= 0:
                score = 0
            combo = 0
            AddReaction("Faux")
        else:
            if combo < 5:
                combo+=1
                AddReaction(str(combo)+"x Bien")
            else:
                AddReaction("Super !")
            score+=5*combo

        wrongMove = False
        moveDone = False
        currMove = randint(37,40)
        can.itemconfigure("bg_touche",fill="lightgray")
        can.itemconfigure("touche",text=GetName(currMove))
        can.itemconfigure("score",text="Vous : "+str(score))
        can.itemconfigure("scoreHarold",text="Harold : "+str(scoreHarold))

        if score < total and scoreHarold < total:
            root.after(1100-100*diff,NewTurn)
        else:
            DeleteReaction()
            root.unbind("<Up>")
            root.unbind("<Down>")
            root.unbind("<Left>")
            root.unbind("<Right>")
            if score >= total:
               TableauSuivant("TourNoir_PartB_14")
               root.destroy()
               EnableWindow()
               return
            else:
                can.itemconfigure("touche",text="Perdu")
                root.after(2000,Reset)

    def Input(event):
        global moveDone,wrongMove
        if currMove == event.keycode and not wrongMove:
            can.itemconfigure("bg_touche",fill="green")
            moveDone = True
        else:
            can.itemconfigure("bg_touche",fill="red")
            wrongMove = True
            
    def Reset():
        global moveDone,wrongMove,currMove,score,combo,scoreHarold

        moveDone = True
        wrongMove = False
        currMove = 0
        score = 0
        combo = 0
        scoreHarold = 0
        
        root.bind("<Up>",Input)
        root.bind("<Down>",Input)
        root.bind("<Left>",Input)
        root.bind("<Right>",Input)
        Harold_NextFrame()
        NewTurn()



    def NewGame():
        root.bind("<Up>",Input)
        root.bind("<Down>",Input)
        root.bind("<Left>",Input)
        root.bind("<Right>",Input)
        Harold_NextFrame()
        NewTurn()

    root.after(2000,NewGame)

    root.mainloop()
