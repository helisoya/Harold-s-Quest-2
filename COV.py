# Call of Vautours par Julien

from tkinter import *
from random import *

cooldown = 0
score = 0
click_x = -50
click_y = -50
end = False
img = []

vautours = []

def MiniGame_COV():
    global cooldown,score,click_x,click_y,end,img,vautours

    cooldown = 0
    score = 0
    click_x = -50
    click_y = -50
    end = False
    img = []

    vautours = []

    root = Tk()
    root.title("Call of Vautours")
    can = Canvas(root,width=750,height=500)
    can.pack()

    img = [
        PhotoImage(master=root,file="Data/Autres/COV/bg.png"),
        PhotoImage(master=root,file="Data/Autres/COV/v1.png"),
        PhotoImage(master=root,file="Data/Autres/COV/v2.png"),
        PhotoImage(master=root,file="Data/Autres/COV/v3.png"),
        PhotoImage(master=root,file="Data/Autres/COV/v4.png"),
        PhotoImage(master=root,file="Data/Autres/COV/v5.png"),
        ]

    can.create_image(750/2,250,image=img[0])
    can.create_text(20,20,text="Score : 0",anchor=W,fill="white",tags="score")


    class Vautour:
        def __init__(self,X,SPD,IMG):
            self.x = X
            self.y = -50
            self.spd = SPD
            self.img = IMG

        def Update(self):
            global click_x,click_y,end,score
            self.y+=self.spd
            if self.y >= 550:
                end = True
                return True
            if (self.x-225/2 <= click_x <= self.x+225/2) and (self.y-150/2 <= click_y <= self.y+150/2):
                score+=1
                click_x = -50
                click_y = -50
                return True
            return False

    def Click(event):
        global click_x,click_y
        click_x = event.x
        click_y = event.y
        root.after(10,Reset_Click)

    def Reset_Click():
        global click_x,click_y
        click_x = -50
        click_y = -50

    def MainLoop():
        global vautours,end,img,score,cooldown

        can.delete("v")

        if cooldown > 0:
            cooldown-=1
        else:
            cooldown = randint(20,60)
            vautours.append(Vautour(randint(50,700),randint(2,4),randint(1,5)))

        toDel = []
        for v in vautours:
            if v.Update():
                toDel.append(v)
            can.create_image(v.x,v.y,image=img[v.img],tags="v")

        for elem in toDel:
            vautours.remove(elem)
            del elem

        can.itemconfigure("score",text="Score : "+str(score))

        if not end:
            root.after(8,MainLoop)
        else:
            del vautours[:]
            vautours = []
            end = False
            score = 0
            can.create_text(750/2,250,text="Perdu !",fill="white",tags="v")
            root.after(2000,MainLoop)


    root.bind("<Button-1>",Click)
    MainLoop()
    root.mainloop()
