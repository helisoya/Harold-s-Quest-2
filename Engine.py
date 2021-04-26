#-------------------------------------------------------------
#------------------------ GAME CORE --------------------------
#-------------------------------------------------------------
#----------------- !!! NE PAS MODIFIER !!! -------------------

Engine_Version = "3.6.4" # Version du Moteur

from tkinter import *
from tkinter import simpledialog
from time import *
from random import *
import pygame
from pygame import mixer
import os
from io import *
from winsound import *
import zipfile


pygame.init()

if pygame.mixer.get_init() != None:
    Cvoix = pygame.mixer.Channel(0)
    CBGM = pygame.mixer.Channel(1)
    CSE = pygame.mixer.Channel(2)

fenetre = Tk()
fenetre.title("Game Core")

GameInfo = {}
D_Tableaux = {}
D_Data = {"BGM":{},
          "SE":{},
          "Decor":{},
          "Voix":{},
          "Persos":{},
          "Icons":{}}
Dic_Variables = {
        "Current":{
        "save":True,
        "type":"str",
        "valeur":"",},

    "TableauId":{
    "save":True,
    "type":"int",
    "valeur":0,},

    "CurrentImg":{
    "save":True,
    "type":"_",
    "valeur":None,},

    "Skiped":{
    "save":False,
    "type":"bool",
    "valeur":False,},

    "IsUsingSpeak":{
    "save":True,
    "type":"bool",
    "valeur":False,},

    "CurrentMusic":{
        "save":False,
        "type":"str",
        "valeur":"",},

    "PlayerName":{
        "save":True,
        "type":"str",
        "valeur":"SwagMaster",},

    "TWESpeed":{
        "save":False,
        "type":"int",
        "valeur":75,},

    "MusicVolume":{
        "save":False,
        "type":"float",
        "valeur":0.15,},

    "VoiceVolume":{
        "save":False,
        "type":"float",
        "valeur":0.80,},

    "SEVolume":{
        "save":False,
        "type":"float",
        "valeur":0.20,}}


Visuel = Canvas(fenetre,height=532,width=400)

Next1 = Button(fenetre, text=">",overrelief="groove")
Next2 = Button(fenetre, text=">",overrelief="groove")
Next3 = Button(fenetre, text=">",overrelief="groove")
Next4 = Button(fenetre, text=">",overrelief="groove")




def DisableWindow():
    """

    Désactive la fenetre de jeu

    """
    fenetre.attributes('-disabled', True)
    
def EnableWindow():
    """

    Active la fenetre de jeu

    """
    fenetre.attributes('-disabled', False)

def RenameWindow(New):
    """

    Renome la fenetre de jeu

    """
    fenetre.title(New)

def CrashReport(text):
    """

    Effectue un rapport de crash

    """
    with open("crashlog.txt","w") as log:
        log.write(os.environ['COMPUTERNAME'])
        log.write("\n"+str(localtime()))
        log.write("\nRapport d'Erreur :")
        log.write("\n"+text)
    exit()



def Blank():
    """

    Fonction bateau

    """
    pass


def GetVar(cle):
    """

    Renvoie la valeur associée à la clé

    """
    return Dic_Variables[cle]["valeur"]


def ModifVar(cle,val):
    """

    Modifie la valeur associé à la clée

    """
    global Dic_Variables
    if Dic_Variables[cle]["type"] == "_" or type(val) == eval(Dic_Variables[cle]["type"]) :
        Dic_Variables[cle]["valeur"] = val
        if cle == "MusicVolume":
            CBGM.set_volume(GetVar("MusicVolume"))
        elif cle == "VoiceVolume":
            Cvoix.set_volume(GetVar("VoiceVolume"))
        elif cle == "SEVolume":
            CSE.set_volume(GetVar("SEVolume"))
        if cle in ["SEVolume","VoiceVolume","MusicVolume","TWESpeed"]:
            Sauvegarde("settings.sav")

def QuitGame():
    """

    Fonction pour quitter le jeu

    """
    exit()

fenetre.protocol("WM_DELETE_WINDOW", QuitGame)

def CheckIfExist(tag):
    """

    Verifie si le tag existe dans le visuel

    """
    if len(Visuel.find_withtag(tag)) != 0:
        return True
    return False

def SetVoix(Voix):
    """

    Change la voix utilisé (facultatif)

    """

    if pygame.mixer.get_init() != None:
        Cvoix.set_volume(GetVar("VoiceVolume"))
        if Voix != None:
            if type(Voix) != str:
                CrashReport("Erreur : "+str(Voix)+" n'est pas une chaine de caractères")
            if not Voix in D_Data["Voix"].keys():
                CrashReport("Erreur : "+Voix+" n'est pas un fichier audio répertorié")
            Cvoix.fadeout(1)
            Cvoix.play(D_Data["Voix"][Voix])

def PlaySE(Sound):
    """

    Joue un effet sonore

    """

    if pygame.mixer.get_init() != None:
        CSE.set_volume(GetVar("SEVolume"))
        if Sound != None:
            if type(Sound) != str:
                CrashReport("Erreur : "+str(Sound)+" n'est pas une chaine de caractères")
            if not Sound in D_Data["SE"].keys():
                CrashReport("Erreur : "+Sound+" n'est pas un fichier audio répertorié")
            CSE.play(D_Data["SE"][Sound])

def SetMusic(Mus):
    """

    Change la musique
    Sauvegarde la nouvelle musique dans CurrentMusic

    """

    if pygame.mixer.get_init() != None:
        if Mus != None:
            if type(Mus) != str:
                CrashReport("Erreur : "+str(Mus)+" n'est pas une chaine de caractères")
            if GetVar("CurrentMusic") != Mus or not CBGM.get_busy():
                CBGM.set_volume(GetVar("MusicVolume"))
                if not Mus in D_Data["BGM"].keys():
                    CrashReport("Erreur : "+Mus+" n'est pas un fichier audio répertorié")
                ModifVar("CurrentMusic",Mus)
                CBGM.fadeout(200)
                CBGM.play(D_Data["BGM"][Mus],-1)
        else:
            CBGM.fadeout(200)


def SetPerso(Person,Couleur):
    """

    Change le nom et la couleur du perso

    """
    if type(Person) != str:
        CrashReport("Erreur : "+str(Person)+" n'est pas une chaine de caractères")
    if type(Couleur) != str:
        CrashReport("Erreur : "+str(Couleur)+" n'est pas une chaine de caractères")
    if Person == "!Player":
        Person = GetVar("PlayerName")
    Visuel.itemconfigure("Dialog_Perso",text=Person,fill=Couleur)

def SetDialogue(Texte,Id):
    """

    Change le contenu du dialogue

    """
    if type(Texte) != str:
        CrashReport("Erreur : "+Texte+" n'est pas une chaine de caractères")
    #Dialogue.configure(text=Texte)
    Texte = Texte.replace("!Player",GetVar("PlayerName"))
    if Texte != "":
        TypeWriterEffect(0,Texte,Id)

def ImageSetUseSpeak(Image):
    """

    Regarde si l'image est en capacité d'utiliser le speak

    """
    if "speak" in list(D_Data["Persos"][Image].keys()) and D_Tableaux[GetVar("Current")]["UseSpeak"] == True:
        return True
    return False

def SetTitre(Text,Id,corID):
    """

    Changer le Texte du Titre

    """
    if type(Text) != str:
        CrashReport("Erreur : "+str(Text)+" n'est pas une chaine de caractères")
    #Visuel.itemconfigure("Text",text=Text)
    TypeWriterEffectTitle(0,Text,Id,corID)

def SkipText():
    """

    Passe l'effet écriture quand on clique avant qu'il soit fini

    """
    Cvoix.fadeout(1)
    txt = D_Tableaux[GetVar("Current")]["Dialogue"].replace("!Player",GetVar("PlayerName"))
    Visuel.itemconfigure("Dialog",text=txt)
    ModifVar("Skiped",True)

def TypeWriterEffect(counter,Text,Id):
    """

    Effet Ecriture

    """
    CorrectId = GetVar("Current")
    if counter <= len(Text) and Id == GetVar("TableauId") and not GetVar("Skiped"):
        Beep(37,1)
        Visuel.itemconfigure("Dialog",text=Text[:counter])

        if not D_Tableaux[CorrectId]["PersoImg"] == None:
            if type(D_Data["Persos"][D_Tableaux[CorrectId]["PersoImg"]]) == dict:
                if ImageSetUseSpeak(D_Tableaux[CorrectId]["PersoImg"]) and counter%2==0:
                    if str(Visuel.itemcget("Perso","image")) == str(D_Data["Persos"][D_Tableaux[CorrectId]["PersoImg"]]["speak"]):
                        fenetre.after(1, lambda: Visuel.itemconfigure("Perso",image=D_Data["Persos"][D_Tableaux[CorrectId]["PersoImg"]]["normal"][0]))
                    else:
                        fenetre.after(1, lambda: Visuel.itemconfigure("Perso",image=D_Data["Persos"][D_Tableaux[CorrectId]["PersoImg"]]["speak"]))
                    ModifVar("IsUsingSpeak",True)
                    if GetVar("CurrentImg") != None:
                        fenetre.after_cancel(GetVar("CurrentImg"))
                    Visuel.update()

        fenetre.after(GetVar("TWESpeed"), lambda: TypeWriterEffect(counter+1,Text,Id))
    elif Id == GetVar("TableauId"):
        SetFunction(D_Tableaux[GetVar("Current")]["Choix"])
        if not D_Tableaux[CorrectId]["PersoImg"] == None:
            if type(D_Data["Persos"][D_Tableaux[CorrectId]["PersoImg"]]) == dict:
                if ImageSetUseSpeak(D_Tableaux[CorrectId]["PersoImg"]):
                    fenetre.after(1, lambda: Visuel.itemconfigure("Perso",image=D_Data["Persos"][D_Tableaux[CorrectId]["PersoImg"]]["speak"]))
                    ModifVar("IsUsingSpeak",False)
                    AnimationPersoVisuel(D_Tableaux[CorrectId]["PersoImg"],0)


def TypeWriterEffectTitle(counter,Text,Id,corID):
    """

    Effet Ecriture pour Titre

    """
    if counter <= len(Text) and Id == GetVar("TableauId"):
        Beep(37,1)
        Visuel.itemconfigure("Text",text=Text[:counter])
        fenetre.after(GetVar("TWESpeed"), lambda: TypeWriterEffectTitle(counter+1,Text,Id,corID))
    elif Id == GetVar("TableauId") and corID[:2] == "?_":
        fenetre.after(2000, lambda: TableauSuivant(D_Tableaux[corID]["Suite"]))


def SetScrollingTitre(Text,Id,Next):
    """

    Ajouter un texte defilant

    """
    if type(Text) != str:
        CrashReport("Erreur : "+str(Text)+" n'est pas une chaine de caractères")
    Visuel.itemconfigure("ScrollText",text=Text)
    ScrollingTitleEffect(Text,Id,Next)

def ScrollingTitleEffect(Text,Id,Next):
    """

    Effet Defilant

    """
    if Visuel.bbox("ScrollText")[3] > 0 and Id == GetVar("TableauId"):
        Visuel.move("ScrollText",0,-0.3)
        fenetre.after(10, lambda: ScrollingTitleEffect(Text,Id,Next))

    else:
        Visuel.itemconfigure("ScrollText",text="")
        Visuel.move("ScrollText",0,int(Visuel['height']))
        if Id == GetVar("TableauId"):
            TableauSuivant(Next)

def MovePersoImg(X,Y):
    """

    deplace l'image du perso

    """
    Visuel.coords("Perso",X,Y)

def DeleteGUI(Id):
    """

    Supprime une réaction

    """
    Visuel.delete(Id)

def ShakeReaction(x,y):
    """

    Secoue une réaction

    """
    if len(Visuel.gettags("reaction")) > 0:
        Visuel.move("reaction",x,y)
        Visuel.update()
        fenetre.after(200, lambda:ShakeReaction(-x,-y))

def ShakeScreen(x,y,counter):
    """

    Secoue l'écran

    """
    if counter > 0:
        Visuel.move("all",x,y)
        Visuel.update()
        fenetre.after(200, lambda:ShakeScreen(-x,-y,counter-1))

def CreateReaction(text,col):
    """

    Crée une réaction

    """

    if not CheckIfExist("reaction"):
        if type(text) != str:
            CrashReport("Erreur : "+str(text)+" n'est pas une chaine de caractères")
        if type(col) != str:
            CrashReport("Erreur : "+str(col)+" n'est pas une chaine de caractères")

        Visuel.create_oval(50,50,100,100,fill="white",tags="reaction")
        Visuel.create_text(75,75,text=text,tags="reaction",fill=col)
        ShakeReaction(0,5)
        fenetre.after(2000, lambda:DeleteGUI("reaction"))

def CreateSystemMessage(text,col):
    """

    Crée un message système

    """
    if not CheckIfExist("systemMessage"):

        if type(text) != str:
            CrashReport("Erreur : "+str(text)+" n'est pas une chaine de caractères")
        if type(col) != str:
            CrashReport("Erreur : "+str(col)+" n'est pas une chaine de caractères")

        Visuel.create_rectangle(0,0,100,50,fill=col,tags="systemMessage")
        Visuel.create_text(50,25,text=text,tags="systemMessage")
        ShakeReaction(0,5)
        fenetre.after(1000, lambda:DeleteGUI("systemMessage"))

def CheckSameImage(Image,Cible):
    """

    Verifie si l'image est la même que celle utilisé

    """

    Img = Visuel.itemcget(Cible,"image")
    C = Cible
    if C == "Perso":
        C = "Persos"
    if C == "Decor":
        for item in D_Data[C][Image]:
            if str(item) == Img:
                return True
        return False
    else:
        for item in D_Data[C][Image]["normal"]:
            if str(item) == Img:
                return True
        return False

def SetDecor(Image):
    """

    Change le decor

    """
    if Image != None:

        if type(Image) != str:
            CrashReport("Erreur : "+str(Image)+" n'est pas une chaine de caractères")

        if not Image in D_Data["Decor"].keys():
            CrashReport("Erreur : "+Image+" n'est pas un fichier Image répertorié")

        if type(D_Data["Decor"][Image]) == list and not CheckSameImage(Image,"Decor"):
            AnimationDecor(Image,0)
        elif type(D_Data["Decor"][Image]) != list:
            Visuel.itemconfigure("Decor",image=D_Data["Decor"][Image])
    else:
        Visuel.itemconfigure("Decor",image="")

def AnimationDecor(Image,Counter):
    """

    Animation Decor

    """
    if Image == D_Tableaux[GetVar("Current")]["Decor"]:
        if Counter > len(D_Data["Decor"][Image])-1:
            Counter = 0
        Visuel.itemconfigure("Decor",image=D_Data["Decor"][Image][Counter])
        fenetre.after(100, lambda: AnimationDecor(Image,Counter+1))


def SetPersoVisuel(Image):
    """

    Change le personnage

    """


    if Image != None:


        if type(Image) != str:
            CrashReport("Erreur : "+str(Image)+" n'est pas une chaine de caractères")

        if not Image in D_Data["Persos"].keys():
            CrashReport("Erreur : "+Image+" n'est pas un fichier Image répertorié")

        if type(D_Data["Persos"][Image]) == dict and ImageSetUseSpeak(Image):
            Visuel.itemconfigure("Perso",image=D_Data["Persos"][Image]["normal"][0])
            AnimationPersoVisuel(Image,0)
        elif type(D_Data["Persos"][Image]) == dict and not CheckSameImage(Image,"Perso"):
            Visuel.itemconfigure("Perso",image=D_Data["Persos"][Image]["normal"][0])
            AnimationPersoVisuel(Image,0)
        elif type(D_Data["Persos"][Image]) != dict:
            Visuel.itemconfigure("Perso",image=D_Data["Persos"][Image])
    else:
        Visuel.itemconfigure("Perso",image="")

def AnimationPersoVisuel(Image,Counter):
    """

    Animation Personnage

    """
    
    if GetVar("Current")[:2] in ["?_","§_"]:
        return
    
    if Image == D_Tableaux[GetVar("Current")]["PersoImg"] and not GetVar("IsUsingSpeak"):
        Duree = 50
        if Counter > len(D_Data["Persos"][Image]["normal"])-1:
            Counter = 0
            Duree = randint(2000,4000)
        Visuel.itemconfigure("Perso",image=D_Data["Persos"][Image]["normal"][Counter])
        ModifVar("CurrentImg",fenetre.after(Duree, lambda: AnimationPersoVisuel(Image,Counter+1)))


def SetFunction(Dic):
    """

    Crée le nombre voulu de boutons avec leurs commandes et leurs noms respectifs

    """

    if type(Dic) != dict:
        CrashReport("Erreur : "+str(Dic)+" n'est pas une chaine de caractères")

    Next1.pack_forget()
    Next2.pack_forget()
    Next3.pack_forget()
    Next4.pack_forget()



    for num in range(1,len(Dic)+1):
        if num <= 4:
            Numero = "Choix"+str(num)
            #eval("Next"+str(num)).pack(padx=10, pady=10)
            if len(Dic) == 1:
                #Visuel.create_window(200,500,height=500,width=400,window=eval("Next"+str(num)),tags="Buttons")
                #Visuel.tag_lower("Buttons")
                if type(Dic[Numero]) is not dict:
                    Visuel.tag_bind("Dialog_Box","<Button-1>",Visuel.tag_bind("Dialog_Box","<Button-1>",lambda arg=Numero : TableauSuivant(Dic[arg][1])))
                    Visuel.tag_bind("Dialog_Perso","<Button-1>",Visuel.tag_bind("Dialog_Perso","<Button-1>",lambda arg=Numero : TableauSuivant(Dic[arg][1])))
                    Visuel.tag_bind("Dialog","<Button-1>",Visuel.tag_bind("Dialog","<Button-1>",lambda arg=Numero : TableauSuivant(Dic[arg][1])))
                else:
                    if eval(Dic[Numero]["if"]):
                        Visuel.tag_bind("Dialog_Box","<Button-1>",Visuel.tag_bind("Dialog_Box","<Button-1>",lambda arg=Numero : TableauSuivant(Dic[arg]["do"][1])))
                        Visuel.tag_bind("Dialog_Perso","<Button-1>",Visuel.tag_bind("Dialog_Perso","<Button-1>",lambda arg=Numero : TableauSuivant(Dic[arg]["do"][1])))
                        Visuel.tag_bind("Dialog","<Button-1>",Visuel.tag_bind("Dialog","<Button-1>",lambda arg=Numero : TableauSuivant(Dic[arg]["do"][1])))
                    else:
                        Visuel.tag_bind("Dialog_Box","<Button-1>",Visuel.tag_bind("Dialog_Box","<Button-1>",lambda arg=Numero : TableauSuivant(Dic[arg]["else"][1])))
                        Visuel.tag_bind("Dialog_Perso","<Button-1>",Visuel.tag_bind("Dialog_Perso","<Button-1>",lambda arg=Numero : TableauSuivant(Dic[arg]["else"][1])))
                        Visuel.tag_bind("Dialog","<Button-1>",Visuel.tag_bind("Dialog","<Button-1>",lambda arg=Numero : TableauSuivant(Dic[arg]["else"][1])))
            else:
                Visuel.itemconfigure("Choice_Img_Filter",state="normal")
                Visuel.tag_raise("Buttons")
                Visuel.create_window(200,10+50*num,window=eval("Next"+str(num)),tags="Buttons")
            if type(Dic[Numero]) is not dict:
                eval("Next"+str(num)).configure(text=Dic[Numero][0])
                eval("Next"+str(num)).configure(command= lambda arg=Numero : TableauSuivant(Dic[arg][1]))
            else:
                if eval(Dic[Numero]["if"]):
                    eval("Next"+str(num)).configure(text=Dic[Numero]["do"][0])
                    eval("Next"+str(num)).configure(command= lambda arg=Numero: TableauSuivant(Dic[arg]["do"][1]))
                else:
                    eval("Next"+str(num)).configure(text=Dic[Numero]["else"][0])
                    eval("Next"+str(num)).configure(command= lambda arg=Numero: TableauSuivant(Dic[arg]["else"][1]))


def Sauvegarde(file):
    """

    Sauvegarde les valeurs dans un fichier .sav

    """
    if file == "settings.sav":
        with open(file, 'w',encoding="utf8") as configfile:
            New = {}
            New["TWESpeed"] = Dic_Variables["TWESpeed"]
            New["MusicVolume"] = Dic_Variables["MusicVolume"]
            New["VoiceVolume"] = Dic_Variables["VoiceVolume"]
            New["SEVolume"] = Dic_Variables["SEVolume"]
            configfile.write(str(New))
            return

    if GetVar("Current")[0:2] != "!_" and GetVar("Current")[0:2] != "?_" and GetVar("Current")[0:2] != "§_":
        with open(file, 'w',encoding="utf8") as configfile:
            New = {}
            for item in Dic_Variables:
                if Dic_Variables[item]["save"]:
                    New[item] = Dic_Variables[item]
            configfile.write(str(New))

        CreateSystemMessage("Sauvegarde !","green")
    else:
        CreateSystemMessage("Impossible","red")


def Sort(L):
    """

    Tri les nombres par ordre croissant

    """
    New = []
    for i in range(1,len(L)+1):
        for item in L:
            if int(item.split(".")[0]) == i:
                New.append(item)
    return New

def Chargement(file):
    """

    Charge les valeurs
    Recrée le tableau présent lors de la sauvegarde

    """
    global Dic_Variables
    if file == "settings.sav":
        if not os.path.exists(file):
            return
        with open(file, 'r',encoding="utf8") as configfile:
            Dic_Charge = eval(configfile.read())
        for n_key in Dic_Charge.keys():
            Dic_Variables[n_key] = Dic_Charge[n_key]
        return

    if os.path.exists(file) and (GetVar("Current")[0:2] != "!_" and GetVar("Current")[0:2] != "?_"):
        with open(file, 'r',encoding="utf8") as configfile:
            Dic_Charge = eval(configfile.read())
        for n_key in Dic_Charge.keys():
            Dic_Variables[n_key] = Dic_Charge[n_key]
        CreateSystemMessage("Chargement !","green")
        TableauSuivant(GetVar("Current"))
    else:
        CreateSystemMessage("Echec","red")





def TableauSuivant(Id):
    """

    Charge le prochain tableau

    """
    if not Id in D_Tableaux.keys():
        CrashReport("Erreur : "+Id+" n'est pas un tableau répertorié")

    ModifVar("Skiped",False)
    ModifVar("Current",Id)
    ModifVar("TableauId",randint(-10**9,10**9)+GetVar("TableauId"))
    DeleteGUI("reaction")
    SetTitre("",GetVar("TableauId"),"__")
    Visuel.itemconfigure("Choice_Img_Filter",state="hidden")

    Visuel.tag_unbind("Dialog_Box","<Button-1>")
    Visuel.tag_unbind("Dialog_Perso","<Button-1>")
    Visuel.tag_unbind("Dialog","<Button-1>")
    Visuel.tag_unbind("Decor","<Button-1>")
    Visuel.tag_unbind("Perso","<Button-1>")
    Visuel.delete("Buttons")


    if Id[0:2] == "§_": # Titre déroulant
        SetVoix(None)
        SetDecor(None)
        SetPersoVisuel(None)
        SetPerso("","black")
        Visuel.itemconfigure("Dialog",text="")
        SetFunction({})
        SetMusic(D_Tableaux[Id]["Mus"])
        SetScrollingTitre(D_Tableaux[Id]["Text"],GetVar("TableauId"),D_Tableaux[Id]["Suite"])
    elif Id[0:2] == "!_": # Choix Moteur
        Choix = D_Tableaux[Id]["DRecours"]
        for eva in D_Tableaux[Id]["Evals"]:
            if eval(eva[0]) and Choix == D_Tableaux[Id]["DRecours"]:
                Choix = eva[1]
        TableauSuivant(Choix)
    elif Id[0:2] == "?_": # Titre
        SetVoix(None)
        SetDecor(None)
        SetPersoVisuel(None)
        SetPerso("","black")
        Visuel.itemconfigure("Dialog",text="")
        SetFunction({})
        SetMusic(D_Tableaux[Id]["Mus"])
        SetTitre(D_Tableaux[Id]["Titre"],GetVar("TableauId"),Id)
    else: #Tableau
        if D_Tableaux[Id]["CustomPlacement"] != None:
            MovePersoImg(D_Tableaux[Id]["CustomPlacement"][0],D_Tableaux[Id]["CustomPlacement"][1])
        else:
            MovePersoImg(int(Visuel['width'])/2,150)
        SetVoix(D_Tableaux[Id]["Voix"])
        SetDecor(D_Tableaux[Id]["Decor"])
        if not D_Tableaux[Id]["PersoImg"] == None:
            if type(D_Data["Persos"][D_Tableaux[Id]["PersoImg"]]) == dict:
                if not ImageSetUseSpeak(D_Tableaux[Id]["PersoImg"]):
                    SetPersoVisuel(D_Tableaux[Id]["PersoImg"])
                else:
                    ModifVar("IsUsingSpeak",True)
            else:
                SetPersoVisuel(D_Tableaux[Id]["PersoImg"])
        else:
            SetPersoVisuel(D_Tableaux[Id]["PersoImg"])
        SetMusic(D_Tableaux[Id]["Mus"])
        SetPerso(D_Tableaux[Id]["Perso"],D_Tableaux[Id]["PersoCouleur"])
        SetDialogue(D_Tableaux[Id]["Dialogue"],GetVar("TableauId"))
        Visuel.tag_bind("Dialog_Box","<Button-1>",Visuel.tag_bind("Dialog_Box","<Button-1>",lambda arg=0 : SkipText()))
        Visuel.tag_bind("Dialog_Perso","<Button-1>",Visuel.tag_bind("Dialog_Perso","<Button-1>",lambda arg=0 : SkipText()))
        Visuel.tag_bind("Dialog","<Button-1>",Visuel.tag_bind("Dialog","<Button-1>",lambda arg=0 : SkipText()))
        #SetFunction(D_Tableaux[Id]["Choix"])
        for Action in D_Tableaux[Id]["Extra"]:
            eval(Action)
    Visuel.update()

def BuiltInSettingsMenu():
    """

    Menu de paramètre préconcu pour les paramètres moteur

    """
    Settings = Tk()
    Settings.title("Parametres")

    TWE_Set = Scale(Settings, orient='horizontal', from_=25, to=150,
      resolution=1, tickinterval=25, length=350,
      label="Vitesse d'écriture <-",command=lambda value, name="TWESpeed":ModifVar(name,int(value)))
    TWE_Set.set(GetVar("TWESpeed"))
    TWE_Set.pack()

    Voix_Set = Scale(Settings, orient='horizontal', from_=0, to=1,
      resolution=0.05, tickinterval=0.5, length=350,
      label="Volume des voix ->",command=lambda value, name="VoiceVolume":ModifVar(name,float(value)))
    Voix_Set.set(GetVar("VoiceVolume"))
    Voix_Set.pack()

    BGM_Set = Scale(Settings, orient='horizontal', from_=0, to=1,
      resolution=0.05, tickinterval=0.5, length=350,
      label="Volume des musiques ->",command=lambda value, name="MusicVolume":ModifVar(name,float(value)))
    BGM_Set.set(GetVar("MusicVolume"))
    BGM_Set.pack()

    SE_Set = Scale(Settings, orient='horizontal', from_=0, to=1,
      resolution=0.05, tickinterval=0.5, length=350,
      label="Volume des effets sonores ->",command=lambda value, name="SEVolume":ModifVar(name,float(value)))
    SE_Set.set(GetVar("SEVolume"))
    SE_Set.pack()

def BuiltInHelpMenu():
    Help = Tk()
    Help.title("A propos")
    label = Label(Help,wraplength=350,text="Jeu : "+GameInfo["Nom"]+
                  "\n\nAuteur : "+GameInfo["Auteur"]+
                  "\n\nVersion : "+GameInfo["Version"]+
                  "\n\nMoteur : "+Engine_Version+
                  "\n\n\n"+GameInfo["Desc"])
    label.pack()

def Apparition():
    """

    Apparition des widgets visuels

    """
    Visuel.pack(padx=5,pady=5)

    Visuel.create_rectangle(0,0,400,300,fill="black",tags="Background")

    Visuel.create_image(int(Visuel['width'])/2,150,image="",tags="Decor")
    Visuel.create_image(int(Visuel['width'])/2,150,image="",tags="Perso")

    Visuel.create_rectangle(0, 0, 400, 300, fill="grey", stipple="gray50",state="hidden", tags="Choice_Img_Filter")

    Visuel.create_text(int(Visuel['width'])/2,150,fill="white",text="",tags="Text")
    Visuel.create_text(int(Visuel['width'])/2,400,fill="white",text="",tags="ScrollText",justif="left",width=380)

    Visuel.create_rectangle(2,300,399,532,fill="lightgray",tags="Dialog_Box")

    Visuel.create_text(int(Visuel['width'])/2,310,text="",width=300,tags="Dialog_Perso")
    Visuel.create_text(int(Visuel['width'])/2,340,text="",width=380,tags="Dialog",justif="left",anchor="n")


    Visuel.create_image(18,516,image=D_Data["Icons"]["save"],tags="Save_Button")
    Visuel.create_image(50,516,image=D_Data["Icons"]["load"],tags="Load_Button")
    Visuel.create_image(82,516,image=D_Data["Icons"]["options"],tags="Settings_Button")
    Visuel.create_image(114,516,image=D_Data["Icons"]["help"],tags="Help_Button")
    Visuel.tag_bind("Save_Button","<Button-1>",lambda arg=0:Sauvegarde("save.sav"))
    Visuel.tag_bind("Load_Button","<Button-1>",lambda arg=0:Chargement("save.sav"))
    Visuel.tag_bind("Settings_Button","<Button-1>",lambda arg=0:BuiltInSettingsMenu())
    Visuel.tag_bind("Help_Button","<Button-1>",lambda arg=0:BuiltInHelpMenu())


def Init_UpdateBar(total,current,can):
    """
       
    Mise à jour de la barre de chargement Init
      
    """
    can.delete("progress")
    can.create_rectangle(10,130,(390*current)/total,170,fill="green",tags="progress")
    can.update()
    
def Init_GetTotal():
    """
       
    Obtention du nombre total d'opération à effectuer
      
    """
    if not os.path.exists("Data"):
        CrashReport("Erreur : Dossier Data manquant")
    if not os.path.exists("Data\\Tableaux"):
        CrashReport("Erreur : Dossier Tableaux manquant")
    if not os.path.exists("Data\\BGM"):
        CrashReport("Erreur : Dossier BGM manquant")
    if not os.path.exists("Data\\SE"):
        CrashReport("Erreur : Dossier SE manquant")
    if not os.path.exists("Data\\Voix"):
        CrashReport("Erreur : Dossier Voix manquant")
    if not os.path.exists("Data\\Decors"):
        CrashReport("Erreur : Dossier Decors manquant")
    if not os.path.exists("Data\\Persos"):
        CrashReport("Erreur : Dossier Persos manquant")
    if not os.path.exists("Data\\Variables.txt"):
        CrashReport("Erreur : Fichier Variables manquant")    
    if not os.path.exists("Data\\Icons.zip"):
        CrashReport("Erreur : Fichier Icons manquant")   
    if not os.path.exists("Data\\Game_Info.txt"):
        CrashReport("Erreur : Fichier Game_Info manquant")            
    
    nb = 3
    for file in os.listdir("Data\Tableaux"):
        nb+=1
     
    if pygame.mixer.get_init() != None:
        for file in os.listdir("Data\BGM"):
            nb+=1
        for file in os.listdir("Data\SE"):
            nb+=1
        for file in os.listdir("Data\Voix"):
            nb+=1
           
    for file in os.listdir("Data\Decors"):
        nb+=1
        
    for file in os.listdir("Data\Persos"):
        nb+=1
        
    return nb
    
def Init_UpdateText(status,current,can):
    """
       
    Mise à jour du texte informatif
      
    """
    can.itemconfigure("status",text=status)
    can.itemconfigure("current",text=current)
    can.update()

def Init():
    """

    Initialisation du moteur et synchronisation avec le fichier Data

    """
    global D_Tableaux,Dic_Variables,D_Data,GameInfo
    print("Version du Moteur : "+Engine_Version)
    
    total = Init_GetTotal()
    curr = 0

    canvas = Canvas(fenetre,width=400,height=300)
    canvas.pack(padx=5,pady=5)
    canvas.create_text(200,110,text="",tags="status")
    canvas.create_text(200,190,text="",tags="current")

    for file in os.listdir("Data\Tableaux"):
        curr+=1
        Init_UpdateBar(total,curr,canvas)
        Init_UpdateText("Chargement des tableaux",file,canvas)
        if file.split(".")[1] == "txt":
            with open("Data\\Tableaux\\"+file,encoding="utf8") as jsonp_file:
                jsonp_str = jsonp_file.read()
                Dico_Full = eval(jsonp_str)
            D_Tableaux.update(Dico_Full)
            
    if pygame.mixer.get_init() != None:
        for file in os.listdir("Data\BGM"):
            curr+=1
            Init_UpdateBar(total,curr,canvas)
            Init_UpdateText("Chargement des musiques",file,canvas)
            key = file.split(".")[0]
            if file.split(".")[1] == "ogg":
                D_Data["BGM"][key] = pygame.mixer.Sound("Data\\BGM\\"+file)

        for file in os.listdir("Data\SE"):
            curr+=1
            Init_UpdateBar(total,curr,canvas)
            Init_UpdateText("Chargement des effets sonores",file,canvas)
            key = file.split(".")[0]
            if file.split(".")[1] == "wav":
                D_Data["SE"][key] = pygame.mixer.Sound("Data\\SE\\"+file)

        for file in os.listdir("Data\Voix"):
            curr+=1
            Init_UpdateBar(total,curr,canvas)
            Init_UpdateText("Chargement des voix",file,canvas)
            key = file.split(".")[0]
            if file.split(".")[1] == "wav":
                D_Data["Voix"][key] = pygame.mixer.Sound("Data\\Voix\\"+file)

    for file in os.listdir("Data\Decors"):
        curr+=1
        Init_UpdateBar(total,curr,canvas)
        Init_UpdateText("Chargement des décors",file,canvas)
        key = file.split(".")[0]
        if file.split(".")[1] == "png":
            D_Data["Decor"][key] = PhotoImage(file="Data\\Decors\\"+file)
        elif file.split(".")[1] == "zip":
            D_Data["Decor"][key] = []
            with zipfile.ZipFile("Data\\Decors\\"+file) as myzip:
                L = Sort(myzip.namelist())
                myzip.extractall("Data\\Zip")
                for item in L:
                    D_Data["Decor"][key].append(PhotoImage(file="Data\\Zip\\"+item))
                    os.remove("Data\\Zip\\"+item)

    for file in os.listdir("Data\Persos"):
        curr+=1
        Init_UpdateBar(total,curr,canvas)
        Init_UpdateText("Chargement des personnages",file,canvas)
        key = file.split(".")[0]
        if file.split(".")[1] == "png":
            D_Data["Persos"][key] = PhotoImage(file="Data\\Persos\\"+file)
        elif file.split(".")[1] == "zip":
            D_Data["Persos"][key] = {}
            D_Data["Persos"][key]["normal"] = []
            with zipfile.ZipFile("Data\\Persos\\"+file) as myzip:
                L = myzip.namelist()
                myzip.extractall("Data\\Zip")
                if "speak.png" in L:
                    L.remove("speak.png")
                    D_Data["Persos"][key]["speak"] = PhotoImage(file="Data\\Zip\\speak.png")
                    os.remove("Data\\Zip\\speak.png")
                L = Sort(L)
                for item in L:
                    D_Data["Persos"][key]["normal"].append(PhotoImage(file="Data\\Zip\\"+item))
                    os.remove("Data\\Zip\\"+item)
                    

    curr+=1
    Init_UpdateBar(total,curr,canvas)
    Init_UpdateText("Chargement des variables","Variables.txt",canvas)
    with open("Data\\Variables.txt",encoding="utf8") as jsonp_file:
        jsonp_str = jsonp_file.read()
        New = eval(jsonp_str)
        for item in New.keys():
            if not item in Dic_Variables.keys():
                Dic_Variables[item] = New[item]
                
                
    curr+=1
    Init_UpdateBar(total,curr,canvas)
    Init_UpdateText("Chargement des informations du jeu","Game_Info.txt",canvas)
    with open("Data\\Game_Info.txt",encoding="utf8") as jsonp_file:
        file = eval(jsonp_file.read())
        check = file["Nom"]
        check = file["Version"]
        check = file["Auteur"]
        check = file["Desc"]
        GameInfo = file

    curr+=1
    Init_UpdateBar(total,curr,canvas)
    Init_UpdateText("Chargement des icônes","Icons.zip",canvas)
    with zipfile.ZipFile("Data\\Icons.zip") as myzip:
        L = myzip.namelist()
        myzip.extractall("Data\\Zip")

        for item in L:
            D_Data["Icons"][item.split(".")[0]] = PhotoImage(file="Data\\Zip\\"+item)
            os.remove("Data\\Zip\\"+item)

    os.rmdir("Data\\Zip")
    canvas.pack_forget()
    Chargement("settings.sav")



from Functions import *


#------------------- Fin Moteur --------------------
