from Engine import *

from EV import *
from MHR import *

def ClickEvent_Decor(target):
    Visuel.tag_bind("Decor","<Button-1>",Visuel.tag_bind("Decor","<Button-1>",lambda arg=0 : TableauSuivant(target)))

def ClickEvent_Perso(target):
    Visuel.tag_bind("Perso","<Button-1>",Visuel.tag_bind("Perso","<Button-1>",lambda arg=0 : TableauSuivant(target)))
