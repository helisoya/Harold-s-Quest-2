#Course de Chevaux par Julien

from tkinter import *
from random import *
from Engine import *

diff = 3
temps = 2000*diff
frame = 0
cld_frame = 10

pos1 = 200
pos2 = 600

def MiniGame_CDC():
    global diff,temps,frame,cld_frame,pos1,pos2
    
    diff = GetVar("difficulte")
    temps = 2000*diff
    frame = 0
    cld_frame = 10

    pos1 = 200
    pos2 = 600
    
    DisableWindow()

    root = Tk()
    root.title("Mini Jeu")

    can = Canvas(root,width=400,height=300)
    can.pack()


    frames = []
    for i in range(4):
        frames.append(PhotoImage(master=root,file="Data/Autres/CDC/horse_"+str(i+1)+".png"))

    img_mur = PhotoImage(master=root,file="Data/Autres/CDC/mur.png")
    img_bul = PhotoImage(master=root,file="Data/Autres/CDC/balle.png")
    img_bg = PhotoImage(master=root,file="Data/Autres/CDC/bg.png")

    can.create_image(200,150,image=img_bg,tags="plaine1")
    can.create_image(600,150,image=img_bg,tags="plaine2")
    
    def QuitMinigame():
        root.destroy()
        EnableWindow()
        Chargement("save.sav")
    
    root.protocol("WM_DELETE_WINDOW", QuitMinigame)

    class Player:

        def __init__(self):
            self.x = 215
            self.y = 200
            self.pv = 6-diff
            self.left = 0
            self.right = 0
            self.up = 0

        def KeyPress(self,event):
            if event.keycode == 37:
                self.left = 1
            elif event.keycode == 38 and self.y == 215:
                self.up = 1
            elif event.keycode == 39:
                self.right = 1

        def KeyRelease(self,event):
            if event.keycode == 37:
                self.left = 0
            elif event.keycode == 38:
                self.up = 0
            elif event.keycode == 39:
                self.right = 0

        def Update(self):
            self.x += self.right*5-self.left*5
            self.y += 2- 4 * self.up
            if self.up > 0.01:
                self.up-=0.007
            else:
                self.up = 0

            if self.x < 0:
                self.x = 0
            if self.x > 400:
                self.x = 400
            if self.y < 0:
                self.y = 0
            if self.y > 215:
                self.y = 215
                self.up = 0


    class Tir:

        def __init__(self):
            self.x = -5
            self.y = -15
            self.cooldown = randint(80,100)-10*diff

        def Update(self,player):
            if self.cooldown > 0:
                self.cooldown-=1
            elif self.y == -15:
                self.y = randint(130,160)

            if self.y != -15:
                self.x+= 2*diff

            if self.x > 400:
                self.x = -5
                self.y = -15
                self.cooldown = randint(80,100)-10*diff

            touch = ConvertIdToTag(can.find_overlapping(self.x-5,self.y-5,self.x+5,self.y+5))
            if len(touch) > 0 and "p" in touch:
                player.pv -= 1
                self.x = 500

    class Mur:

        def __init__(self):
            self.x = 450
            self.y = 215
            self.cooldown = randint(80,100)-10*diff

        def Update(self,player):
            if self.cooldown > 0:
                self.cooldown-=1
                return

            self.x-= 2*diff

            if self.x < 0:
                self.x = 450
                self.cooldown = randint(80,100)-10*diff

            touch = ConvertIdToTag(can.find_overlapping(self.x-86/2,self.y-15,self.x+86/2,self.y+15))
            if len(touch) > 0 and "p" in touch:
                player.pv -= 1
                self.x = -100
            

    perso = Player()

    tir = Tir()

    mur = Mur()

    def ConvertIdToTag(l):
        l = list(l)
        for i in range(len(l)):
            l[i] = can.gettags(l[i])[0]
        return l

    def UpdateScrollDownGrass():
        global pos1,pos2
        pos1-=2
        pos2-=2
       
        if pos1 <= -200:
            pos1 = 600
        if pos2 <= -200:
            pos2 = 600
        
        can.coords("plaine1",pos1,150)
        can.coords("plaine2",pos2,150)

    def Delete_Reaction():
        can.delete("reaction")

    def MainLoop():
        global temps,diff,frame,cld_frame
        temps-=1
        can.delete("p")
        can.delete("e")
        
        UpdateScrollDownGrass()
        
        if cld_frame > 0:
            cld_frame-=1
        else:
            cld_frame = 10
            frame+=1
            if frame > 3:
                frame = 0
        
        perso.Update()
        can.create_image(perso.x,perso.y,image=frames[frame],tags="p")

        tir.Update(perso)
        can.create_image(tir.x,tir.y,image=img_bul,tags="e")

        mur.Update(perso)
        can.create_image(mur.x,mur.y,image=img_mur,tags="e")

        can.create_text(10,10,anchor=W,text="PV : "+str(perso.pv),tags="e")
        can.create_text(10,40,anchor=W,text="Temps : "+str(round(temps/100)),tags="e")

        if perso.pv <= 0:
            perso.pv = 6-diff
            tir.x = -5
            tir.y = -15
            tir.cooldown = 80
            mur.x = 450
            mur.cooldown = 80

            temps = 2000*diff
            
            can.create_text(200,20,text="Perdu !",tags="reaction")
            root.after(1000,Delete_Reaction)

        if temps == 0:
            TableauSuivant("RickeyLandHorse_Attr_3")
            root.destroy()
            EnableWindow()
            return
        else:
            root.after(15,MainLoop)

    root.bind("<KeyPress>",perso.KeyPress)
    root.bind("<KeyRelease>",perso.KeyRelease)
        
    MainLoop()
    root.mainloop()

