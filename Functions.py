from Engine import *

from EV import *
from MHR import *
from TSS import *
from JDH import *
from T import *
from CR0 import *
from TSM import *
from CDC import *
from CPC import *
from CCC import *
from ST import *
from QW import *
from JV import *
from CQTE import *
from CPR import *

def ClickEvent_Decor(target):
    Visuel.tag_bind("Decor","<Button-1>",Visuel.tag_bind("Decor","<Button-1>",lambda arg=0 : TableauSuivant(target)))

def ClickEvent_Perso(target):
    Visuel.tag_bind("Perso","<Button-1>",Visuel.tag_bind("Perso","<Button-1>",lambda arg=0 : TableauSuivant(target)))
