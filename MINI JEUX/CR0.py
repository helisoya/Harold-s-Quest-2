#Combat contre Rick0 par Julien

from tkinter import *
from random import *

diff = 3


turn = True
hp = 100
hp_rick0 = 100
res = 0
res_rick0 = 0

dic = {}

root = Tk()

dic["p_idle"] = PhotoImage(master=root,file="Data//Autres//CR0//player_idle.png")
dic["p_block"] = PhotoImage(master=root,file="Data//Autres//CR0//player_block.png")
dic["r_idle"] = PhotoImage(master=root,file="Data//Autres//CR0//rick0_idle.png")
dic["r_block"] = PhotoImage(master=root,file="Data//Autres//CR0//rick0_block.png")

can = Canvas(root,width=400,height=300)
can.pack()

can.create_oval(20,190,150,240,fill="green") # Rond vert
can.create_oval(250,120,380,170,fill="green")

can.create_image(75,180,image=dic["p_idle"],tags="player") # Persos
can.create_image(310,100,image=dic["r_idle"],tags="rick0")

can.create_rectangle(5,5,105,25,fill="gray") #Barre de vie
can.create_rectangle(295,5,395,25,fill="gray")

can.create_rectangle(0,210,400,300,fill="gray") # Interface
can.create_rectangle(190,235,290,275,fill="lightgray",tags="att")
can.create_text(240,255,text="Attaquer",tags="att")
can.create_rectangle(295,235,395,275,fill="lightgray",tags="par")
can.create_text(345,255,text="Parer",tags="par")
can.create_text(100,255,text="",tags="txt")


def UpdateHp():
    global hp,hp_rick0,res,res_rick0


    if hp_rick0 <= 0:
        root.destroy()
    if hp <= 0:
        hp = 100
        hp_rick0 = 100
        res = 0
        res_rick0 = 0
        can.itemconfigure("txt",text="Rick0 est très fort, \n je dois me concentrer")
    
    can.delete("hp")
    can.create_rectangle(5,5,hp+5,25,fill="green",tags="hp")
    can.create_rectangle(395,5,395-hp_rick0,25,fill="red",tags="hp")




def Attaque():
    global turn,hp_rick0,res_rick0
    if not turn:
        return
    turn = False 
    hp_rick0 -= 5-res_rick0
    UpdateHp()
    can.itemconfigure("rick0",image=dic["r_idle"])
    can.itemconfigure("txt",text="Vous attaquez Rick0 - "+str(5-res_rick0))
    res_rick0 = 0
    root.after(1000,TourBot)

def Parer():
    global turn,res_rick0,res
    if not turn:
        return
    turn = False
    res = 2
    res_rick0 = 0
    can.itemconfigure("rick0",image=dic["r_idle"])
    can.itemconfigure("player",image=dic["p_block"])
    can.itemconfigure("txt",text="Vous vous préparez")
    root.after(1000,TourBot)

def TourBot():
    global res,hp,turn,res_rick0

    if randint(1,10) <= 6:
        hp-= 3+diff - res
        can.itemconfigure("txt",text="Rick0 vous attaque - "+str(3+diff - res))
    else:
        can.itemconfigure("rick0",image=dic["r_block"])
        res_rick0 = 2
        can.itemconfigure("txt",text="Rick0 se prépare")
    can.itemconfigure("player",image=dic["p_idle"])
    UpdateHp()
    res = 0
    turn = True

    
    
UpdateHp()

can.tag_bind("att","<Button-1>",lambda arg=0:Attaque())
can.tag_bind("par","<Button-1>",lambda arg=0:Parer())

root.mainloop()

