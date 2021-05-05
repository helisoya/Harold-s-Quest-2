# Combat contre Cerf par Julien

from tkinter import *
from random import *
from Engine import *

diff = 3
PV = 6-diff
list_att = []
cooldown = 0
temps = 2000

def MiniGame_CCC():
    global diff,PV,list_att,cooldown,temps
    
    DisableWindow()

    root = Tk()
    root.title("Mini Jeu")

    can = Canvas(root,width=300,height=300,bg="black")
    can.pack()

    dic = []
    
    diff = GetVar("difficulte")
    PV = 6-diff
    list_att = []
    cooldown = 0
    temps = 2000
    
    def QuitMinigame():
        root.destroy()
        EnableWindow()
        Chargement("save.sav")
    
    root.protocol("WM_DELETE_WINDOW", QuitMinigame)

    class Attaque:

        def __init__(self,X,Y,DIRX,DIRY,TYPE):
            self.x = X
            self.y = Y
            self.dirX = DIRX
            self.dirY = DIRY
            self.type = TYPE

        def Update(self,player):
            global PV
            self.x+=self.dirX*diff
            self.y+=self.dirY*diff

            if self.x < 0 or self.y < 0 or self.x > 300 or self.y > 300:
                return False

            if (self.x-20 < perso.x-10 < self.x+20 or self.x-20 < perso.x+10 < self.x+20) and (self.y-10 < perso.y-10 < self.y+10 or self.y-10 < perso.y+10 < self.y+10) and self.type == "h":
                PV-=1
                return False

            if (self.x-10 < perso.x-10 < self.x+10 or self.x-10 < perso.x+10 < self.x+10) and (self.y-20 < perso.y-10 < self.y+20 or self.y-20 < perso.y+10 < self.y+20) and self.type == "v":
                PV-=1
                return False
            
            return True

    class Perso:

        def __init__(self):
            self.x = 150
            self.y = 150
            self.left = 0
            self.right = 0
            self.up = 0
            self.down = 0

        def KeyPress(self,event):
            if event.keycode == 37:
                self.left = 1
            elif event.keycode == 38:
                self.up = 1
            elif event.keycode == 39:
                self.right = 1
            elif event.keycode == 40:
                self.down = 1

        def KeyRelease(self,event):
            if event.keycode == 37:
                self.left = 0
            elif event.keycode == 38:
                self.up = 0
            elif event.keycode == 39:
                self.right = 0
            elif event.keycode == 40:
                self.down = 0

        def Update(self):
            self.x += self.right*3-self.left*3
            self.y += self.down*3-self.up*3

            if self.x < 5:
                self.x = 5
            if self.x > 295:
                self.x = 295
            if self.y < 5:
                self.y = 5
            if self.y > 295:
                self.y = 295

    perso = Perso()
    root.bind("<KeyPress>",perso.KeyPress)
    root.bind("<KeyRelease>",perso.KeyRelease)


    def CheckIfWithin(pos,toCheck,r):
        return pos-r <= toCheck <= pos+r

    def CheckAllWithin(l,toCheck):
        for value in l:
            if CheckIfWithin(value,toCheck,10):
                return True
        return False
     

    def Mainloop():
        global list_att,PV,cooldown,temps

        can.delete("all")
        temps-=1

        if cooldown > 0:
            cooldown-=1
        else:
            cooldown = 100-10*diff
            de = randint(1,4)
            l = [-50]
            for i in range(2+diff):
                p = randint(10,290)
                while CheckAllWithin(l,p):
                    p = randint(10,290)
                l.append(p)
                
                if de == 1: # Gauche
                    list_att.append(Attaque(0,randint(10,290),1,0,"h"))
                elif de == 2: # Droite
                    list_att.append(Attaque(300,randint(10,290),-1,0,"h"))
                elif de == 3: # Haut
                    list_att.append(Attaque(randint(10,290),0,0,1,"v"))
                else: # Bas
                    list_att.append(Attaque(randint(10,290),300,0,-1,"v"))


        perso.Update()
        can.create_rectangle(perso.x-10,perso.y-10,perso.x+10,perso.y+10,fill="green")

        toRemove = []
        

        for att in list_att:
            if att.Update(perso):
                if att.type == "h":
                    can.create_rectangle(att.x-20,att.y-10,att.x+20,att.y+10,fill="red")
                else:
                    can.create_rectangle(att.x-10,att.y-20,att.x+10,att.y+20,fill="red")
            else:
                toRemove.append(att)

        for att in toRemove:
            list_att.remove(att)

        can.create_text(10,20,anchor=W,text="PV : "+str(PV),fill="white")

        if temps > 0 and PV > 0:
            can.create_text(10,40,anchor=W,text="Temps : "+str(round(temps/100)),fill="white")
            root.after(8,Mainloop)
        else:
            if temps == 0:
                TableauSuivant("TourNoir_PartC_Cerf_15")
                root.destroy()
                EnableWindow()
                return
            else:
                PV = 6-diff
                temps = 2000
                list_att = []
                root.after(15,Mainloop)

    can.create_text(200,150,text="Flèches pour vous déplacer \n Évitez les attaques.",fill="white",tags="desc")
    def NewGame():
        can.delete("desc")
        Mainloop()
        
    root.after(2000,NewGame)

    root.mainloop()
