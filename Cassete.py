# Menu des Cassettes à collectionner par Julien


from tkinter import *
from Engine import *

from COV import *


def CasWindow():
    cas = Tk()
    cas.title("Cassettes")

    dic = {}

    dic["unknow"] = PhotoImage(master=cas,file="Data\\Autres\\Tapes\\Unknow.png")
    dic["cov"] = PhotoImage(master=cas,file="Data\\Autres\\Tapes\\CoV.png")
    dic["vab"] = PhotoImage(master=cas,file="Data\\Autres\\Tapes\\VAB.png")
    dic["fh"] = PhotoImage(master=cas,file="Data\\Autres\\Tapes\\FH.png")


    can = Canvas(cas,width=150*3,height=175)
    can.pack()


    for i in range(1,4):
        can.create_image(75*i+75*(i-1),175/2,image=dic["unknow"],tags="b"+str(i))


    if GetVar("cas_arc"):
        can.itemconfigure("b1",image=dic["cov"])
        can.tag_bind("b1","<Button-1>",lambda e=0: MiniGame_COV())
    if GetVar("cas_toque"):
        can.itemconfigure("b2",image=dic["fh"])
    if GetVar("cas_casque"):
        can.itemconfigure("b3",image=dic["vab"])


    cas.mainloop()

