#Tir Sur Sbire par Mathis

from tkinter import *
from random import randint
import time

diff = 3

def niveau1():
    global photo
    global photo2
    global carest
    global temps1
    global niveau
    niveau=1
    carest=5
    dessin.create_image(0,0, anchor = NW, image=photo, tags="fond")


    for k in range(carest): # pour le niveau 1 je créer directement directement tout les ennemis
        x=randint(0,375)
        y=randint(0,690)
        dessin.create_image(y, x, image=photo2,tags="sbire")

    temps1=time.perf_counter()
    root.bind("<Button-1>", deteclic) #la fonction deteclic va se faire à chaque fois qu'on appuis sur le bouton gauche de la souris

    root.mainloop()


def niveau2():
    global photo
    global photo2
    global carest
    global temps1
    global niveau
    niveau=2
    carest=10
    dessin.create_image(0,0, anchor = NW, image=photo, tags="fond")

    crepersonnage() # pour les niveau 2 et 3 j'utilise une fonction que j'appelerais des qu'on touche un ennemi

    temps1=time.perf_counter()
    root.bind("<Button-1>", deteclic)

    root.mainloop()

def niveau3():
    global photo
    global photo2
    global carest
    global temps1
    global niveau
    niveau=2
    carest=15
    dessin.create_image(0,0, anchor = NW, image=photo, tags="fond")

    crepersonnage() # pour les niveau 2 et 3 j'utilise une fonction que j'appelerais des qu'on touche un ennemi

    temps1=time.perf_counter()
    root.bind("<Button-1>", deteclic)
    MoveSbire()
    root.mainloop()


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
    global compteur
    global temps1
    global temps2
    global niveau
    xsouris, ysouris = event.x, event.y

    objet = dessin.find_closest(xsouris, ysouris) #j'utilise la fonction find_closest pour obtenir l'objet sur lequel j'ai cliquer


    type = dessin.itemcget(objet[0], 'tags')
    
    if type=="sbire current":    #cette condition nous permet de rentrer dans la boucle seulement si on clique sur un ennemie est pas sur le fond

        dessin.itemconfigure(objet[0], image=photo3)
        dessin.itemconfigure(objet[0], tags='mort')
        carest-=1
        if niveau != 1 and carest!=0: # on vérifie qu'on ne soit pas dans le niveau 1 car il n'y a pas besoin de créer de personnage dans ce niveau et que le nombre de personnage a tuer avant la fin du niveau n'est pas de 0
            crepersonnage()


    else:
        compteur+=1
    if carest==0:

        temps2=time.perf_counter()
        temps=temps2-temps1 #on soustrai le temps au début et à la fin du programme
        legende['text'] = 'vous avez réussi  en '+str(round(temps))+'s , nombre de tir manqué:'+str(compteur)


    root.mainloop()

def MoveSbire():
    global x,y,dirX,dirY

    if ( dirX-5 < x < dirX+5 ) and ( dirY-5 < y < dirY+5 ):
        dirY = randint(20,680)
        dirX = randint(20,370)
        
    if x < dirX:
        x+=2
    elif x > dirX:
        x-=2

    if y < dirY:
        y+=2
    elif y > dirY:
        y-=2
        
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



root = Tk()

legende  = Label(root, text='tirer sur les ennemies')
legende.pack()
photo = PhotoImage(file="Data\\Autres\\TSS\\paysage.png")
photo2 = PhotoImage(file="Data\\Autres\\TSS\\sbire.png")


compteur = 0

temps1=0#je créer 2 variables temps pour avoir la différence de temps entre le début et la fin du minijeu
temps2=0
carest=0#cette fonction va nous permettre de connaitre le nombre de personnage à tuer avant la fin du niveau
x=0
y=0
dirX = 0
dirY = 0

photo3 = PhotoImage(file="Data\\Autres\\TSS\\mort.png")
dessin = Canvas(root, bg='white', height=405, width=720)
dessin.pack()

if diff == 1:
    niveau1()
elif diff == 2:
    niveau2()
else:
    niveau3()


root.mainloop()
