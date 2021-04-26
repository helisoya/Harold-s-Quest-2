#Tir Sur Sbire par Mathis

from tkinter import *
from random import randint
import time

diff = 3



def NewGame():
    global photo,photo2,carest,temps,timeloop
    temps = 2000
    carest=5*diff
    dessin.delete("legende")

    if timeloop != 0:
        root.after_cancel(timeloop)
    
    dessin.create_image(0,0, anchor = NW, image=photo, tags="fond")
    dessin.create_text(5,10,anchor=W,text="Restant : "+str(carest),tags="nb",fill="white")
    dessin.create_text(5,30,anchor=W,text="Temps Restant : 20",tags="time",fill="white")

    crepersonnage() 

    temps1=time.perf_counter()
    root.bind("<Button-1>", deteclic)
    MoveSbire()
    timeloop = root.after(0,TimeLoop)


def crepersonnage(): # fonction pour faire apparaitre les personnages
    global x,y,dirX,dirY
    x=randint(0,375)
    y=randint(0,690)
    dirX = x
    dirY = y
    dessin.create_image(y, x, image=photo2,tags="sbire")




def deteclic(event):
    global carest
    global photo3
    xsouris, ysouris = event.x, event.y

    objet = dessin.find_closest(xsouris, ysouris) #j'utilise la fonction find_closest pour obtenir l'objet sur lequel j'ai cliquer


    type = dessin.itemcget(objet[0], 'tags')
    
    if type=="sbire current":    #cette condition nous permet de rentrer dans la boucle seulement si on clique sur un ennemie est pas sur le fond

        dessin.tag_raise("time")
        dessin.tag_raise("nb")
        dessin.itemconfigure(objet[0], image=photo3)
        dessin.itemconfigure(objet[0], tags='mort')
        carest-=1
        dessin.itemconfigure("nb",text="Restant : "+str(carest))
        if carest!=0: # on vérifie que le nombre de personnage a tuer avant la fin du niveau n'est pas de 0
            crepersonnage()


    if carest==0: # End Script
        root.destroy()
        return 




def MoveSbire():
    global x,y,dirX,dirY

    if ( dirX-5 < x < dirX+5 ) and ( dirY-5 < y < dirY+5 ):
        dirY = randint(20,680)
        dirX = randint(20,370)
        
    if x < dirX:
        x+=1.5*diff
    elif x > dirX:
        x-=1.5*diff

    if y < dirY:
        y+=1.5*diff
    elif y > dirY:
        y-=1.5*diff
        
    dessin.delete("sbire")
    if x>375 :
        x=375
    if y>690:
        y=690
    if x<10 :
        x=10
    if y<10:
        y=10
    dessin.create_image(y, x, image=photo2,tags="sbire")
    root.after(5,MoveSbire)

def TimeLoop():
    global timeloop,temps,carest

    temps-=1

    dessin.itemconfigure("time",text="Temps : "+str(round(temps/100)))

    if round(temps/100) == 0:
        temps = 2000
        carest = 5*diff
    timeloop = root.after(8,TimeLoop)

root = Tk()

photo = PhotoImage(file="Data\\Autres\\TSS\\paysage.png")
photo2 = PhotoImage(file="Data\\Autres\\TSS\\sbire.png")





carest=0#cette variable va nous permettre de connaitre le nombre de personnage à tuer avant la fin du niveau
x=0
y=0
dirX = 0
dirY = 0
timeloop = 0
temps = 2000

photo3 = PhotoImage(file="Data\\Autres\\TSS\\mort.png")
dessin = Canvas(root, bg='white', height=405, width=720)
dessin.pack()


dessin.create_text(720/2,405/2,text="Cliquez sur les sbires avant le temps impartis !",tags="legende")
root.after(2000,NewGame)


root.mainloop()
