# Course Poursuite avec Chasseur par Mathis

from tkinter import *
from random import randint
import time

diff = 3


def gauche(x):
    global xperso

    if not xperso-240 <0:
        dessin.delete("joueur")
        xperso-=240
        dessin.create_image(xperso, yperso, image=photo,tags="joueur")
        root.after(500,MoveChasseurG)

def MoveChasseurG():
    global xchasseur
    xchasseur-=240
    dessin.delete("chasseur")
    dessin.create_image(xchasseur, ychasseur, image=photo3,tags="chasseur")

def droite(x):
    global xperso

    if not xperso+240 >720:
        dessin.delete("joueur")
        xperso+=240
        dessin.create_image(xperso, yperso, image=photo,tags="joueur")
        root.after(500,MoveChasseurD)

def MoveChasseurD():

    global xchasseur
    xchasseur+=240
    dessin.delete("chasseur")
    dessin.create_image(xchasseur, ychasseur, image=photo3,tags="chasseur")

def MoveBalle(x,y,z):
    global photo2
    global p
    global temps

    dessin.delete(z)
    if p==1:
        y=0
        p=0

    y-=4
    w=[]
    z=[]
    final=[]
    w=GetTagFromId(dessin.find_overlapping(x-50,y-25,x+50,y+50))

    for elem in w:
        if elem == "joueur":
            temps=20*diff
            legende.configure(text="Perdu !")
            return

    if y>0:
        z=dessin.create_image(x, y, image=photo2,tags="balle")
        root.after(10,lambda:MoveBalle(x,y,z))


def TirreBalle():
    global xchasseur
    x=xchasseur
    global ychasseur
    y=ychasseur
    global photo2
    z=dessin.create_image(x, y, image=photo2,tags="balle")
    MoveBalle(x,y,z)
    root.after(3400,TirreBalle)

def appbarrière():
    xb=randint(1,3)
    xb=xb*240-120
    yb=0
    global photo4
    zb=dessin.create_image(xb, yb, image=photo4,tags="barrière")
    MoveBarrière(xb,yb,zb)
    root.after(4000,appbarrière)

def MoveBarrière(x,y,z):
    global photo4
    global p
    global temps
    dessin.delete(z)
    y+=4
    w=[]
    z=[]
    final=[]
    w=GetTagFromId(dessin.find_overlapping(x-50,y-25,x+50,y+50))
    for elem in w:
        if elem == "balle":
            p=1

        if elem == "joueur":
            dessin.create_image(202,360)
            temps=20*diff
            legende.configure(text="Perdu !")
            return

    if y<705:
        z=dessin.create_image(x, y, image=photo4,tags="balle")
        root.after(10,lambda:MoveBarrière(x,y,z))


def GetTagFromId(t):
    t = list(t)
    for i in range(len(t)):
        t[i] = dessin.gettags(t[i])[0]
    return t

root = Tk()
niveau=0

temps=20*diff

legende  = Label(root, text=temps)
legende.pack()

def timer():
    global temps
    temps-=1
    legende.configure(text=temps)
    if temps==0:
        root.destroy()
    else:
        root.after(1000,timer)


dessin = Canvas(root, bg='white', height=805, width=720)
dessin.pack()



pos1 = 805/2
pos2 = -805/2

bg = PhotoImage(master=root,file="Data/Autres/CPC/bg.png")

dessin.create_image(720/2,pos1,image=bg,tags="plaine1")
dessin.create_image(720/2,pos2,image=bg,tags="plaine2")

def UpdateScrollDownGrass():
    global pos1,pos2
    pos1+=2
    pos2+=2
   
    if pos1 >= 805+805/2-2:
        pos1 = -805/2
    if pos2 >= 805+805/2-2:
        pos2 = -805/2
    
    dessin.coords("plaine1",720/2,pos1)
    dessin.coords("plaine2",720/2,pos2)

    root.after(5,UpdateScrollDownGrass)

dessin.create_line(240,0,240,805)
dessin.create_line(480,0,480,805)
dessin.create_image(202,360)



photo = PhotoImage(master=root,file="Data/Autres/CPC/perso.png")
xperso=360
yperso=255
dessin.create_image(xperso, yperso, image=photo,tags="joueur")

photo2 = PhotoImage(master=root,file="Data/Autres/CPC/balle.png")
photo3 = PhotoImage(master=root,file="Data/Autres/CPC/chasseur.png")
photo4 = PhotoImage(master=root,file="Data/Autres/CPC/barrière.png")

xchasseur=360
ychasseur=705
p=0
dessin.create_image(xchasseur, ychasseur, image=photo3,tags="chasseur")


root.bind("<Left>", gauche)
root.bind("<Right>", droite)

UpdateScrollDownGrass()
TirreBalle()
appbarrière()
timer()
root.mainloop()
