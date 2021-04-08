# Evite vautour par Corentin et Julien

from tkinter import*
from random import *
from Engine import *

list_vautour = []
diff=1
temps=2000*diff
counter = 20
pos2 = -450/2
pos1 = 450/2
loop = 0

def MiniGame_EV():
    global list_vautour,diff,temps,counter,pos2,pos1,loop
 
    list_vautour = []
    diff=GetVar("difficulte")
    temps=2000*diff
    counter = 20
    pos2 = -450/2
    pos1 = 450/2 
    
    DisableWindow()
 
    fenetre=Tk()
    fenetre.title("Mini Jeu")

    canvas = Canvas(fenetre, width=480, height=450, background='white')

    plaine = PhotoImage(master=fenetre,file="Data\\Autres\\EV\\plaine.png")
    player = PhotoImage(master=fenetre,file="Data\\Autres\\EV\\player.png")

    canvas.create_image(480/2,450/2,image=plaine,tags="plaine1")
    canvas.create_image(480/2,-450/2,image=plaine,tags="plaine2")
    canvas.create_line(325, 0, 325, 450)
    canvas.create_line(150, 0, 150, 450)
    canvas.create_text(50,50,text="HP * 5",tags="hp",fill="white",font=("Helvetica",24))
    canvas.create_text(200,50,text="temps=",tags="temps",fill="white",font=("Helvetica",24))



    img_vautours = [
            PhotoImage(master=fenetre,file="Data\\Autres\\EV\\vautour_1.png"),
            PhotoImage(master=fenetre,file="Data\\Autres\\EV\\vautour_2.png"),
            PhotoImage(master=fenetre,file="Data\\Autres\\EV\\vautour_3.png"),
        ]

    def QuitMinigame():
        fenetre.after_cancel(loop)
        fenetre.destroy()
        EnableWindow()
        Chargement("save.sav")
       
    fenetre.protocol("WM_DELETE_WINDOW", QuitMinigame)

    def UpdateScrollDownGrass():
        global pos1,pos2,diff
        pos1-=2*diff
        pos2-=2*diff
       
        if pos1 < -220:
            pos1 = 450+450/2-5
        if pos2 < -220:
            pos2 = 450+450/2-5
        
        canvas.coords("plaine1",480/2,pos1)
        canvas.coords("plaine2",480/2,pos2)


    class Hero:
        def __init__(self,diff):
            self.pos = 2
            self.hp = 6-diff


    class Vautour:
        def __init__(self,X,Y,SPD,IMG):
            self.x=X
            self.y=Y
            self.spd= SPD
            self.canHit = True
            self.img = IMG

        def Update(self):
            self.y+=1*self.spd

            if not self.canHit:
                return

            if ( (self.x == 70 and hero.pos==1) or (self.x == 250 and hero.pos==2) or (self.x == 400 and hero.pos==3)) and 180<=self.y<=220:
                hero.hp-=1
                self.canHit = False

    canvas.pack()

    hero = Hero(diff)

    def GetInput(event):
        if event.keycode==37:# Gauche
            hero.pos-=1
            if hero.pos==0:
                hero.pos=1
        if event.keycode==39:#Droite
            hero.pos+=1
            if hero.pos==4:
                hero.pos=3


    fenetre.bind("<KeyPress>",GetInput)

    def MainLoop():
        global temps,counter,list_vautour,loop
        canvas.delete("perso")
        canvas.delete("vautour")
        
        UpdateScrollDownGrass()

        if counter > 0:
            counter -=1
        elif len(list_vautour) < 2+diff and randint(1,50) == 1:
            list_vautour.append(Vautour(choice([70,250,400]),0,2+diff,randint(0,len(img_vautours)-1)))
            counter = 20

        for pnj in list_vautour:
            pnj.Update()
            canvas.create_image(pnj.x,pnj.y,image=img_vautours[pnj.img],tags="vautour")
            if pnj.y > 450:
                list_vautour.remove(pnj)

        canvas.itemconfigure("hp",text="HP * "+str(hero.hp))
        canvas.itemconfigure("temps",text="temps="+str(round(temps/100)))
        temps-=1

        X = 70
        if hero.pos==2:
            X = 250
        if hero.pos==3:
            X = 400
        canvas.create_image(X,200,image=player,tags="perso")

        if hero.hp==0 :
            temps=2000*diff
            hero.hp = 6-diff
            list_vautour = []
        if temps==0:
           TableauSuivant("Event_Archer_11")
           fenetre.destroy()
           EnableWindow()
           return
        loop = fenetre.after(15,MainLoop)





    MainLoop()

    fenetre.mainloop()
