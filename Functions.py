from Engine import *

def ClickEvent_IntroGetFirstCard():
    Visuel.tag_bind("Perso","<Button-1>",Visuel.tag_bind("Perso","<Button-1>",lambda arg=0 : TableauSuivant("IntroHarold_47")))
    
def ClickEvent_ReveilEasterEgg():
    Visuel.tag_bind("Decor","<Button-1>",Visuel.tag_bind("Decor","<Button-1>",lambda arg=0 : TableauSuivant("ChezHarold_ReveilEasterEgg_1")))
    
def GetPageOne():
    ModifVar("page1",True)
    TableauSuivant("ChezHarold_Reveil_9")
    
def ClickEvent_GetPageOne():
    Visuel.tag_bind("Decor","<Button-1>",Visuel.tag_bind("Decor","<Button-1>",lambda arg=0 : GetPageOne()))