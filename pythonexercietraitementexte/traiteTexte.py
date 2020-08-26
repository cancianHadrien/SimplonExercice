#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:15:15 2020

@author: simplon
"""
from re import findall
from re import sub
# EXO 1
# q = "Bonjour je m'appelle Hadrien"

# def hascap(s):
#     maj = s.split()
#     for i in maj:
#         if ord(i[0]) < 90 and ord(i[0])>65:
#             print(i)
    
# hascap(q)

# EXO 2
# prix = "Le prix est de 67 euros"     
# def inflation (s):
#     liste_prix  = s.split()
#     for i,value in enumerate(liste_prix):
#         if value.isnumeric():
#             double = int(value)*2
#             print("Le prix est de {} euros".format(double))
# inflation(prix)
#EXO 3

# s = "Onze ans déjà que cela passe vite Vous "
# s += "vous étiez servis simplement de vos armes la "
# s += "mort n‘éblouit pas les yeux des partisans Vous "
# s += "aviez vos portraits sur les murs de nos villes "

# listeMot = s.split()

# def cut(s):
#     ligne = ""
#     vide = []
#     for mot in listeMot:
#         if len(ligne)+1+len(mot) > 24:
#             vide.append(ligne)
#             ligne = mot+" "
#         else:
#             ligne += mot +" "
#     vide.append(ligne)        
#     print(vide)
    
# cut(s)

# EXO 4
    # q = "Les 2 maqueraux valent 6.50 euros et -3,3"
    
    # def chiffre(s):
    #     motif = '-*[0-9]*[\.\,]*[0-9]+'
    #     s = findall(motif,q)
    #     print(s)
    
    # chiffre(q)

# EXO 5

# chiffre = "3.3 et -3,6"
# def arrondi(s):
#       motif = '[\.\,]+[0-9]+'
#       q = sub(motif,'',s)
#       print(q)
# arrondi(chiffre)
