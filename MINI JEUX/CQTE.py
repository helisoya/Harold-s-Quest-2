# Combat QTE par Julien

from tkinter import *
from random import *

diff = 3
hp = 7-diff
hp_en = 10*diff
move = 0
current = ""

root = Tk()
root.title("Mini Jeu")

bg = PhotoImage(master=root,file="Data/Autres/CQTE/bg.png")
can = Canvas(root,width=400,height=300)
can.pack()
can.create_image(200,150,image=bg)
can.create_rectangle(170,200,230,220,tags="bg_touche",fill="lightgray")
can.create_text(200,210,text="Attention !",tags="touche")
can.create_text(10,20,text="HP : "+str(hp-1),anchor=W,fill="white",tags="hp")
can.create_text(10,50,text="Ennemi : "+str(hp_en),anchor=W,fill="white",tags="hp_en")

def EndQTE():
    global hp,hp_en,move,current
    if move == 2:
        hp_en-=1
    else:
        hp-=1
    
    move = 0
    current = choice(["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"])

    can.itemconfigure("touche",text=current)
    can.itemconfigure("bg_touche",fill="lightgray")

    can.itemconfigure("hp",text="HP : "+str(hp))
    can.itemconfigure("hp_en",text="Ennemi : "+str(hp_en))

    if hp == 0:
        hp = 7-diff
        hp_en=10*diff
        can.itemconfigure("touche",text="Perdu !")
    elif hp_en == 0:
        root.destroy()
        return

    root.after(2000-200*diff,EndQTE)

def KeyPress(event):
    global move,current
    if move == 0:
        if event.keysym == current:
            move = 2
            can.itemconfigure("bg_touche",fill="green")
        else:
            move = 1
            can.itemconfigure("bg_touche",fill="red")

            

root.bind("<Key>",KeyPress)
root.after(2000,EndQTE)

root.mainloop()
