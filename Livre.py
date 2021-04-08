# Dictionnaire informatif par Julien

from tkinter import *
from Engine import *

def DicWindow():

    curr = "harold"

    livre = Tk()
    livre.title("Dictionaire")

    dic = {
        "joueur":{
            "type":"perso",
            "nom":"Joueur",
            "profession":"Héro",
            "age":"???",
            "residence":"Une autre dimension",
            "desc":"Vous êtes le héro de cette aventure. Vous ne savez pas la raison exacte de votre présence en Vlatyr mais une chose est sure : Vous allez accomplir votre quête.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\hero.png"),
        },
        "harold":{
            "type":"perso",
            "nom":"Harold",
            "profession":"Retraité",
            "age":"73 ans",
            "residence":"4 rue du Cerf",
            "desc":"Harold vit paisiblement dans la région de Vlatyr, dans les Provinces Unis de Kosky. Il est toujours pret à partager un café et a beaucoup de problèmes. Il semble cependant cacher des ambitions étranges.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\harold.png"),
        },
        "rickey":{
            "type":"perso",
            "nom":"Rickey",
            "profession":"PDG",
            "age":"???",
            "residence":"RickeyLand",
            "desc":"Rickey est le PDG du parc RickeyLand, un endroit pour toute la famille. Il n'aime pas voir son égo maltraité et il compte détruire tout ceux qui ne viennent pas à la boutique de souvenir. Il semble détester Harold.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\rickey.png"),
        },
        "rick0":{
            "type":"perso",
            "nom":"Rick0",
            "profession":"PDG",
            "age":"???",
            "residence":"RickeyLand",
            "desc":"Rickey a été amellioré en Rick0, une machine de guerre sanguinaire qui ne souhaite qu'une chose : détruire Harold et son envoyé. Ses amelliorations lui permettent d'avoir une agilité et une force supérieur.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\rick0.png"),
        },
        "chasseur":{
            "type":"perso",
            "nom":"Chasseur",
            "profession":"Chasseur",
            "age":"43 ans",
            "residence":"3 rue du Merle",
            "desc":"Ce chasseur ne va pas bien, il chasse en pleine nuit tout ce qui bouge. Il ne faut surtout pas le croiser, car l'on risque de se faire tirer dessus. Il est aussi connu pour ses mauvaises blagues.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\chasseur.png"),
        },
        "garde":{
            "type":"perso",
            "nom":"Garde",
            "profession":"Garde",
            "age":"???",
            "residence":"RickeyLand",
            "desc":"Personne ne sait pourquoi il y a autant de gardes à RickeyLand, ni pourquoi ils se ressemblent tous. La seule chose qui est certaine est leur obéissance absolu à Rickey, leur PDG.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\garde.png"),
        },
        "archer":{
            "type":"perso",
            "nom":"Archer",
            "profession":"Voleur",
            "age":"34 ans",
            "residence":"Marais Maudit",
            "desc":"Cet archer est très fier de sa position dominante dans le marais maudit. Depuis la mort de l'ogre, il peut se permettre d'établir des raids contre les villages alentours.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\archer.png"),
        },
        "marchand":{
            "type":"perso",
            "nom":"Marchand",
            "profession":"Escroc",
            "age":"52 ans",
            "residence":"15 rue des bars",
            "desc":"Ce marchand est en réalité un escroc, il extorque des montants énormes chez les plus vieux. Il n'a cependant pas beaucoup de succes avec les populations plus jeunes.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\marchand.png"),
        },
        "invocateurs":{
            "type":"perso",
            "nom":"Invocateur",
            "profession":"Cultiste",
            "age":"???",
            "residence":"Forteresse Noire",
            "desc":"Les Invocateurs sont sous l'égide d'Harold, ils forment un culte qui n'a qu'un rêve : reveiller leur maitre et plonger le monde dans le chaos",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\invocateurs.png"),
        },
        "cerf":{
            "type":"perso",
            "nom":"Seigneur Cerf",
            "profession":"Dieu",
            "age":"Infini",
            "residence":"La terre des Cerfs",
            "desc":"Seigneur Cerf est le dieu ultime d'Harold et des Invocateurs. Il souhaite plonger le monde dans le chaos et détruire son rival, le Grand Caribou. Il n'utilise en général qu'1% de sa puissance en combat.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\cerf.png"),
        },
        "waldo":{
            "type":"perso",
            "nom":"Waldo",
            "profession":"Employé",
            "age":"40 ans",
            "residence":"RickeyLand",
            "desc":"Waldo est un homme très occupé. Il s'occupe de la totalité du parc, des attractions au restaurant du parc. Il aimerait bien pouvoir avoir un peut d'aide, mais il se débrouille comme il le peut.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\waldo.png"),
        },
        "rickeyland":{
            "type":"lieu",
            "nom":"RickeyLand",
            "desc":"RickeyLand est un endroit féerique pour toute la famille. Ici, vous pourrez jouer à nos nombreuses attractions comme la maison hantée ou le tir sur marchand. N'oubliez surtout pas de venir à la boutique de souvenir. \nPublicité de RickeyLand",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\rickeyland.png"),
        },
        "chezharold":{
            "type":"lieu",
            "nom":"4 rue du Cerf",
            "desc":"Ce chalet est le lieu de vie d'Harold, il y a vecu toute sa vie et il l'aime beaucoup. Parlez-lui de sa maison et il pourrait vous raconter pendant des journées entières son enfance.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\chezharold.png"),
        },
        "chezchasseur":{
            "type":"lieu",
            "nom":"3 rue du Merle",
            "desc":"Cette maison est le lieu de vie d'un chasseur de Vlatyr. On raconte qu'il lui arrive de tirer sur des passants depuis sa fenêtre. C'est pour cela que personne ne s'aventure près de ce lieu.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\chezchasseur.png"),
        },
        "tournoir":{
            "type":"lieu",
            "nom":"Forteresse Noire",
            "desc":"Cette forteresse est le lieu de vie des Invocateurs et de leur chef Harold. C'est un endroit sinistre ou de nombreuses invocations illégales et atroves ont été fait.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\tournoir.png"),
        },
        "braise":{
            "type":"lieu",
            "nom":"Forteresse Braise",
            "desc":"Cette forteresse fut le lieu de vie du Seigneur Braise quand il était encore en vie. Elle a été détruite par un inconnu un an après la mort de son propriétaire. Personne ne sait pourquoi.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\braise.png"),
        },
        "marais":{
            "type":"lieu",
            "nom":"Marais Maudit",
            "desc":"Ce marais est un lieu maudit, il fut pendant longtemps le lieu de vie d'un terrible ogre qui mangeait les enfants. Depuis quelques temps, l'ogre est mort et un archer s'est auto-proclamé seigneur du marais.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\marais.png"),
        },
        "seigneurnoir":{
            "type":"perso",
            "nom":"Seigneur Noir",
            "profession":"Bras Droit",
            "age":"52 ans",
            "residence":"RickeyLand",
            "desc":"Le seigneur noir est le bras droit du PDG Rickey, c'est lui qui s'occupe de gérer les entrées du parc et du palais. On raconte qu'il a volé le titre à son prédecesseur, qui a gardé son chapeau en guise de protestation.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\seigneurnoir.png"),
        },
        "sheperd":{
            "type":"perso",
            "nom":"???",
            "profession":"???",
            "age":"???",
            "residence":"Forteresse Noire",
            "desc":"Ce soldat est un vrai mystère. Personne ne sais d’où il vient, ni pourquoi il est là. La seule chose qui est sure c'est qu'il protégera son maître de sa vie. Il a beaucoup de talents qui font de lui un redoutable combattant.",
            "img":PhotoImage(master=livre,file="Data\\Autres\\Livre\\sheperd.png"),
        },
    }



    can = Canvas(livre,width=500,height=300)
    can.pack(side = RIGHT)
    can.create_rectangle(0,0,500,50,fill="gray")
    can.create_rectangle(0,50,250,300,fill="lightgray")
    can.create_rectangle(250,50,500,300,fill="darkgray")
    can.create_text(60,25,text="",tags="nom")
    can.create_text(160,25,text="",tags="age")
    can.create_text(260,25,text="",tags="job")
    can.create_text(410,25,text="",tags="res")
    can.create_text(125,150,text="",tags="desc",width=240,justif="left")
    can.create_image(375,175,image="",tags="img")


    ListFrame = Frame(livre,height=300)
    list_Perso = Listbox(ListFrame)

    def GetKeyFromName(Name):
        for key in dic.keys():
            if dic[key]["nom"] == Name:
                return key

    def SetCurrent(event):
        curr = GetKeyFromName(list_Perso.get(list_Perso.curselection()[0]))
        can.delete("nom")
        if dic[curr]["type"] == "lieu":
            can.create_text(80,25,text="Nom : "+dic[curr]["nom"],tags="nom")
            can.itemconfigure("age",text="")
            can.itemconfigure("job",text="")
            can.itemconfigure("res",text="")
            can.itemconfigure("desc",text=dic[curr]["desc"])
            can.itemconfigure("img",image=dic[curr]["img"])
        else:
            can.create_text(60,25,text="Nom : "+dic[curr]["nom"],tags="nom")
            can.itemconfigure("age",text="Age : "+dic[curr]["age"])
            can.itemconfigure("job",text="Travail : "+dic[curr]["profession"])
            can.itemconfigure("res",text="Residence : "+dic[curr]["residence"])
            can.itemconfigure("desc",text=dic[curr]["desc"])
            can.itemconfigure("img",image=dic[curr]["img"])




    tab =  []
    for key in dic.keys():
        tab.append(dic[key]["nom"])
    tab = sorted(tab)
    for key in tab:
        if GetKeyFromName(key) == "joueur" or GetVar("dic_"+GetKeyFromName(key)):
            list_Perso.insert(END,key)
    list_Perso.pack( side = LEFT,expand=True,fill=BOTH)
    list_Perso.selection_set(0)
    list_Perso.bind('<<ListboxSelect>>',SetCurrent)
    ListFrame.pack(side = LEFT,expand=True)
        
        

    SetCurrent("harold")

    livre.mainloop()
