#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:38:58 2020

@author: simplon
"""
import pandas as pd
donnees = pd.read_csv('/home/simplon/Téléchargements/Netflix/netflix_titles.csv')
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

from sqlalchemy import create_engine

df = pd.read_csv("/home/simplon/Téléchargements/Netflix/netflix_titles.csv")
engine = create_engine('mysql+pymysql://hadrien:H01011997C@localhost:3306/netflix')

#df=id/categorie
cat_name = pd.DataFrame(data = df,columns = ["ca_id", "cat_name"])
cat_name.drop_duplicates().dropna(inplace=True)


#df=id/cast
cast = pd.DataFrame(data = df,columns = ["ca_id", "cast_name"])
cast.dropna(inplace=True)


#df=id/director
directors = pd.DataFrame(data = df,columns = ["ca_id", "dir_name"])
directors.dropna(inplace=True)

#df=id/country
country = pd.DataFrame(data = df,columns = ["ca_id", "co_name"])
country.dropna(inplace=True)

#fonction split 
def separator(id, column, column_name):
    c = 0
    liste_id = []
    liste_col = []
    for i in column:
        x = i.split(", ")
        for z in x:
            liste_col.append(z)
            liste_id.append(id[c])
        
        c+=1
    dataframe = pd.DataFrame({'ca_id':liste_id, column_name: liste_col}, columns = ['ca_id', column_name])
    return dataframe 





#dataframe id/catégories
cat_id=separator(cat_name['ca_id'], cat_name['cat_name'], 'cat_name')
#dataframe id/cast
cast_id=separator(cat_name['ca_id'], cast['cast_name'], 'cast_name')
#dataframe id/directors
dir_id=separator(cat_name['ca_id'], directors['dir_name'], 'dir_name')
#dataframe id/country
country_id=separator(cat_name['ca_id'], country['co_name'], 'co_name')


def table(df, column ,id): #formatage table
    data = df.drop_duplicates(subset=[column]).reset_index().rename(columns={"index": id})
    del data['ca_id']
    print(data)
    return data

def associationTable(df_base, df, column ,id): #formatage table association
    data= df.merge(df_base, left_on=column, right_on= column)
    data = data.rename(columns={"ca_id_x": "ca_id"})
    del data[column]
    print(data)
    return data


#table categorie catalogue
categories = table(cat_id, "cat_name", "cat_id")
cat_categories = associationTable(categories, cat_id, "cat_name", "cat_id")

#table country catalogue
country = table(country_id, "co_name", "co_id")
cat_country = associationTable(country, country_id, "co_name", "co_id")

#table cast catalogue
cast = table(cast_id, "cast_name", "cast_id")
cat_cast = associationTable(cast, cast_id, "cast_name", "cast_id")

#table dir catalogue

dir = table(dir_id, "dir_name", "dir_id")
cat_dir = associationTable(dir, dir_id, "dir_name", "dir_id")


#table catalogue
del df['cat_name']
del df['dir_name']
del df['cast_name']
del df['co_name']
del df['Unnamed: 12']



#changement type durée et date ajout

df['ca_duration'] = df['ca_duration'].str.replace(" min", "").str.replace(" Season", "").str.replace(" season", "").str.replace("s", "").astype(int)
df['ca_date']=pd.to_datetime(df['ca_date'])



#insertion tables

df.to_sql('catalogue', con=engine, if_exists='append', index=False)
country.to_sql('country', con=engine, if_exists='append', index=False)
cast.to_sql('cast', con=engine, if_exists='append', index=False)
dir.to_sql('directors', con=engine, if_exists='append', index=False)
categories.to_sql('category', con=engine, if_exists='append', index=False)


#insertion tables d'association

cat_country.to_sql('catalogue_country', con=engine, if_exists='append', index=False)
cat_cast.to_sql('catalogue_cast', con=engine, if_exists='append', index=False)
cat_dir.to_sql('catalogue_directors', con=engine, if_exists='append', index=False)
cat_categories.to_sql('catalogue_category', con=engine, if_exists='append', index=False)






