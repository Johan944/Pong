from tkinter import* #interface graphique
import random #définir nombre aléatoire
import os #pour changer de fichier 
import pygame #pour les sons   
def haut(event): #monter les raquettes
    global y1,y2 #rend les variables accessibles  à la fonction
    if y1 > 0:
        y1 -= 30
        y2 -= 30
        Canevas.coords(2,900,y1,900,y2)
        Canevas.coords(1,100,y1,100,y2)
def bas(event): #descendre les raquettes
    global y1,y2
    if y2 < 600:
        y1 += 30
        y2 += 30
        Canevas.coords(2,900,y1,900,y2)
        Canevas.coords(1,100,y1,100,y2)
        
def Demarrer(event): #commencer partie
    global dx
    if arret == 1: #fonction activée si le jeu n'est pas en cours
        sens = random.randint(1,2) #définit le sens où va la balle
        if sens == 1:
            dx = -dx #palet se déplace à gauche
        mvt() #appel de la fonction pour déplacer la balle

def Recommencer (event): #recommencer une nouvelle partie
    Fenetre.destroy() #suppression de la fenêtre
    os.system("J1.py") #le programme se relance
    
def mvt(): #déplacement du palet
    global xpalet,ypalet,r,dx,dy,coups,arret
    arret = 0 #indicateur que le jeu est en cours
    xpalet += dx #déplacement palet
    ypalet += dy 
    if ypalet-r <= 0 or ypalet+r >= 600: #détection des bords du haut et du bas
        collision.play() #joue le son de collision
        dy = -dy 
    if xpalet - r == 100 and (ypalet-r >= y1 and ypalet+r <= y2): #détection collision avec raquette de gauche
        dx = -dx
        coups += 1
        raquette.play() 
    if xpalet + r == 900 and (ypalet+r >= y1 and ypalet+r <= y2): #détection collision avec raquette de droite
        dx = -dx
        coups += 1
        raquette.play()
    Canevas.coords(3,xpalet-r,ypalet-r,xpalet+r,ypalet+r) #le palet changent de coordonnées pour donner l'impression d'un mouvement
    if xpalet -r <= 0 or  xpalet +r >= 1000 : #détection si point marqué 
        gameover.play()
        if xpalet - r <= 0: 
            xpalet = 0
        else:
            xpalet = 1000
        Fenetre.after(40,perdu)#renvoie à la fonction perdu
    else:
        Fenetre.after(40,mvt) #récursivité de la fonction
        
    if coups == 5: #au bout de 5 collisions avec les raquettes, la vitesse du palet accélère
        if dx < 0:
            dx = -15
        else:
            dx = 15
        if dy < 0:
            dy = -15
        else:
            dy = 15
            
def perdu():
    Canevas.create_text(400,100,text="SCORE :", font="BolsterBold 70",fill='white') #affichage des messages
    Canevas.create_text(700,100,text=coups, font="BolsterBold 70",fill='white')
    Canevas.create_text(500,500,text="APPUYEZ SUR ECHAP POUR CONTINUER",font="BolsterBold 20", fill='white')
    Canevas.create_text(500,530,text="APPUYER SUR LA TOUCHE 'TAB' POUR RECOMMENCER",font="BolsterBlod 20", fill='white')
    
    

def sortie(event):
    Fenetre.destroy() #suppression de la fenêtre 
    os.system("option1.py")#affichage du menu
    
    
    
Fenetre = Tk() #création de la fenêtre
Fenetre.title("PONG") #ajout du titre de la fenêtre
Fenetre.geometry("1000x600+200+50") #on définit la taille de la fenêtre
Canevas = Canvas(Fenetre,width = 1000, height = 600,bg='black') #création de l'interface graphique
coups = 0 #initialisation du nombre
pygame.mixer.init() #initialisation de pygame pour importer des sons
collision = pygame.mixer.Sound("collision.wav") #importation sons 
gameover = pygame.mixer.Sound("gameover.wav") #importation sons  
raquette = pygame.mixer.Sound("raquette.wav") #importation sons
y1 = 250 #coordonnées des raquettes
y2 = 350 
r = 10 #rayon palet
xpalet = 500 #abscisse initiale du palet
ypalet = 300 #ordonnée initiale du palet
dx = 10 #vitesse horizontale
dy = 10 #vitesse verticale
arret = 1 #détection si le jeu est en route ou pas

Canevas.create_line(100,y1,100,y2, fill='white',width=5) #raquette de gauche
Canevas.create_line(900,y1,900,y2,fill='white',width=5) #raquette de droite
Canevas.create_rectangle(xpalet-r,ypalet-r,xpalet+r,ypalet+r,fill='white',outline='white') #palet
Canevas.create_line(500,0,500,50,fill='white')   #rond centrale, pointillés, etc....
Canevas.create_line(500,100,500,150,fill='white')
Canevas.create_line(500,200,500,250,fill='white')
Canevas.create_line(500,350,500,400,fill='white')
Canevas.create_line(500,450,500,500,fill='white')
Canevas.create_line(500,550,500,600,fill='white')
Canevas.create_oval(450,250,550,350,outline='white',width=2)
Canevas.create_oval(500,300,501,301,outline='white',width= 2)
Canevas.bind("<Up>",haut)       #assignation des touches aux fonctions
Canevas.bind("<Down>",bas)
Canevas.bind("<Escape>",sortie)
Canevas.bind("<Return>",Demarrer)
Canevas.bind("<Tab>",Recommencer)
Canevas.focus_set()
Canevas.pack()
Fenetre.mainloop()
