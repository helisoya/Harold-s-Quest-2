#Tetris par Julien

from tkinter import *
from random import *

diff = 1


currBloc = []

colors = {
    "0":"white",
    "#":"blue",
    "1":"green",
}

data = []
input = 0

nb = 5*diff

root = Tk()

can = Canvas(root,width=6*40,height=10*40+50)
can.pack()

for i in range(10):
    data.append([])
    for p in range(6):
        data[i].append(0)
        can.create_rectangle(40*p,40*i,40*(p+1),40*(i+1))


def Apparition(t):
    global data,currBloc,nb
    nb-=1
    if nb == 0:
        return True
    currBloc = []
    for bloc in t:
        currBloc.append(bloc)
        if data[bloc[0]][bloc[1]] != 0:
            return False
    return True

def Update():
    can.delete("all")
    for i in range(len(data)):
        for j in range(len(data[i])):
            col = str(data[i][j])
            if [i,j] in currBloc:
                col = "#"
            can.create_rectangle(40*j,40*i,40*(j+1),40*(i+1),fill=colors[col])
    can.create_text((5*40)/2,10*40+25,text="Restant : "+str(nb))

def CheckIfFree(pos,y,x):
    if y > 0 and pos[0] == len(data)-1 or x > 0 and pos[1] == len(data[0])-1 or x < 0 and pos[1] == 0:
        return False
    if data[pos[0]+y][pos[1]+x] == 0:
        return True
    return False

def GetInput(event):
    global input
    input = event.keycode

def Move():
    global currBloc,input
    x = 1
    if input == 37:
        x = -1
    ok = True
    for bloc in currBloc:
        if not CheckIfFree(bloc,0,x):
            ok = False
    for bloc in currBloc:
        if ok:
           bloc[1]+=x
    input = 0

def Reset():
    global nb,data,currBloc,input
    data = []
    for i in range(10):
        data.append([])
        for p in range(6):
            data[i].append(0)

    currBloc = []
    nb = 5*diff
    input = 0
    
def DestroyRow(row,i):
    global data
    data[row][i] = 0
    i+=1
    if i == len(data[row]):
        return
    root.after(50,lambda:DestroyRow(row,i))
    

def MainLoop():
    global currBloc,data

    if input != 0:
        Move()
    
    ok = True
    for bloc in currBloc:
        if not CheckIfFree(bloc,1,0):
            ok = False
    for bloc in currBloc:
        if ok:
           bloc[0]+=1
        else:
            data[bloc[0]][bloc[1]] = 1

    if not ok or currBloc == []:

        for i in range(len(data)):
            if not 0 in data[i]:
                DestroyRow(i,0)
        
        if not Apparition(choice([
    [ [0,0],[1,0],[2,0] ], # |
    [ [0,0],[0,1],[0,2] ], # -
    [ [0,0],[0,1],[0,2],[1,1] ], # T
    [ [0,1],[1,0],[1,1],[1,2] ], # T enverse
    [ [0,0],[1,0],[1,1] ], # L
    [ [1,0],[1,1],[0,1] ], # L envers
        ])):
            Reset()
        if nb == 0:
            root.destroy()
            
    if nb > 0:
        Update()

    root.after(550-50*diff,MainLoop)

Apparition(choice([
    [ [0,0],[1,0],[2,0] ], # |
    [ [0,0],[0,1],[0,2] ], # -
    [ [0,0],[0,1],[0,2],[1,1] ], # T
    [ [0,1],[1,0],[1,1],[1,2] ], # T enverse
    [ [0,0],[1,0],[1,1] ], # L
    [ [1,0],[1,1],[0,1] ], # L envers
    ]))

Update()

root.bind("<Left>",GetInput)
root.bind("<Right>",GetInput)

MainLoop()

root.mainloop()

