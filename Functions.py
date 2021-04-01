from Engine import *
from random import *

def ClickEvent_Decor(target):
    Visuel.tag_bind("Decor","<Button-1>",Visuel.tag_bind("Decor","<Button-1>",lambda arg=0 : TableauSuivant(target)))

def ClickEvent_Perso(target):
    Visuel.tag_bind("Perso","<Button-1>",Visuel.tag_bind("Perso","<Button-1>",lambda arg=0 : TableauSuivant(target)))


def GetPageOne():
    ModifVar("page1",True)
    TableauSuivant("ChezHarold_Reveil_9")

def ClickEvent_GetPageOne():
    Visuel.tag_bind("Decor","<Button-1>",Visuel.tag_bind("Decor","<Button-1>",lambda arg=0 : GetPageOne()))

def GetPageTwo():
    ModifVar("page2",True)
    TableauSuivant("ChezChasseur_Arrive")

def ClickEvent_GetPageTwo():
    Visuel.tag_bind("Decor","<Button-1>",Visuel.tag_bind("Decor","<Button-1>",lambda arg=0 : GetPageTwo()))
