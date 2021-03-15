from tkinter import *
from random import *
from Engine import *


def PagesWindow():
    pages = Tk()
    pages.title("Pages")

    dic = {}

    dic["1"] = PhotoImage(master=pages,file="Data\\Autres\\Pages\\1.png")
    dic["2"] = PhotoImage(master=pages,file="Data\\Autres\\Pages\\2.png")
    dic["3"] = PhotoImage(master=pages,file="Data\\Autres\\Pages\\3.png")
    dic["4"] = PhotoImage(master=pages,file="Data\\Autres\\Pages\\4.png")
    dic["5"] = PhotoImage(master=pages,file="Data\\Autres\\Pages\\5.png")
    dic["6"] = PhotoImage(master=pages,file="Data\\Autres\\Pages\\6.png")
    dic["7"] = PhotoImage(master=pages,file="Data\\Autres\\Pages\\7.png")
    dic["8"] = PhotoImage(master=pages,file="Data\\Autres\\Pages\\8.png")



    can = Canvas(pages,width=364,height=500)
    can.pack()
    can.create_image(163/2,153/2,image=dic["1"],tags="1")
    can.create_image(485/2,127/2,image=dic["2"],tags="2")
    can.create_image(607/2,324/2,image=dic["3"],tags="3")
    can.create_image(350.5/2,365/2,image=dic["4"],tags="4")
    can.create_image(170/2,485/2,image=dic["5"],tags="5")
    can.create_image(141/2,789/2,image=dic["6"],tags="6")
    can.create_image(490/2,630/2,image=dic["7"],tags="7")
    can.create_image(453/2,850/2,image=dic["8"],tags="8")

    ok = 0
    for i in range(1,9):
        if not GetVar("page"+str(i)):
            ok+=1
            can.itemconfigure(str(i),state="hidden")


    def TextCerf():
        tab = ["Je suis la",
               "Je te vois",
               "Proclame ton maitre",
               "Je vait détruire le monde",
               "Es-tu la, Mortel ?"]
        can.create_text(364/2,150,text=choice(tab),fill="red",font=('Helvetica', '16'))

    if(ok == 0):
        if(randint(1,25) == 1):
            TextCerf()
    elif ok== 8:
        can.create_text(364/2,250,text="Trouvez les pages cachées")

    pages.mainloop()
