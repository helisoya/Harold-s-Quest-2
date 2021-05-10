#Survivre à la Torture par Julien

from tkinter import *
from random import *
from Engine import *

diff = 3

hp = 100
pressed = False
temps = 20

def MiniGame_ST():
    global diff,hp,pressed,temps
    
    DisableWindow()
    
    diff = GetVar("difficulte")

    hp = 100
    pressed = False
    temps = 20

    root = Tk()
    root.title("Mini Jeu")

    bg = PhotoImage(master=root,file="Data/Autres/ST/bg.png")
    can = Canvas(root,width=400,height=300)

    can.create_image(200,150,image=bg)
    can.create_rectangle(5,5,105,25,fill="gray")
    can.create_text(200,20,text="Temps : "+str(temps),fill="white",tags="temps")
    can.pack()
    
    def QuitMinigame():
        root.destroy()
        EnableWindow()
        Chargement("save.sav")
    
    root.protocol("WM_DELETE_WINDOW", QuitMinigame)

    def Input(event):
        global hp,pressed
        if event.type == "3":
            pressed = False

        if not pressed:
            pressed = True
            hp+=2
            if hp > 100:
                hp = 100

    def Time():
        global temps
        temps-=1
        can.itemconfigure("temps",text="Temps : "+str(temps))
        if temps == 0:
            TableauSuivant("RickeyLandPalais_RickeyPartB_15")
            root.destroy()
            EnableWindow()
            return
        else:
            root.after(1000,Time)


    def MainLoop():
        global hp,temps
        if hp > 0:
            hp-=1
            can.delete("hp")
            can.create_rectangle(5,5,hp+5,25,fill="green",tags="hp")
        else:
            can.itemconfigure("temps",text=" Perdu ! Temps : "+str(temps))
            hp = 100
            temps = 20
        root.after(200-diff*50,MainLoop)

    def Start():
        can.delete("txt")
        root.bind("<KeyPress-space>",Input)
        root.bind("<KeyRelease-space>",Input)
        Time()
        MainLoop()
    
    can.create_text(200,150,text="Appuyez rapidement sur Espace !",fill="white",tags="txt")
    root.after(2000,Start)

    root.mainloop()

