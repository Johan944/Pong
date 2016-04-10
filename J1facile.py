from tkinter import*
import time
import random
import winsound
import os
import pygame         
def haut(event):
    global y1,y2
    if y1 > 0:
        y1 -= 30
        y2 -= 30
        Canevas.coords(2,900,y1,900,y2)
        Canevas.coords(1,100,y1,100,y2)
def bas(event):
    global y1,y2
    if y2 < 600:
        y1 += 30
        y2 += 30
        Canevas.coords(2,900,y1,900,y2)
        Canevas.coords(1,100,y1,100,y2)
def Demarrer(event):
    global dx
    if arret == 1:
        sens = random.randint(1,2)
        if sens == 1:
            dx = -dx
        mvt()

def Recommencer (event):
    Fenetre.destroy()
    os.system("J1facile.py")
    
def mvt():
    global xpalet,ypalet,r,dx,dy,coups,arret
    arret = 0
    xpalet += dx
    ypalet += dy
    if ypalet-r <= 0 or ypalet+r >= 600:
        collision.play()
        dy = -dy
    if xpalet - r == 100 and (ypalet-r >= y1 and ypalet+r <= y2):
        dx = -dx
        coups += 1
        raquette.play()
    if xpalet + r == 900 and (ypalet+r >= y1 and ypalet+r <= y2):
        dx = -dx
        coups += 1
        raquette.play()

    Canevas.coords(3,xpalet-r,ypalet-r,xpalet+r,ypalet+r)
    if xpalet -r <= 0 or  xpalet +r >= 1000 :
        gameover.play()
        if xpalet - r<= 0:
            xpalet = 15
        else:
            xpalet = 985
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
    Canevas.create_text(400,100,text="SCORE :", font="BolsterBold 70",fill='white')
    Canevas.create_text(700,100,text=coups, font="BolsterBold 70",fill='white')
    Canevas.create_text(500,500,text="APPUYEZ SUR ECHAP POUR CONTINUER",font="BolsterBold 20", fill='white')
    Canevas.create_text(500,530,text="APPUYER SUR LA TOUCHE 'TAB' POUR RECOMMENCER",font="BolsterBlod 20", fill='white')
    
def sortie(event):
    Fenetre.destroy()
    os.system("option1")
    
    
    
           
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
y1 = 200 
y2 = 400 
coups = 0
r = 10 #rayon palet
xpalet = 500 #palet
ypalet = 300 #palet
dx = 10
dy = 10
arret = 1
Canevas.create_line(100,y1,100,y2, fill='white',width=5) 
Canevas.create_line(900,y1,900,y2,fill='white',width=5)
Canevas.create_rectangle(xpalet-r,ypalet-r,xpalet+r,ypalet+r,fill='white',outline='white')
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
Canevas.bind("<Escape>",sortie)
Canevas.bind("<Return>",Demarrer)
Canevas.bind("<Tab>",Recommencer)
Canevas.focus_set()
Canevas.pack()
Fenetre.mainloop()



