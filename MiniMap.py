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
        "RickeyLandStatue":"Entrée du Parc",
        "RickeyLandWaldo":"Quiz de Waldo",
        "RickeyLandHorse":"Centre Hippique",
        "RickeyLandHante":"Maison Hantée",
        "RickeyLandMarchand":"Tir sur Marchand",
    }

    dic = {}

    dic["map"] = PhotoImage(master=map,file="Data\\Autres\\Map.png")
    dic["map_parc"] = PhotoImage(master=map,file="Data\\Autres\\Map_Parc.png")

    text = Label(map,text="Objectif : "+objectives[GetVar("quest")])
    text.pack()
    can = Canvas(map,width=500,height=332)
    can.pack()

    def Select(tag):
        if not GetVar("canMove") or ( "ext" in can.gettags("current") and not GetVar("exterieur")) or ( "parc" in can.gettags("current") and GetVar("exterieur")) :
            return
        ok = messagebox.askyesno("Déplacement","Voulez-vous aller à : "+names[tag])

        if ok:
            Destroy()
            if GetVar("quest") == 3 and tag == "RickeyLandEntree" and not GetVar("foughtArcher"):
                TableauSuivant("Event_Archer_1")
            else:
                TableauSuivant(tag+"_Arrive")

    if GetVar("exterieur"): # Map Région
        can.create_image(500/2,332/2,image=dic["map"])

        if "ChezHarold" in GetVar("Current"):
            can.create_rectangle(124,280,134,290,fill="green",activefill="blue",tags=("ChezHarold","ext"))
        else:
            can.create_rectangle(124,280,134,290,fill="red",activefill="blue",tags=("ChezHarold","ext"))

        if "ChezChasseur" in GetVar("Current"):
            can.create_rectangle(114,239,124,249,fill="green",activefill="blue",tags=("ChezChasseur","ext"))
        else:
            can.create_rectangle(114,239,124,249,fill="red",activefill="blue",tags=("ChezChasseur","ext"))

        if "RickeyLand" in GetVar("Current"):
            can.create_rectangle(190,178,200,188,fill="green",activefill="blue",tags=("RickeyLandEntree","ext"))
        else:
            can.create_rectangle(190,178,200,188,fill="red",activefill="blue",tags=("RickeyLandEntree","ext"))

        can.tag_bind("ChezHarold","<Button-1>",lambda arg=0:Select("ChezHarold"))
        can.tag_bind("ChezChasseur","<Button-1>",lambda arg=0:Select("ChezChasseur"))
        can.tag_bind("RickeyLandEntree","<Button-1>",lambda arg=0:Select("RickeyLandEntree"))

    else:
        can.create_image(500/2,332/2,image=dic["map_parc"])

        if "RickeyLandStatue" in GetVar("Current"):
            can.create_rectangle(179,254,189,264,fill="green",activefill="blue",tags=("RickeyLandStatue","parc"))
        else:
            can.create_rectangle(179,254,189,264,fill="red",activefill="blue",tags=("RickeyLandStatue","parc"))

        if "RickeyLandWaldo" in GetVar("Current"):
            can.create_rectangle(69,148,79,158,fill="green",activefill="blue",tags=("RickeyLandWaldo","parc"))
        else:
            can.create_rectangle(69,148,79,158,fill="red",activefill="blue",tags=("RickeyLandWaldo","parc"))

        if "RickeyLandHorse" in GetVar("Current"):
            can.create_rectangle(358,61,368,71,fill="green",activefill="blue",tags=("RickeyLandHorse","parc"))
        else:
            can.create_rectangle(358,61,368,71,fill="red",activefill="blue",tags=("RickeyLandHorse","parc"))

        if "RickeyLandHante" in GetVar("Current"):
            can.create_rectangle(92,53,102,63,fill="green",activefill="blue",tags=("RickeyLandHante","parc"))
        else:
            can.create_rectangle(92,53,102,63,fill="red",activefill="blue",tags=("RickeyLandHante","parc"))

        if "RickeyLandMarchand" in GetVar("Current"):
            can.create_rectangle(383,181,393,191,fill="green",activefill="blue",tags=("RickeyLandMarchand","parc"))
        else:
            can.create_rectangle(383,181,393,191,fill="red",activefill="blue",tags=("RickeyLandMarchand","parc"))

        can.tag_bind("RickeyLandStatue","<Button-1>",lambda arg=0:Select("RickeyLandStatue"))
        can.tag_bind("RickeyLandWaldo","<Button-1>",lambda arg=0:Select("RickeyLandWaldo"))
        can.tag_bind("RickeyLandHorse","<Button-1>",lambda arg=0:Select("RickeyLandHorse"))
        can.tag_bind("RickeyLandHante","<Button-1>",lambda arg=0:Select("RickeyLandHante"))
        can.tag_bind("RickeyLandMarchand","<Button-1>",lambda arg=0:Select("RickeyLandMarchand"))

    map.mainloop()
