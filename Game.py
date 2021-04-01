# Boucle Principal + Menu par Julien

from Engine import *
from Pages import *
from Livre import *
from Cartes import *
from MiniMap import *

from random import *
import os

Init()
RenameWindow("Harold's Quest 2")

def AddCustomMenu():
    Visuel.create_image(146,516,image=D_Data["Icons"]["pages"],tags="Pages_Button")
    Visuel.tag_bind("Pages_Button","<Button-1>",lambda arg=0:PagesWindow())
    Visuel.create_image(178,516,image=D_Data["Icons"]["livre"],tags="Dic_Button")
    Visuel.tag_bind("Dic_Button","<Button-1>",lambda arg=0:DicWindow())
    Visuel.create_image(210,516,image=D_Data["Icons"]["card"],tags="Card_Button")
    Visuel.tag_bind("Card_Button","<Button-1>",lambda arg=0:CardsWindow())
    Visuel.create_image(242,516,image=D_Data["Icons"]["map"],tags="Map_Button")
    Visuel.tag_bind("Map_Button","<Button-1>",lambda arg=0:MapWindow())
    
def NewGame():
    name = simpledialog.askstring("HQ2","Quel est votre nom ?")
    if name != "":
        ModifVar("PlayerName",name)
    else:
        ModifVar("PlayerName","Héro")
    menu.pack_forget()
    Apparition()
    AddCustomMenu()
    TableauSuivant("?_Prologue")


def LoadSave():
    menu.pack_forget()
    Apparition()
    AddCustomMenu()
    Chargement("save.sav")

    
    
img = PhotoImage(file="Data//Autres//HQ2.png")
img2 = PhotoImage(file="Data//Autres//HQ2_white.png")
img5 = PhotoImage(file="Data//Autres//HQ2_secret.png")
img3 = PhotoImage(file="Data//Autres//Menu//s.png")
img4 = PhotoImage(file="Data//Autres//Menu//screamer.png")
img_fort_normal = PhotoImage(file="Data//Autres//Menu//tour_normal.png")
img_fort_vrai = PhotoImage(file="Data//Autres//Menu//tour_vrai.png")
D_Menu = [PhotoImage(file="Data//Autres//Menu//menu1.png"),
          PhotoImage(file="Data//Autres//Menu//menu2.png"),
          PhotoImage(file="Data//Autres//Menu//menu3.png"),
          PhotoImage(file="Data//Autres//Menu//menu4.png"),
          PhotoImage(file="Data//Autres//Menu//menu5.png")]
menu = Canvas(fenetre,width=400,height=300)
menu.pack()
curr = 0


def SetUpDifficulty():
    menu.delete("ng")
    menu.delete("c")

    menu.create_rectangle(25,205,125,225,fill="green",tags="t1")
    menu.create_text(75,215,text="Facile",tags="t1")
    menu.tag_bind("t1","<Button-1>",lambda arg=1:SetDifficulty(1))

    menu.create_rectangle(150,205,250,225,fill="orange",tags="t2")
    menu.create_text(200,215,text="Normal",tags="t2")
    menu.tag_bind("t2","<Button-1>",lambda arg=2:SetDifficulty(2))

    menu.create_rectangle(275,205,375,225,fill="red",tags="t3")
    menu.create_text(325,215,text="Difficile",tags="t3")
    menu.tag_bind("t3","<Button-1>",lambda arg=3:SetDifficulty(3))
    

def SetDifficulty(diff):
    ModifVar("difficulte",diff)
    NewGame()
    

def StartScreenNormal():
    global curr
    if curr == 0:
        menu.delete("egg")
        SetMusic("Menu")
    if 0 <= curr <= 50:
        menu.move("t",0,1)
    if 50 <= curr <= 100:
        menu.move("but",0,-2)
    elif curr == 101:
        menu.tag_bind("ng","<Button-1>",lambda arg=0:SetUpDifficulty())
        menu.tag_bind("c","<Button-1>",lambda arg=0:LoadSave())

    menu.update()
    if curr != 101:
        curr+=1;
        fenetre.after(10,StartScreenNormal)



def EasterEggDialog1():
    global curr
    if curr == 300:
        PlaySE("Cerf_1")
        menu.itemconfigure("dia",fill="red",text="Parfait, tout ce déroule comme prévu")
    elif curr == 600:
        PlaySE("Cerf_1")
        menu.itemconfigure("dia",fill="red",text="Vous êtes comme toujours mon plus fidèle serviteur")
    elif curr == 900:
        PlaySE("Cerf_1")
        menu.itemconfigure("dia",fill="red",text="Bientôt, le monde sera à nos pieds, et vous serez à mes cotés")
    elif curr == 1200:
        menu.itemconfigure("dia",fill="white",text="Oui...maitre...")   
    elif curr == 1500:
        curr = 0
        StartScreenNormal()
        return

    menu.update()
    if curr != 1500:
        curr+=1;
        fenetre.after(10,EasterEggDialog1)

def EasterEggDialog2():
    global curr
    if curr == 300:
        menu.itemconfigure("dia",fill="white",text="J'ai une très bonne nouvelle pour vous")
    elif curr == 600:
        menu.itemconfigure("dia",fill="white",text="Un confrère va bientôt vous rejoindre")
    elif curr == 900:
        menu.itemconfigure("dia",fill="white",text="Avec vos forces combinées, vous serez instopables")
    elif curr == 1200:
        menu.itemconfigure("dia",fill="white",text="Il m'a échappé la dernière fois, mais ne vous en faites pas")
    elif curr == 1500:
        menu.itemconfigure("dia",fill="white",text="Cette fois, je vais l'avoir")
    elif curr == 1800:
        menu.itemconfigure("dia",fill="lightgray",text="Oui...maitre...")   
    elif curr == 2100:
        curr = 0
        StartScreenNormal()
        return

    menu.update()
    if curr != 2100:
        curr+=1;
        fenetre.after(10,EasterEggDialog2)


tab = [
    "Crée par Julien, Mathis et Corentin",
    "Jouez à vos riques et périls",
    "Avez-vous collecté toute les pages ?",
    "Avez-vous collecté toute les cartes de RickeyLand ?",
    "Aimez-vous les Caribous ?",
    "Deja de retour ?",
    "Il est temps de jouer à nouveau",
    "Méfiez-vous du PDG",
    "2 fois plus fun !",
    "Harold a encore mangé tout le gateau"
    ]

def AfficheDefaultMenu():
    de = randint(0,4)
    menu.create_image(200,150,image=D_Menu[de])
    if de == 2:
        menu.create_image(200,50,image=img,tags="t")
    else:
        menu.create_image(200,50,image=img2,tags="t")
    menu.create_rectangle(150,305,250,325,fill="red",tags=("but","ng"))
    menu.create_text(200,315,text="Jouer",tags=("but","ng"))
    if os.path.exists("save.sav"):
        menu.create_rectangle(150,335,250,355,fill="red",tags=("but","c"))
        menu.create_text(200,345,text="Continuer",tags=("but","c"))

def ChooseMenu():
    menu.delete("all")
    de = randint(1,100)
    if 1 <= de <= 50 : # Menu Normal
        AfficheDefaultMenu()
        StartScreenNormal()
        
    elif  51 <= de <= 80 : # Menu Fort
        if randint(1,100) < 71:
            menu.create_image(200,150,image=img_fort_normal)
            menu.create_image(200,50,image=img,tags="t")
        else:
            PlaySE("menu_laugh")
            menu.create_image(200,150,image=img_fort_vrai)
            menu.create_image(200,50,image=img5,tags="t")
        menu.create_rectangle(150,305,250,325,fill="red",tags=("but","ng"))
        menu.create_text(200,315,text="Jouer",tags=("but","ng"))
        if os.path.exists("save.sav"):
            menu.create_rectangle(150,335,250,355,fill="red",tags=("but","c"))
            menu.create_text(200,345,text="Continuer",tags=("but","c"))
        StartScreenNormal()
        
    elif 81 <= de <= 85: # Easter Egg 1 (Yeux) 
        
        AfficheDefaultMenu()
        menu.create_rectangle(0,0,400,300,fill="black",tags="egg")
        menu.create_oval(150,150,160,160,fill="red",tags="egg")
        menu.create_oval(250,150,260,160,fill="red",tags="egg")
        PlaySE("Cerf_1")
        fenetre.after(1500,lambda:StartScreenNormal())

    elif 86 <= de <= 91: # Easter Egg 2 (Yeux+Texte)

        AfficheDefaultMenu()
        menu.create_rectangle(0,0,400,300,fill="black",tags="egg")
        menu.create_oval(150,150,160,160,fill="red",tags="egg")
        menu.create_oval(250,150,260,160,fill="red",tags="egg")
        PlaySE("Cerf_1")
        fenetre.after(2500,lambda:StartScreenNormal())

    elif 92 <= de <= 95: # Easter Egg 3 (Dialogue - 1)

        AfficheDefaultMenu()

        menu.create_rectangle(0,0,400,300,fill="black",tags="egg")
        menu.create_oval(150,150,160,160,fill="red",tags="egg")
        menu.create_oval(250,150,260,160,fill="red",tags="egg")
        menu.create_text(205,200,text="Tout ce passe comme prévu, il arrivera bientôt",fill="white",tags=("egg","dia"))
        EasterEggDialog1()

    elif 96 <= de <= 99: # Easter Egg 4 (Dialogue - 2) 

        AfficheDefaultMenu()

        menu.create_rectangle(0,0,400,300,fill="black",tags="egg")
        menu.create_image(200,250,image=img3,tags="egg")
        menu.create_text(205,200,text="Vous voila enfin...",fill="white",tags=("egg","dia"))
        EasterEggDialog2()

    elif de == 100: # Easter Egg 5 (Screamer)
        PlaySE("Cerf_2")
        menu.create_image(200,150,image=img4,tags="egg")
        fenetre.after(2000,lambda:exit())

de = randint(1,100)
if 1 <= de <= 91: # Jeu se lance Normalement
    menu.create_text(200,150,text=choice(tab))
    fenetre.after(1500,ChooseMenu)
elif 92 <= de <= 99: # Easter Egg 6 (DLC Missing)
    menu.create_text(200,150,text="Attention, il vous manque des DLCs pour pouvoir jouer ! \n -Premium Edition \n -Gold Edition \n -Game Of The Year Edition \n -Skin Packs n°1-50")
    fenetre.after(4000,lambda:exit())
else: # Easter Egg 7 (CoV)
    menu.create_text(200,150,text="Mini-jeu manquant !")
    fenetre.after(2000,lambda:exit())

fenetre.mainloop()
