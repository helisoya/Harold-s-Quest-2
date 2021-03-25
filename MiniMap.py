# MiniMap + Objectifs par Julien

from tkinter import *
from Engine import *
from tkinter import messagebox

def MapWindow():

    if GetVar("mapOpened"):
        return True

    ModifVar("mapOpened",True)
    map = Tk()
    map.title("MiniMap")

    def Destroy():
        ModifVar("mapOpened",False)
        map.destroy()

    map.protocol("WM_DELETE_WINDOW", Destroy)

    objectives = [
        "Finir le Prologue",
        "Aller à Rickeyland",
        "Trouver une invitation",
        "Acceder à Rickeyland",
        "Finir les 4 attractions",
        "Aller au palais de Rickey",
        "Survivre",
        "Retourner voir Harold",
        "Confronter Harold",
        ]

    names = {
        "ChezHarold":"4 rue du Cerf",
        "ChezChasseur":"3 rue du Merle",
        "RickeyLandEntree":"RickeyLand",
    }

    dic = {}

    dic["map"] = PhotoImage(master=map,file="Data\\Autres\\Map.png")

    text = Label(map,text="Objectif : "+objectives[GetVar("quest")])
    text.pack()
    can = Canvas(map,width=500,height=332)
    can.pack()

    def Select(tag):
        if not GetVar("canMove"):
            return
        ok = messagebox.askyesno("Déplacement","Voulez-vous aller à : "+names[tag])

        if ok:
            Destroy()
            TableauSuivant(tag+"_Arrive")

    can.create_image(500/2,332/2,image=dic["map"])
    
    if "ChezHarold" in GetVar("Current"):
        can.create_rectangle(124,280,134,290,fill="green",tags="ChezHarold")
    else:
        can.create_rectangle(124,280,134,290,fill="red",tags="ChezHarold")

    if "ChezChasseur" in GetVar("Current"):
        can.create_rectangle(114,239,124,249,fill="green",tags="ChezChasseur")
    else:
        can.create_rectangle(114,239,124,249,fill="red",tags="ChezChasseur")

    if "RickeyLand" in GetVar("Current"):
        can.create_rectangle(190,178,200,188,fill="green",tags="RickeyLandEntree")
    else:
        can.create_rectangle(190,178,200,188,fill="red",tags="RickeyLandEntree")

    can.tag_bind("ChezHarold","<Button-1>",lambda arg=0:Select("ChezHarold"))
    can.tag_bind("ChezChasseur","<Button-1>",lambda arg=0:Select("ChezChasseur"))
    can.tag_bind("RickeyLandEntree","<Button-1>",lambda arg=0:Select("RickeyLandEntree"))

    map.mainloop()
