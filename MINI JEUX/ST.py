#Survivre à la Torture par Julien

from tkinter import *
from random import *

diff = 2

hp = 100
pressed = False

root = Tk()

can = Canvas(root,width=400,height=300)

can.create_rectangle(5,5,105,25,fill="gray")
can.pack()

def Input(event):
    global hp,pressed
    if event.type == "3":
        pressed = False

    if not pressed:
        pressed = True
        hp+=2
        if hp > 100:
            hp = 100


def MainLoop():
    global hp
    if hp > 0:
        hp-=1
        can.delete("hp")
        can.create_rectangle(5,5,hp+5,25,fill="green",tags="hp")
        root.after(200-diff*50,MainLoop)
    else:
        can.delete("all")
        can.create_text(200,150,text="PERDU")


root.bind("<KeyPress-space>",Input)
root.bind("<KeyRelease-space>",Input)

MainLoop()

root.mainloop()

