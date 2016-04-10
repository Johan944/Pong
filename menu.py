from tkinter import*
import time
import random
import os
import pygame

def pointeur(event):
    global joueur 
    if (event.x >= 382 and event.x <= 618) and (event.y >= 202 and event.y <= 252): #détection J1
        Fenetre.destroy()
        musique.stop()
        os.system("option1.py") 

    if (event.x >= 382 and event.x <= 618) and (event.y >= 302 and event.y <= 352): #détection J2
        Fenetre.destroy()
        musique.stop()
        os.system("option2.py")  #lance le programme 2 Joueurs
    if (event.x > 382 and event.x <= 618) and (event.y >=402 and event.y <= 452): #détection Quitter
        musique.stop()
        Fenetre.destroy()
    
def option1 (event) :
    Fenetre.destroy()
    os.system("option1.py")
def option2 (event) :
    Fenetre.destroy()
    os.system("option2.py")
def sortie (event) :
    Fenetre.destroy()

Fenetre = Tk()
Fenetre.title("PONG")
Fenetre.geometry("1000x600+200+50")
Canevas = Canvas(Fenetre, width = 1000, height=600,bg='black')
Canevas.pack()
Canevas.bind("<Button-1>",pointeur) #détection coordonnées clic de la souris
Canevas.focus_set()
Canevas.pack()
pygame.mixer.init()
musique = pygame.mixer.Sound("musiquemenu.wav")
musique.play()
Canevas.create_text(500,75,text='PONG',font="BolsterBold 70",fill ='white')
Canevas.create_text(500,225,text='1 Joueur',font="BolsterBold 30",fill ='white')
Canevas.create_text(500,325,text='2 Joueurs',font="BolsterBold 30",fill ='white')
Canevas.create_text(500,425,text='Quitter',font="BolsterBold 30",fill ='white')
Canevas.create_rectangle(380,200,620,255,outline='white',width=3)
Canevas.create_rectangle(380,300,620,355,outline='white',width=3)
Canevas.create_rectangle(380,400,620,455,outline='white',width=3)
Canevas.bind("<KeyPress-1>",option1)
Canevas.bind("<KeyPress-2>",option2)
Canevas.bind("<Escape>",sortie)
Fenetre.mainloop()


