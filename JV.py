#Joute Verbal par Julien

from tkinter import *
from Engine import *

diff = 3
bg = []
curr = 0
frame = 0

phrases = [
    "Je suis le plus grand PDG !",
    "J'ai un parc et plein de blé !",
    "Je suis le plus beau,",
    "et j'ai un paquebot !",
    "T'as aucune chance contre moi,",
    "y'a des braquages tout les mois !", #5

    "Ah Ah Ah !",
    "Je suis le plus grand PDG !",
    "Regarde tout mon blé !",
    "J'ai aussi plein d'otages,",
    "le Marchand et le mage !",
    "Personne ne m'en veux,",
    "Car je fais ce que je veux !", #12


    "Ah Ah Ah !",
    "Je suis le plus grand PDG !",
    "Sérieux regarde mon blé !",
    "Maison hantée,",
    "vol armée,",
    "je suis le roi des coups fourrés !",
    "Alors moi j'vais t'manger !", #19
    ]

repliques = {
    "5":[
        "De votre caisse ?",
        "C'est nul !",
        "Au secours !",
        "C'est moi le PDG !",
        "Je peux partir ?",
        "1"
        ],
    "12":[
        "Je me rend.",
        "C'est atroce.",
        "Waldo vous déteste.",
        "WaldoLand c'était mieux...",
        "Je vais appeler les pompiers.",
        "3"
        ],
    "19":[
        "Par pitié....",
        "C'est moi qui vous mange !",
        "Je vais mourir...",
        "Mes oreilles saignent...",
        "Argh !",
        "2"
        ],
    }
    
def MiniGame_JV():
    global diff,bg,curr,frame,repliques,phrases

    diff = GetVar("difficulte")
    curr = 0
    frame = 0

    DisableWindow()

    root = Tk()
    root.title("Mini Jeu")
    
    def QuitMinigame():
        root.destroy()
        EnableWindow()
        Chargement("save.sav")
    
    root.protocol("WM_DELETE_WINDOW", QuitMinigame)


    bg = [
        PhotoImage(master=root,file="Data/Autres/JV/bg1.png"),
        PhotoImage(master=root,file="Data/Autres/JV/bg2.png")
        ]

    can = Canvas(root,width=400,height=300)
    can.pack()
    can.create_image(200,150,image="",tags="bg")
    can.create_rectangle(100,180,300,220,fill="gray")
    can.create_text(200,200,text="",tags="lyric")

    can.create_rectangle(50,20,350,40,fill="gray",tags="t1")
    can.create_text(200,30,text="",tags=("t1","txt1"))
    can.create_rectangle(50,42,350,62,fill="gray",tags="t2")
    can.create_text(200,52,text="",tags=("t2","txt2"))
    can.create_rectangle(50,64,350,84,fill="gray",tags="t3")
    can.create_text(200,74,text="",tags=("t3","txt3"))
    can.create_rectangle(50,86,350,106,fill="gray",tags="t4")
    can.create_text(200,96,text="",tags=("t4","txt4"))
    can.create_rectangle(50,108,350,128,fill="gray",tags="t5")
    can.create_text(200,118,text="",tags=("t5","txt5"))
                
    def GetTagsFromId(t):
        t = list(t)
        for i in range(len(t)):
            t[i] = can.gettags(t[i])[0]
        return t

    def Click(event):
        global repliques,phrases,curr
        t = GetTagsFromId(can.find_overlapping(event.x, event.y,event.x+1,event.y+1))
        for c in t:
            if c in ["t1","t2","t3","t4","t5"]:
                if c[1] == repliques[str(curr)][5]:
                    if curr != 19:
                        curr+=1
                        NextLyric()
                    else:
                        TableauSuivant("RickeyLandPalais_RickeyPartC_20")
                        root.destroy()
                        EnableWindow()
                else:
                    curr = 0
                    NextLyric()
                return
                

    def NextLyric():
        global phrases,curr,bg,frame

        can.itemconfigure("bg",image=bg[frame])
        frame+=1
        if frame == len(bg):
            frame=0

        can.itemconfigure("t1",state="hidden")
        can.itemconfigure("t2",state="hidden")
        can.itemconfigure("t3",state="hidden")
        can.itemconfigure("t4",state="hidden")
        can.itemconfigure("t5",state="hidden")

        can.itemconfigure("lyric",text=phrases[curr])

        if not curr in [5,12,19]:
            curr+=1
            root.after(2000,NextLyric)
        else:
            can.itemconfigure("t1",state="normal")
            can.itemconfigure("t2",state="normal")
            can.itemconfigure("t3",state="normal")
            can.itemconfigure("txt1",text=repliques[str(curr)][0])
            can.itemconfigure("txt2",text=repliques[str(curr)][1])
            can.itemconfigure("txt3",text=repliques[str(curr)][2])
            if diff>=2:
                can.itemconfigure("t4",state="normal")
                can.itemconfigure("txt4",text=repliques[str(curr)][3])
            if diff>=3:
                can.itemconfigure("t5",state="normal")
                can.itemconfigure("txt5",text=repliques[str(curr)][4])


    can.bind("<Button-1>",Click)
    NextLyric()


    root.mainloop()
