# Quiz de Waldo par Julien et Corentin

from tkinter import*
from random import *


Questions = {
    "Q1":{
        "question":"Qui est le PDG du Parc ?",
        "1":"Rickey",
        "2":"Waldo",
        "3":"Harold",
        "good":"1",
    },
     "Q2":{
        "question":"Qui présente le quiz ?",
        "1":"Rickey",
        "2":"Harold",
        "3":"Waldo",
        "good":"3",
    },
     "Q3":{
        "question":"Combien d'attractions devez-vous réussir ?",
        "1":"4",
        "2":"10",
        "3":"5",
        "good":"1",
    },
     "Q4":{
        "question":"Combien d'employés y a-t-il au parc ?",
        "1":"10",
        "2":"1",
        "3":"100",
        "good":"2",
    },
     "Q5":{
        "question":"Qu'offre Rickey au premier qui réussit toute les attractions ?",
        "1":"Une baffe",
        "2":"Un tank",
        "3":"Un livre",
        "good":"3",
    },
     "Q6":{
        "question":"Qui assure la sécurité au parc ?",
        "1":"Les Gardes",
        "2":"Rickey",
        "3":"Le seigneur noir",
        "good":"1",
    },
     "Q7":{
        "question":"Quel couvre chef porte le PDG ?",
        "1":"Un coiffe d'officier",
        "2":"Un beret",
        "3":"Une perruque",
        "good":"1",
    },
     "Q8":{
        "question":"Comment s'appelait le dragon qui vivait au Nord ?",
        "1":"Mark Croc-Brisé",
        "2":"Dragono le Terrible",
        "3":"Seigneur Braise",
        "good":"3",
    },
     "Q9":{
        "question":"Quel est le lieu obligatoirement visité à Rickeyland ?",
        "1":"Le Palais du PDG",
        "2":"La boutique de souvenir",
        "3":"Le guichet",
        "good":"2",
    },
     "Q10":{
        "question":"Laquelle de ces attractions n'est pas à Rickeyland ?",
        "1":"Le Tir sur Marchand",
        "2":"Le Quiz de Rickey",
        "3":"La course de chevaux",
        "good":"2",
    },
     "Q11":{
        "question":"Ou est-ce que j'habite ?",
        "1":"Dans un placard",
        "2":"Dans la ville de Vlatyr",
        "3":"Dans les montagnes",
        "good":"1",
    },
     "Q12":{
        "question":"Qui sont les mieux payés au parc ?",
        "1":"Les employés",
        "2":"Les Gardes",
        "3":"Les serveurs",
        "good":"2",
    },
     "Q13":{
        "question":"Dans quelle région vivont nous ?",
        "1":"Marklicht",
        "2":" Aajotyr",
        "3":"Vlatyr",
        "good":"3",
    },
     "Q14":{
        "question":"Dans quel pays vivons-nous ?",
        "1":"Kosky",
        "2":"Kalia",
        "3":"Oremil",
        "good":"1",
    },
     "Q15":{
        "question":"Quelle est la capitale de Vlatyr ?",
        "1":"Vlatyr",
        "2":"Belios",
        "3":"Vorlan",
        "good":"1",
    },
     "Q16":{
        "question":"Quel est la capitale de notre pays ?",
        "1":"Luasyo",
        "2":"Aajotyr",
        "3":"Regiapolis",
        "good":"2",
    },
     "Q17":{
        "question":"Quel pays nous borde à l'Est ?",
        "1":"Marklicht",
        "2":"Kalia",
        "3":"Orkva",
        "good":"1",
    },
    "Q18":{
        "question":"Quel pays nous borde à l'Ouest ?",
        "1":"Lonas",
        "2":"Regia",
        "3":"Oremil",
        "good":"3",
    },
    "Q19":{
        "question":"Qui est interdit de venir au parc ?",
        "1":"Harold",
        "2":"Le Mage des montagnes",
        "3":"L'Archer",
        "good":"1",
    },
    "Q20":{
        "question":"Qui est le bras droit du PDG ?",
        "1":"Rickey",
        "2":"Le seigneur noir",
        "3":"Waldo",
        "good":"2",
    },


}

Curr = ""
diff = 3

available = []
for i in range(5*(diff-1)+1,5*(diff-1)+11):
    available.append("Q"+str(i))


fenetre=Tk()
fenetre.title("Mini Jeu")

def input(event):
    awnser = str(event.widget.gettags('current')[0])
    if Questions[Curr]["good"] == awnser:
        NextQuestion()
    else:
        fenetre.destroy()


waldo = PhotoImage(master=fenetre,file="Data/Autres/QW/waldo.png")

canvas = Canvas(fenetre, width=500, height=450, background='white')
canvas.create_image(250,150,image=waldo)
canvas.create_rectangle(100,300,240,350,fill="gray",tags="1")
canvas.create_rectangle(260,300,400,350,fill="gray",tags="2")
canvas.create_rectangle(185,360,325,410,fill="gray",tags="3")


canvas.create_rectangle(100,240,400,290,fill="gray")
canvas.create_text(250,265,text="Question",tags="question")
canvas.create_text(170,325,text="A",tags=("1","txt1"))
canvas.create_text(330,325,text="B",tags=("2","txt2"))
canvas.create_text(255,385,text="C",tags=("3","txt3"))


canvas.pack()

canvas.tag_bind("1","<Button-1>",input)
canvas.tag_bind("2","<Button-1>",input)
canvas.tag_bind("3","<Button-1>",input)
canvas.tag_bind("4","<Button-1>",input)
canvas.tag_bind("txt1","<Button-1>",input)
canvas.tag_bind("txt2","<Button-1>",input)
canvas.tag_bind("txt3","<Button-1>",input)




def ChangeQuestion(ID):
    global Curr
    Curr = ID
    canvas.itemconfigure("question",text=Questions[ID]["question"])
    canvas.itemconfigure("txt1",text=Questions[ID]["1"])
    canvas.itemconfigure("txt2",text=Questions[ID]["2"])
    canvas.itemconfigure("txt3",text=Questions[ID]["3"])


def NextQuestion():
    global available
    question = choice(available)
    available.remove(question)
    if len(available) > 4:
        ChangeQuestion(question)
    else:
        fenetre.destroy()



NextQuestion()
fenetre.mainloop()
