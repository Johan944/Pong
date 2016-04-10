from tkinter import*
import time
import random
import winsound
import pygame
from pygame.locals import *
import os
def haut2(event):
    global y3,y4
    if y3 > 0:
        y3 -= 30
        y4 -= 30
        Canevas.coords(1,100,y3,100,y4)
def bas2(event):
    global y3,y4
    if y4 < 600:
        y3 += 30
        y4 += 30
        Canevas.coords(1,100,y3,100,y4)               
def haut(event):
    global y1,y2
    if y1 > 0:
        y1 -= 30
        y2 -= 30
        Canevas.coords(2,900,y1,900,y2)
def bas(event):
    global y1,y2
    if y2 < 600:
        y1 += 30
        y2 += 30
        Canevas.coords(2,900,y1,900,y2)
def Demarrer(event):
    global dx, arret
    if arret == 1:
        sens = random.randint(1,2)
        if sens == 1:
            dx = -dx
        mvt()

def Recommencer (event) :
    Fenetre.destroy()
    os.system("J2.py")



def mvt():
    global xpalet,ypalet,r,dx,dy,score1,score2,coups,arret
    arret = 0
    xpalet += dx
    ypalet += dy
    if ypalet-r <= 0 or ypalet+r >= 600:
        collision.play()
        dy = -dy
    if xpalet - r == 100 and (ypalet-r >= y3 and ypalet+r <= y4):
        dx = -dx
        coups += 1
        raquette.play()
    if xpalet + r == 900 and (ypalet+r >= y1 and ypalet+r <= y2):
        dx = -dx
        coups += 1
        raquette.play()
    Canevas.coords(3,xpalet-r,ypalet-r,xpalet+r,ypalet+r)
    if xpalet -r <= 0 or  xpalet +r >= 1000 :
        if xpalet - r<= 0:
            xpalet = 15
            score2 += 1
            Canevas.itemconfigure(5,text=score2)
        else:
            xpalet = 985
            score1 += 1
            Canevas.itemconfigure(4,text=score1)
        Fenetre.after(40,perdu)
    else:
        Fenetre.after(40,mvt)
    if coups == 5:
        if dx < 0:
            dx = -15
        else:
            dx = 15
        if dy < 0:
            dy = -15
        else:
            dy = 15
def perdu():
    global score1,score2,y1,y2,r,xpalet,ypalet,dx,dy,coups,y3,y4,arret
    perdu1.play()
    arret = 1
    if score1 != 11 and score2 != 11:
        coups = 0
        y1 = 200 
        y2 = 400
        y3 = 200
        y4 = 400
        r = 10 #rayon palet
        xpalet = 500 #palet
        ypalet = 300 #palet
        dx = 10
        dy = 10
        Canevas.coords(1,100,y3,100,y4)
        Canevas.coords(2,900,y1,900,y2)
        Canevas.coords(3,xpalet-r,ypalet-r,xpalet+r,ypalet+r)
    elif score1 == 11:
        Canevas.create_text(500,200,text="VICTOIRE JOUEUR 1",font="BolsterBold 50",fill='red')
        Canevas.create_text(500,500,text="APPUYEZ SUR ECHAP POUR REVENIR AU MENU",font="BolsterBold 20", fill='white')
        Canevas.create_text(500,530,text="APPUYER SUR LA TOUCHE 'TAB' POUR RELANCER LA PARTIE",font="BolsterBold 20", fill='white')
    else:
        Canevas.create_text(500,200,text="VICTOIRE JOUEUR 2",font="BolsterBold 50",fill='blue')
        Canevas.create_text(500,500,text="APPUYEZ SUR ECHAP POUR REVENIR AU MENU",font="BolsterBold 20", fill='white')
        Canevas.create_text(500,530,text="APPUYER SUR LA TOUCHE 'TAB' POUR RELANCER LA PARTIE",font="BolsterBold 20", fill='white')
        
def sortie(event):
    Fenetre.destroy()
    os.system("option2.py")
    
Fenetre = Tk()
Fenetre.title("PONG")
Fenetre.geometry("1020x630+200+50")

Canevas = Canvas(Fenetre,width = 1000, height = 600,bg='black')
Canevas.pack()
coups = 0
pygame.mixer.init()
collision = pygame.mixer.Sound("collision.wav")
gameover = pygame.mixer.Sound("gameover.wav")
raquette = pygame.mixer.Sound("raquette.wav")
perdu1 = pygame.mixer.Sound("perdu.wav")
y1 = 200 
y2 = 400 
y3 = 200
y4 = 400
score1 = 0
score2 = 0
r = 10 #rayon palet
xpalet = 500 #palet
ypalet = 300 #palet
dx = 10
dy = 10
arret = 1
Canevas.create_line(100,y3,100,y4, fill='white',width=5) 
Canevas.create_line(900,y1,900,y2,fill='white',width=5)
Canevas.create_rectangle(xpalet-r,ypalet-r,xpalet+r,ypalet+r,fill='white',outline='white')
Canevas.create_text(250,50,text = score1, font ="BolsterBold 70", fill='red')
Canevas.create_text(750,50,text = score2, font ="BolsterBold 70", fill='blue')
Canevas.create_line(500,0,500,50,fill='white')
Canevas.create_line(500,100,500,150,fill='white')
Canevas.create_line(500,200,500,250,fill='white')
Canevas.create_line(500,350,500,400,fill='white')
Canevas.create_line(500,450,500,500,fill='white')
Canevas.create_line(500,550,500,600,fill='white')
Canevas.create_oval(450,250,550,350,outline='white',width=2)
Canevas.create_oval(500,300,501,301,outline='white',width= 2)
Canevas.bind("<Up>",haut)
Canevas.bind("<Down>",bas)
Canevas.bind("<KeyPress-z>",haut2)
Canevas.bind("<KeyPress-Z>",haut2)
Canevas.bind("<KeyPress-s>",bas2)
Canevas.bind("<KeyPress-S>",bas2)
Canevas.bind("<Escape>",sortie)
Canevas.bind("<Return>",Demarrer)
Canevas.bind("<Tab>",Recommencer)
Canevas.focus_set()
Canevas.pack()
Fenetre.mainloop()
