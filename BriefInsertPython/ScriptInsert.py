#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:56:07 2020

@author: simplon
"""
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://hadrien:H01011997C@localhost/ASSURAUTO")

SQL_Query = pd.read_sql_query("select * from CONTRAT",engine)
SQL_Query2 = pd.read_sql_query("select * from CLIENTS",engine)
print(SQL_Query)
print(SQL_Query2)
print ('Veuillez entrer la date du contrat sous ce format AAAA-MM-JJ')
Date_Contrat = input()
while len(Date_Contrat) < 10:
    print ('Veuillez entrer la date du contrat sous ce format AAAA-MM-JJ')
    Date_Contrat = input()
print ('Veuillez entrer la categorie du contrat')
Cat_Contrat = input()
print ("Veuillez entrer le bonus du client (en pourcentage)")
Bon_Contrat = input()
print ('Veuillez entrer le malus du client (en pourcentage)')
Mal_Contrat = input()
print ('Veuillez entrer le nom du client en majuscule')
Nom_Client = input()
if Nom_Client.isupper() == False:
    Nom_Client = Nom_Client.upper()
print ('Veuillez entrer le prénom du client en majuscuule')
Prenom_Client = input()
if Prenom_Client.isupper() == False:
    Prenom_Client = Prenom_Client.upper()
print ("Veuillez entrer l'adresse du client")
Adresse_Client =input()
print ('Veuillez entrer le code postal a 5 chiffres du client')
CP_Client = input()
while len(CP_Client) < 5 or CP_Client.isdigit() == False :
       print("Le code postal est uniquement composé de chiffre,veuillez recommencer")
       CP_Client = None
       CP_Client = input()
        
print ('Veuillez entrer la ville du client')
Ville_Client = input()
print ('Veuillez entrer le téléphone du client')
Tel_Client = input()
print ('Veuillez entrer le mail du client')
Mail_Client = input()

ID_CO = pd.read_sql_query("select max(CO_ID) as Max from CONTRAT",engine)['Max'].values
ID_CL = pd.read_sql_query("select max(CL_ID) as Max from CLIENTS",engine)['Max'].values
id_co= ID_CO[0]
id_cl = ID_CL[0]
id_cl = 0 if not id_cl else id_cl
id_co = 0 if not id_co else id_co
id_cl +=1
id_co += 1
print(id_cl)
engine.execute('INSERT INTO CLIENTS (CL_ID,CL_NOM,CL_PRENOM,CL_ADRESSE,CL_CODEPOSTAL,CL_VILLE,CL_TEL,CL_MAIL,CL_CONTRAT_ID)'
               ' VALUES (%s,"%s","%s","%s","%s","%s","%s","%s","%s");'
               %(id_cl,Nom_Client,Prenom_Client,Adresse_Client,CP_Client,Ville_Client,Tel_Client,Mail_Client,id_co))
engine.execute('INSERT INTO CONTRAT (CO_ID,CO_DATE,CO_CATEGORIE,CO_BONUS,CO_MALUS)'
               ' VALUES  (%s,"%s","%s","%s","%s");' 
               %(id_co,Date_Contrat,Cat_Contrat,Bon_Contrat,Mal_Contrat))








