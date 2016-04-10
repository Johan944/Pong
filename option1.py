from tkinter import*
import time
import random
import os
import pygame
def pointeur(event):
    global joueur 
    if (event.x >= 382 and event.x <= 618) and (event.y >= 202 and event.y <= 252): #détection J1
        Fenetre.destroy()
        os.system("J1facile.py")
    if (event.x >= 382 and event.x <= 618) and (event.y >= 302 and event.y <= 352): #détection J2
        Fenetre.destroy()
        os.system("J1.py")
    if (event.x > 382 and event.x <= 618) and (event.y >=402 and event.y <= 452): #détection Quitter
        Fenetre.destroy()
        os.system("J1difficile.py")
    if (event.x > 20 and event.x <= 200) and (event.y >=525 and event.y <= 580): #détection Quitter
        Fenetre.destroy()
        os.system("Menu.py")

def J1facile (event) :
    Fenetre.destroy()
    os.system("J1facile.py")
def J1 (event) :
    Fenetre.destroy ()
    os.system("J1.py")
def J1difficile (event) :
    Fenetre.destroy()
    os.system("J1difficile")

def sortie(event) :
    Fenetre.destroy()
    os.system("Menu.py")

Fenetre=Tk()
Fenetre.title("PONG : 1 JOUEUR -> CHOIX NIVEAU")
Fenetre.geometry("1020x630+200+50")
Canevas = Canvas(Fenetre, width = 1000, height=600,bg='black')
Canevas.pack()
Canevas.bind("<Button-1>",pointeur) #détection coordonnées clic de la souris
Canevas.focus_set()
Canevas.pack()

Canevas.bind("<Escape>",sortie)
Canevas.create_text(500,75,text='1 JOUEUR',font="BolsterBold 70",fill ='white')
Canevas.create_text(500,225,text='Facile',font="BolsterBold 30",fill ='white')
Canevas.create_text(500,325,text='Normal',font="BolsterBold 30",fill ='white')
Canevas.create_text(500,425,text='Difficile',font="BolsterBold 30",fill ='white')
Canevas.create_text(110,552,text='Retour',font="BolsterBold 30",fill ='white')
Canevas.create_rectangle(380,200,620,255,outline='white',width=3)
Canevas.create_rectangle(380,300,620,355,outline='white',width=3)
Canevas.create_rectangle(380,400,620,455,outline='white',width=3)
Canevas.create_rectangle(20,525,200,580,outline='white',width=3)
Canevas.bind("<KeyPress-f>",J1facile)
Canevas.bind("<KeyPress-F>",J1facile)
Canevas.bind("<KeyPress-n>",J1)
Canevas.bind("<KeyPress-N>",J1)
Canevas.bind("<KeyPress-d>",J1difficile)
Canevas.bind("<KeyPress-D>",J1difficile)
Fenetre.mainloop()



