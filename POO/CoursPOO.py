#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:13:21 2020

@author: simplon
"""
# class superstring:
#     def __init__(self,chaine):
#         self.ch=chaine
#     def ajoute(self,char):
#         self.ch+=char
#     def insert(self,char,i):
#         self.ch=self.ch[:i]+char+self.ch[i:]
#     def upper(self):
#         self.ch = self.ch.upper()
#     def capsdown(self):
#         self.ch = self.ch.lower()
#     def tri(self):
#         self.ch = self.ch.split()
#         self.ch.sort()
#         self.ch = " ".join(self.ch)
#     def __str__(self):
#         return "« type : superstring, content : ECOUTEZ BIEN C'EST TRÈS IMPORTANT CE QUE JE DIS ! »"
    
# s1 = superstring("Ecoutez bien c'est important")
# s1.ajoute(" ce que je dis!")
# s1.insert(" très", 18)
# s1.upper()
# print(s1)

# class formulaire :
#     def __init__(self,nom,prenom,anneeNaissance):
#         self.nom =nom.upper()
#         self.prenom = prenom.upper()
#         self.anneeNaissance = anneeNaissance
#     def age(self):
#         return 2020-self.anneeNaissance
#     def majeur(self):
#         return self.age()>=18
#     def memeFamille(self,formulaire):
#         return self.nom == formulaire.nom
#     def memeformulaire(self,formulaire):
#         if  self.nom == formulaire.nom and self.prenom == formulaire.prenom and self.anneeNaissance == formulaire.anneeNaissance:
#             return True
#         else:
#             return False
    
#     def __repr__(self):
#         return repr((self.nom,self.prenom,self.anneeNaissance))
    
# jd = formulaire('Doe', 'John', 2005)
# ad = formulaire('doe', 'alice', 2000)
# hc= formulaire('cancian', 'hadrien', 1997)

# liste = [jd,ad,hc]
# print(liste)
# liste.sort(key = lambda annee: annee.anneeNaissance)
# print(liste)

#Bataille

from random import randrange

# Enfin on crée une liste de tuple
# pour représenter le paquet de cartes


# Deuxième partie du code
# Chacun des deux joueurs tire une carte aléatoirement, elle est
# supprimé du paquet et on répète l'opération pour chaque tour.

valeur = 6
couleur = 4
nbTour = 12
paquet = [(v,c) for v in range(1,valeur) for c in range(1,couleur)]
print(paquet)
class partie :
    def __init__(self,valeur,couleur,nbTours):
            self.valeur= valeur
            self.couleur = couleur
            self.nbTours = nbTours
    def __repr__(self):
        return repr([self.valeur,self.couleur,self.nbTours])

class carte:
    def __init__(self,valeur,couleur):
        self.valeurs = randrange(1,valeur)
        self.couleurs = randrange(1,couleur)
    def __repr__(self):
        return repr((self.valeurs,self.couleurs))

debut = partie(valeur,couleur,nbTour)
print(debut)
main1, main2 = [], []

# def piocher(m1,m2,paq,nbTour):
#     for i in range (nbTour):
#         # f  carte(valeur,couleur) in paquet:
#           x = carte(valeur,couleur)
#           # paquet.remove(x)
#         # elif carte(valeur,couleur) in paquet:
#           y = carte(valeur,couleur)
#           # paquet.remove(y)
#           if x !=y :
#               main1.append(x)
#               main2.append(y)
# piocher(main1,main2,paquet,debut.nbTours)


def plusGrandQue(m1,m2,nbTour):
    score1 = 0
    score2 = 0
    for i in range(nbTour):
        carte1 = carte(valeur,couleur)
        carte2 = carte(valeur,couleur)
        if carte1.valeurs >carte2.valeurs :
            score1 +=1
        else:
            score2 +=1
    if score1 == score2:
        return ("Match Nul")
    else:
        return ("Vainqueur : " + ("joueur 1, le joueur 1 a marqué "+str(score1)+" points & le joueur 2 a marqué "+str(score2)+" points" if score1 > score2 else "joueur 2 ,le joueur 1 a marqué "+str(score1)+" points & le joueur 2 a marqué "+str(score2)+" points"))
VICTOIRE = plusGrandQue(main1,main2,debut.nbTours)
print(VICTOIRE)
