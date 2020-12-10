import random
from tkinter import Button,Tk,Label
global playerscore,comscore,draw
playerscore=0
comscore=0
draw=0
def play(n,t):
    global comscore,playerscore,draw
    comp=random.choice([0,1,2])
    dictionary={0:'paper',1:'scissor',2:'rock'}
    t['text']='com plays '+dictionary[comp]
    if comp==n+1 or (comp==0 and n==2):
        comscore+=1
    elif comp==n-1 or (comp==2 and n==0):
        playerscore+=1
    else:
        draw+=1
def main():
    global playerscore,comscore,draw
    tk=Tk()
    comlabel=Label(tk,text=' ')
    rock=Button(tk,text='rock',width=16,command=lambda:play(2,comlabel))
    scissor=Button(tk,text='scissor',width=16,command=lambda:play(1,comlabel))
    paper=Button(tk,text='paper',width=16,command=lambda:play(0,comlabel))
    comlabel.pack()
    rock.pack()
    scissor.pack()
    paper.pack()
    tk.mainloop()
    scoretk=Tk()
    scoreplayer=Label(scoretk,text='your score : '+str(playerscore))
    scorecom=Label(scoretk,text='com score : '+str(comscore))
    scoredraw=Label(scoretk,text='draws : '+str(draw))
    scoreplayer.pack()
    scorecom.pack()
    scoredraw.pack()
main()
