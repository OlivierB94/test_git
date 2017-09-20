from turtle import *

def triangle(couleur):
    if couleur in ('red', 'blue'):
        color(couleur)
     
    for i in range(3):
        fd(100)
        left(120)
 
couleur = input("Choisir une couleur : ")
triangle(couleur)
 
mainloop()
