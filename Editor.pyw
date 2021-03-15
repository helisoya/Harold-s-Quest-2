from tkinter import *
from tkinter import colorchooser
import configparser
import json
import os






root = Tk()
root.title("Editeur")
frame_setter = Frame(root)
frame_setter.pack()
root.protocol("WM_DELETE_WINDOW", exit)



Text_Nom = Label(frame_setter,text="Nom du Tableau") #Nom
Text_Nom.pack()
Entry_Nom = Entry(frame_setter)
Entry_Nom.pack()

Text_Music = Label(frame_setter,text="Musique") #Musique
Text_Music.pack(pady=2)
Entry_Music = Entry(frame_setter)
Entry_Music.pack()

Text_Extra = Label(frame_setter,text="Extra") #Extra
Text_Extra.pack(pady=2)
Entry_Extra = Entry(frame_setter)
Entry_Extra.pack()

Text_Voix = Label(frame_setter,text="Voix") # Voix
Text_Voix.pack(pady=2)
Entry_Voix = Entry(frame_setter)
Entry_Voix.pack()

Text_Image = Label(frame_setter,text="Decor") # Decor
Text_Image.pack(pady=2)
Entry_Image = Entry(frame_setter)
Entry_Image.pack()

Text_PersoImg = Label(frame_setter,text="Image du Perso") # Image du Personage
Text_PersoImg.pack(pady=2)
Entry_PersoImg = Entry(frame_setter)
Entry_PersoImg.pack()


Text_NamePerso = Label(frame_setter,text="Nom Du Perso") #Nom Perso
Text_NamePerso.pack(pady=2)
Entry_NamePerso = Entry(frame_setter)
Entry_NamePerso.pack()

Text_Place = Label(frame_setter,text="Placement (Optionel)") #Place Perso
Text_Place.pack(pady=2)
Entry_Place = Entry(frame_setter)
Entry_Place.pack()

Couleur_Perso = "#000000" # Couleur Perso

def GetColor():
    global Couleur_Perso
    Couleur_Perso = colorchooser.askcolor()[1]
    Button_CouleurPerso.configure(fg=Couleur_Perso)
    
Button_CouleurPerso = Button(frame_setter,fg=Couleur_Perso,text="Couleur Du Perso",command=GetColor)
Button_CouleurPerso.pack()


Text_Dialog = Label(frame_setter,text="Dialogue") #Dialogue
Text_Dialog.pack(pady=2)

Entry_Dialog = Text(frame_setter,height = 10,width=50)
Entry_Dialog.pack()


Frame_1 = Frame(frame_setter)
Frame_2 = Frame(frame_setter)
Frame_3 = Frame(frame_setter)
Frame_4 = Frame(frame_setter)

IfText_1 = Label(Frame_1,text="Si")
DoNameText_1 = Label(Frame_1,text="Alors - Nom")
DoToText_1 = Label(Frame_1,text="Alors - Cible")
ElseNameText_1 = Label(Frame_1,text="Sinon - Nom")
ElseToText_1 = Label(Frame_1,text="Sinon - Cible")


IfText_2 = Label(Frame_2,text="Si")
DoNameText_2 = Label(Frame_2,text="Alors - Nom")
DoToText_2 = Label(Frame_2,text="Alors - Cible")
ElseNameText_2 = Label(Frame_2,text="Sinon - Nom")
ElseToText_2 = Label(Frame_2,text="Sinon - Cible")


IfText_3 = Label(Frame_3,text="Si")
DoNameText_3 = Label(Frame_3,text="Alors - Nom")
DoToText_3 = Label(Frame_3,text="Alors - Cible")
ElseNameText_3 = Label(Frame_3,text="Sinon - Nom")
ElseToText_3 = Label(Frame_3,text="Sinon - Cible")


IfText_4 = Label(Frame_4,text="Si")
DoNameText_4 = Label(Frame_4,text="Alors - Nom")
DoToText_4 = Label(Frame_4,text="Alors - Cible")
ElseNameText_4 = Label(Frame_4,text="Sinon - Nom")
ElseToText_4 = Label(Frame_4,text="Sinon - Cible")

                   
Text_1 = Label(Frame_1,text="Choix 1")     # Choix
If_1 = Entry(Frame_1)
DoName_1 = Entry(Frame_1)
DoTo_1 = Entry(Frame_1)
ElseName_1 = Entry(Frame_1)
ElseTo_1 = Entry(Frame_1)

Text_1.pack(pady=4)
IfText_1.pack()
If_1.pack()
DoNameText_1.pack()
DoName_1.pack()
DoToText_1.pack()
DoTo_1.pack()
ElseNameText_1.pack()
ElseName_1.pack()
ElseToText_1.pack()
ElseTo_1.pack()


Text_2 = Label(Frame_2,text="Choix 2")     
If_2 = Entry(Frame_2)
DoName_2 = Entry(Frame_2)
DoTo_2 = Entry(Frame_2)
ElseName_2 = Entry(Frame_2)
ElseTo_2 = Entry(Frame_2)
Text_2.pack(pady=4)
IfText_2.pack()
If_2.pack()
DoNameText_2.pack()
DoName_2.pack()
DoToText_2.pack()
DoTo_2.pack()
ElseNameText_2.pack()
ElseName_2.pack()
ElseToText_2.pack()
ElseTo_2.pack()
               
Text_3 = Label(Frame_3,text="Choix 3")     
If_3 = Entry(Frame_3)
DoName_3 = Entry(Frame_3)
DoTo_3 = Entry(Frame_3)
ElseName_3 = Entry(Frame_3)
ElseTo_3 = Entry(Frame_3)
Text_3.pack(pady=4)
IfText_3.pack()
If_3.pack()
DoNameText_3.pack()
DoName_3.pack()
DoToText_3.pack()
DoTo_3.pack()
ElseNameText_3.pack()
ElseName_3.pack()
ElseToText_3.pack()
ElseTo_3.pack()

Text_4 = Label(Frame_4,text="Choix 4")     
If_4 = Entry(Frame_4)
DoName_4 = Entry(Frame_4)
DoTo_4 = Entry(Frame_4)
ElseName_4 = Entry(Frame_4)
ElseTo_4 = Entry(Frame_4)
Text_4.pack(pady=4)
IfText_4.pack()
If_4.pack()
DoNameText_4.pack()
DoName_4.pack()
DoToText_4.pack()
DoTo_4.pack()
ElseNameText_4.pack()
ElseName_4.pack()
ElseToText_4.pack()
ElseTo_4.pack()
               

root_preview = Tk()
root_preview.title("Apercu")

def ClosePreview():
    root_preview.withdraw()

root_preview.protocol("WM_DELETE_WINDOW", ClosePreview)
ImageBg = PhotoImage(master=root_preview,file="")
ImagePerso = PhotoImage(master=root_preview,file="")

Preview_Visuel = Canvas(root_preview,height=300,width=400)
Preview_Visuel.create_image(int(Preview_Visuel['width'])/2,int(Preview_Visuel['height'])/2,image=ImageBg,tags="Decor")
Preview_Visuel.create_image(int(Preview_Visuel['width'])/2,int(Preview_Visuel['height'])/2,image=ImagePerso,tags="Perso")
Preview_Visuel.pack(pady=5)
Preview_Perso = Label(root_preview,text="",fg=Couleur_Perso,wraplength=350)
Preview_Perso.pack(pady=5)
Preview_Dialog = Label(root_preview,text="",wraplength=350)
Preview_Dialog.pack(pady=5)
    

Button_1 = Button(root_preview,text="",wraplength=350)
Button_2 = Button(root_preview,text="",wraplength=350)
Button_3 = Button(root_preview,text="",wraplength=350)
Button_4 = Button(root_preview,text="",wraplength=350)

root_preview.withdraw()

root_rendu = Tk()
root_rendu.title("Rendu")

def CloseRendu():
    root_rendu.withdraw()

root_rendu.protocol("WM_DELETE_WINDOW", CloseRendu)
Rendu = Text(root_rendu)
Rendu.pack(pady=5)
root_rendu.withdraw()




def GetCurrentChoice():
    Frame_1.pack_forget()
    Frame_2.pack_forget()
    Frame_3.pack_forget()
    Frame_4.pack_forget()
    Nb = int(SpinBox_Choice.get())
    for i in range(1,Nb+1):
        eval("Frame_"+str(i)).pack(side="left")

SpinBox_Choice = Spinbox(frame_setter, from_=0, to=4,command=GetCurrentChoice) #Nb Choix
SpinBox_Choice.pack()


def Update():
    root_preview.deiconify()
    File = ""
    if Entry_Place.get() != "":
        Preview_Visuel.coords("Perso",eval(Perso,Entry_Place.get()))
    else:
        Preview_Visuel.coords("Perso",int(Preview_Visuel['width'])/2,int(Preview_Visuel['height']))
    if str(Entry_Image.get())+".png" in os.listdir("Data\Decors"):
        File = "Data\\Decors\\"+str(Entry_Image.get())+".png"
    print(File)
    ImageBg.configure(file=File)
    Preview_Visuel.itemconfigure("Decor",image=ImageBg)
    if str(Entry_PersoImg.get())+".png" in os.listdir("Data\Persos"):
        File = "Data\\Persos\\"+str(Entry_PersoImg.get())+".png"
    ImagePerso.configure(file=File)
    
    Preview_Perso.configure(text=str(Entry_NamePerso.get()),fg=Couleur_Perso)
    Preview_Dialog.configure(text=str(Entry_Dialog.get("1.0", "end-1c")))
    Nb = int(SpinBox_Choice.get())
    Button_1.pack_forget()
    Button_2.pack_forget()
    Button_3.pack_forget()
    Button_4.pack_forget()
    for i in range(1,Nb+1):
        eval("Button_"+str(i)).pack(pady=5)
        eval("Button_"+str(i)).configure(text=eval("DoName_"+str(i)).get())
    root_preview.update()
    root_preview.mainloop()

def Generate():
    root_rendu.deiconify()
    Rendu.delete(1.0,"end")

    Voix = "None"
    if str(Entry_Voix.get()) != "":
       Voix = '"'+str(Entry_Voix.get())+'"'
    Decor = "None"
    if str(Entry_Image.get()) != "":
       Decor = '"'+str(Entry_Image.get())+'"'
    Mus = "None"
    if str(Entry_Music.get()) != "":
       Decor = '"'+str(Entry_Music.get())+'"'
    PersoImg = "None"
    if str(Entry_PersoImg.get()) != "":
        PersoImg = '"'+str(Entry_PersoImg.get())+'"'

    Place = "None"
    if str(Entry_Place.get()) != "":
        Place = str(Entry_Place.get())


    Rendu.insert("end",'"'+str(Entry_Nom.get())+'": {'+
                 '\n    "Voix":'+Voix+','+
                 '\n    "Decor":'+Decor+','+
                 '\n    "PersoImg":'+PersoImg+','+
                 '\n    "CustomPlacement":'+Place+','+
                 '\n    "Mus":'+Mus+','+
                 '\n    "Perso":"'+str(Entry_NamePerso.get())+'",'+
                 '\n    "PersoCouleur":"'+str(Couleur_Perso)+'",'+
                 '\n    "Dialogue":"'+str(Entry_Dialog.get("1.0", "end-1c"))+'",'+
                 '\n    "Choix":{')
    for i in range(1,int(SpinBox_Choice.get())+1):
        if eval("If_"+str(i)).get() != "":
            Rendu.insert("end",'\n        "Choix'+str(i)+'":{'+
                        '\n            "if":"'+str(eval("If_"+str(i)).get())+'",'+
                         '\n            "do":("'+str(eval("DoName_"+str(i)).get())+'","'+str(eval("DoTo_"+str(i)).get())+'"),'+
                         '\n            "else":("'+str(eval("ElseName_"+str(i)).get())+'","'+str(eval("ElseTo_"+str(i)).get())+'")},')
        else:
            Rendu.insert("end",'\n        "Choix'+str(i)+'":("'+str(eval("DoName_"+str(i)).get())+'","'+str(eval("DoTo_"+str(i)).get())+'"),')
    Rendu.insert("end",'\n    },')
    Rendu.insert("end",'\n    "Extra":['+str(Entry_Extra.get())+'],'+
                 '\n},')

def ChoixMoteur():
    CM = Tk()
    CM_Entry = Text(CM)
    CM_Entry.pack()
    CM_Entry.insert("end",'"!_???": {'+
                 '\n    "DRecours":"???",'+
                 '\n    "Evals":['+
                 '\n        ("EVAL","CIBLE"),'+
                 '\n    ],'+
                 '\n},')

def Titre():
    T = Tk()
    T_Entry = Text(T)
    T_Entry.pack()
    T_Entry.insert("end",'"?_NOM": {'+
                 '\n    "Titre":"???",'+
                 '\n    "Suite":"???",'+
                 '\n    "Mus":"???",'+
                 '\n},')

def Defilant():
    T = Tk()
    T_Entry = Text(T)
    T_Entry.pack()
    T_Entry.insert("end",'"§_???": {'+
                 '\n    "Text":"???",'+
                 '\n    "Suite":"???",'+
                 '\n    "Mus":"???",'+
                 '\n},')

menuBar = Menu(root)
root['menu'] = menuBar
menuBar.add_command(label='Apercu', command=Update)
menuBar.add_command(label='Generer', command=Generate)
menuBar.add_command(label='Choix Moteur', command=ChoixMoteur)
menuBar.add_command(label='Titre', command=Titre)
menuBar.add_command(label='Defilant', command=Defilant)

root.mainloop()
