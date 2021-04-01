# Menu des Cartes à collectionner par Julien


from tkinter import *
from Engine import *


def CardsWindow():
    cartes = Tk()
    cartes.title("Cartes")

    dic = {}

    dic["unknow"] = PhotoImage(master=cartes,file="Data\\Autres\\Cartes\\Unknow.png")
    dic["harold"] = PhotoImage(master=cartes,file="Data\\Autres\\Cartes\\Harold.png")
    dic["harold_fete"] = PhotoImage(master=cartes,file="Data\\Autres\\Cartes\\Harold_Fete.png")
    dic["rickey"] = PhotoImage(master=cartes,file="Data\\Autres\\Cartes\\Rickey.png")
    dic["waldo"] = PhotoImage(master=cartes,file="Data\\Autres\\Cartes\\Waldo.png")
    dic["waldo_cuisine"] = PhotoImage(master=cartes,file="Data\\Autres\\Cartes\\Waldo_Cuisine.png")
    dic["waldo_uniforme"] = PhotoImage(master=cartes,file="Data\\Autres\\Cartes\\Waldo_Uniforme.png")
    dic["garde"] = PhotoImage(master=cartes,file="Data\\Autres\\Cartes\\Garde.png")
    dic["garde_cagoule"] = PhotoImage(master=cartes,file="Data\\Autres\\Cartes\\Garde_Cagoule.png")
    dic["garde_uniforme"] = PhotoImage(master=cartes,file="Data\\Autres\\Cartes\\Garde_Uniforme.png")

    can = Canvas(cartes,width=150*3,height=175*3)
    can.pack()

    col = 1
    rang = 1
    
    for key in dic.keys():
        if key != "unknow":
            str_img = key
            if not GetVar("card_"+key):
                str_img = "unknow"

            can.create_image(75*col+75*(col-1),(175/2)*rang+(175/2)*(rang-1),image=dic[str_img])
            col+=1
            if col == 4:
                col = 1
                rang+=1

    cartes.mainloop()
