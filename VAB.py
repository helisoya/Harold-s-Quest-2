# Vendeur de l'arrière boutique par mathis

from tkinter import *
from random import randint
import time

temps=3
score=0
objet=0
x=randint(1,4)
photo1 = 0
photo2 = 0
photo3 = 0
photo4 = 0
photo5 = 0

def MiniGame_VAB():
    global temps,score,objet,x,photo1,photo2,photo3,photo4,photo5

    minijeu = Tk()
    minijeu.title("Vendeur de l'Arrière Boutique")


    temps=3
    score=0
    objet=0
    x=randint(1,4)

    photo1 = PhotoImage(master=minijeu,file="Data/Autres/VAB/barbe_a_papa.png")
    photo2 = PhotoImage(master=minijeu,file="Data/Autres/VAB/glace.png")
    photo3 = PhotoImage(master=minijeu,file="Data/Autres/VAB/churros.png")
    photo4 = PhotoImage(master=minijeu,file="Data/Autres/VAB/pomme d'amour.png")
    photo5 = PhotoImage(master=minijeu,file="Data/Autres/VAB/bg.png")
    timer  = Label(minijeu, text='temps restant='+ str(temps))
    timer.pack()
    scorer  = Label(minijeu, text='score ='+ str(score))
    scorer.pack()

    def time():
        global temps,score,x
        temps-=1

        if temps==0:
            w=x
            while w==x:
                x=randint(1,4)
            temps=3
            score=0
            scorer.configure(text='score ='+ str(score))
        timer.configure(text='temps restant='+ str(temps))

        minijeu.after(1000,time)


    dessin = Canvas(minijeu, bg='white', height=605, width=1000)
    dessin.pack()

    def demande():
        global photo1
        global photo2
        global photo3
        global photo4
        global objet
        global x
        global score
        global temps
        if x==1:
            photo=photo1
        if x==2:
            photo=photo2
        if x==3:
            photo=photo3
        if x==4:
            photo=photo4

        dessin.delete("demande")
        z=dessin.create_image(400,400,image=photo,tag="demande")
        if objet !=() and dessin.itemcget(z,'image') == dessin.itemcget(objet,'image') and dessin.itemcget(objet, 'tag') != "demande":
            w=x
            while w==x:
                x=randint(1,4)
            score+=1
            scorer.configure(text='score ='+ str(score))
            temps=3
            timer.configure(text='temps restant='+ str(temps))

        minijeu.after(1,demande)

    def click(c):
        global objet
        objet = list(dessin.find_overlapping(c.x, c.y, c.x+1, c.y+1))
        objet.remove(1)


    time()
    dessin.create_image(500,605/2,image=photo5)
    dessin.create_image(175,100,image=photo1,tag="bapa")
    dessin.create_image(375,100,image=photo2,tag="glace")
    dessin.create_image(575,100,image=photo3,tag="churros")
    dessin.create_image(775,100,image=photo4,tag="pommour")
    minijeu.bind("<Button-1>", click)
    demande()
    minijeu.mainloop()
    
