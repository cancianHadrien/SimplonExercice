#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:38:58 2020

@author: simplon
"""
import pandas as pd
import sqlalchemy as db
import re
import numpy as np

engine = db.create_engine('mysql+pymysql://hadrien:H01011997C@localhost:3306/Netflix')
connection = engine.connect()

donnees = pd.read_csv('/home/simplon/Téléchargements/NETFLIX/netflix_titles.csv')
#print(donnees)

#EXO20
#donnees = pd.read_csv("netflix_titles.csv") #à rectifier par le chemin où se trouve votre fichier

#Suppression des doublons (en fonction de toutes les colonnes sauf index)
# 1 ligne en moins
# donnees = donnees.drop_duplicates(subset=donnees.columns[1:])

#Suppression des lignes ayant des valeurs indéfinies
# 2460 lignes en moins !!!!
# donnees = donnees.dropna()

# On crée le DataFrame show_listed en précisant ses colonnes
# Il sera utilisé à la fin de la partie 3 pour remplir la table côté MySQL 
# qui fait la liaison entre le catalogue et les catégories
# show_listed_in = pd.DataFrame(columns = ['sh_id','listed_in'])

# Pour chaque ligne (film ou série) i du DataFrame
# for i in donnees.index:
#     # On récupère toutes les catégories que l'on sépare dans une liste
#     categoriesFilm = donnees["listed_in"][i].split(", ") 
#     # On crée une liste de même longueur (len(categoriesFilm)) remplie par l'identifiant show_id
#     # ex pour créer une liste : ["toto"] * 3 crée la liste ["toto, "toto", "toto"]
#     idFilm = [donnees["sh_id"][i]] * len(categoriesFilm)
#     # On crée un Dataframe df temporaire qui fusionne les 2 listes qu'on vient de créer
#     df = pd.DataFrame({'sh_id': idFilm,'listed_in': categoriesFilm})
#     # On colle ce Dataframe temporaire à show-listed_in
#     show_listed_in = show_listed_in.append(df)
    
# # show_listed_in contient tous les DataFrames temporaires qu'on a créés à chaque ligne       
# show_listed_in 


# tmp2 = donnees.loc[donnees["listed_in"].notna()][['show_id', 'listed_in']]

# show_listed_in = pd.DataFrame(columns = ['show_id', 'listed_in'])


# for i in range(tmp2.shape[0]):
#     tmp = tmp2.iloc[i]["listed_in"].split(", ")
#     show_id = [tmp2.iloc[i]["show_id"]]*len(tmp)
#     df = pd.DataFrame({'sh_id': show_id,
#                     'listed_in': tmp}, columns = ['sh_id', 'listed_in'])
#     show_listed_in = show_listed_in.append(df, ignore_index=True)


#EXO21

# listed_in = show_listed_in['listed_in'].drop_duplicates().reset_index(drop=True).reset_index()
# listed_in = listed_in.rename(columns={"index": "listed_in_id"})
# show_listed_in = show_listed_in.merge(listed_in,
#                                       left_on='listed_in',
#                                       right_on='listed_in',
#                                       how='left')
# del show_listed_in['listed_in']




#EXO22


# tmp2 = donnees.loc[donnees["director"].notna()][['show_id', 'director']]

# show_director = pd.DataFrame(columns = ['show_id', 'director'])


# for i in range(tmp2.shape[0]):
#     tmp = tmp2.iloc[i]["director"].split(", ")
#     show_id = [tmp2.iloc[i]["show_id"]]*len(tmp)
#     df = pd.DataFrame({'show_id': show_id,
#                     'director': tmp}, columns = ['show_id', 'director'])
#     show_director = show_director.append(df, ignore_index=True)

# director = show_director['director'].drop_duplicates().reset_index(drop=True).reset_index()
# director = director.rename(columns={"index": "director_id"})
# show_director = show_director.merge(director,
#                                       left_on='director',
#                                       right_on='director',
#                                       how='left')

# del donnees['director']
# print(show_director)

# tmp2 = donnees.loc[donnees["cast"].notna()][['show_id', 'cast']]
# show_cast = pd.DataFrame(columns = ['show_id', 'cast'])
# for i in range(tmp2.shape[0]):
#     tmp = tmp2.iloc[i]["cast"].split(", ")
#     show_id = [tmp2.iloc[i]["show_id"]]*len(tmp)
#     df = pd.DataFrame({'show_id': show_id,
#                     'cast': tmp}, columns = ['show_id', 'cast'])
#     show_cast = show_cast.append(df, ignore_index=True)

# cast = show_cast['cast'].drop_duplicates().reset_index(drop=True).reset_index()
# cast = cast.rename(columns={"index": "cast_id"})
# show_cast = show_cast.merge(cast,
#                                       left_on='cast',
#                                       right_on='cast',
#                                       how='left')

# del donnees['cast']
# print(show_cast)


#EXO 23



engine.execute("SET FOREIGN_KEY_CHECKS=0;")
engine.execute("TRUNCATE catalog;")
engine.execute("TRUNCATE catalog_country;")
engine.execute("TRUNCATE Country;")
engine.execute("TRUNCATE catalog_category;")
engine.execute("TRUNCATE category;")
engine.execute("TRUNCATE catalog_actor;")
engine.execute("TRUNCATE actor;")
engine.execute("TRUNCATE catalog_director;")
engine.execute("TRUNCATE director;")
engine.execute("SET FOREIGN_KEY_CHECKS=1;")

def getTableData(colFilter, valNameDefault, newValName, colNameID, insertIntoTblNames):
    # Intialisation des variables
    dataFramesLst = []
    data_filtered = donnees[colFilter]
    data_filtered = donnees.loc[donnees[valNameDefault].notna()][colFilter]
    colNameFirst, colNameSecond = [], []
    # On parcour toutes les lignes
    for index, row in data_filtered.iterrows():
        for subdata in row[1].split(", "):
            if not re.search(r',$', subdata):
                colNameFirst.append(row[0])
                colNameSecond.append(subdata)
    # Premier DataFrame
    firstDFtmp = pd.DataFrame({colFilter[0]: colNameFirst, colFilter[1]: colNameSecond}, columns = colFilter)
    firstDFtmp = firstDFtmp.rename(columns={valNameDefault:newValName, 'show_id':'catalog_id'})
    firstDF = firstDFtmp.drop(columns='catalog_id').drop_duplicates()
    firstDF.index = np.arange(1,len(firstDF)+1)
    # Deuxieme DataFrame
    secondDF = firstDFtmp[newValName].drop_duplicates().reset_index(drop=True).reset_index().rename(columns={'index':colNameID})
    secondDF[colNameID] = np.arange(1,len(secondDF)+1)
    secondDF = secondDF.merge(firstDFtmp, on=newValName, how='left').drop(columns=[newValName])
    # Ajout des données dans les 2 tables
    firstDF.to_sql(insertIntoTblNames[0], con=engine, index = False, if_exists = 'append')
    secondDF.drop_duplicates().to_sql(insertIntoTblNames[1], con=engine, index = False, if_exists = 'append')


# Catalog
data_catalog = donnees.drop(columns=['listed_in', 'country', 'cast', 'director']).rename(columns={'show_id':'catalog_show_id', 'type':'catalog_type', 'title':'catalog_title', 'date_added':'catalog_date_added', 'rating':'catalog_rating', 'release_year':'catalog_release_year', 'duration':'catalog_duration', 'description':'catalog_description'})
data_catalog["catalog_date_added"] = pd.to_datetime(donnees["date_added"])
data_catalog = data_catalog.replace({'catalog_duration' : { ' min' : '', ' Seasons' : '', ' Season' : '' }}, regex=True)
data_catalog.to_sql('catalog', con=engine, index = False, if_exists = 'append')
# Category
category = getTableData(["show_id", "listed_in"], "listed_in", "category_name", "category_id", ["category", "catalog_category"])
# Country
country = getTableData(["show_id", "country"], "country", "country_name", "country_id", ["country", "catalog_country"])
# Actor
actor = getTableData(["show_id", "cast"], "cast", "actor_name", "actor_id", ["actor", "catalog_actor"])
# Director
director = getTableData(["show_id", "director"], "director", "director_name", "director_id", ["director", "catalog_director"])
