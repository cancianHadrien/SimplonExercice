#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:16:21 2020

@author: simplon
"""


import pandas as pd
import re
import seaborn as sns
# EXO 1

# donnee = pd.read_csv('/home/simplon/Téléchargements/NETFLIX/netflix_titles.csv',
#                       index_col = 0)
# print(donnee.head())

#EXO 2

# print(donnee.shape)

#EXO 3

# film = donnee.loc[donnee["type"]=="Movie"]
# serie = donnee.loc[donnee["type"]=="TV Show"]

# print(film.type.value_counts())
# print(serie.type.value_counts())

#EXO 4

# print(donnee.describe(include = 'all'))

#EXO5
# print(donnee.isna().sum())

#EXO 6 A

# director = donnee.loc[donnee['director'].isna()]
# print(director)
# film =director.loc[director['type']=='Movie']
# series = director.loc[director['type']=='TV Show']
# print(film.type.value_counts())

# print(series.type.value_counts())

#EXO 6 B

# cast = donnee.loc[donnee['cast'].isna()]
# print(cast)
# print(cast.listed_in.value_counts().head(10))

#EXO 7

# double = donnee.duplicated()
# print(double)
# remove = donnee.drop_duplicates()
# print(remove)

# EXO 8

# France =  donnee.loc[donnee['country']=="France" ]
# USA = donnee.loc[donnee["country"]=="United States"]
# print(USA)
# print(France.shape,USA.shape)

#EXO 9

# year = donnee.release_year.min()
# print(year)
# print(donnee['title'].loc[donnee['release_year'] == year])

#EXO 10

# film = donnee.loc[donnee["type"]=="Movie"]
# duree = film.duration.astype("string")
# duree = duree.str.replace("min"," ")
# duree = duree.astype('int').sort_values(ascending = False)
# print(duree.head(5))

# film = film.join(duree,on = 'show_id',lsuffix ='_right')
# film = film.sort_values(by= 'duration',ascending = False).head(5)
# print(film['title'])

#EXO 11
# categories=pd.Series(", ".join(donnee["listed_in"].dropna()).split(", "))
# print(categories.value_counts().head())

#partie graphique (partie2 exo Netflix)

#EXO 12 

# director=pd.Series(", ".join(donnee["director"].dropna()).split(", "))
# print(director.value_counts().head(10))

#EXO 13
# director = donnee.loc[donnee['director'].notna()]
# print(director)
# donnee_jan_suter =director[director['director'].str.contains('Jan Suter')]
# print(donnee_jan_suter)
# cast = pd.Series(", ".join(donnee_jan_suter['cast']).split(','))
# print(cast.value_counts().head(5))

#EXO 14

# pays = donnee[donnee['country'].notna()]
# top = pd.Series(','.join(pays['country']).split(','))
# top = top.value_counts().head(10)
# print(top)
# topPays=pays[pays['country'].isin(top.index)]
# print(topPays)

# sns.set_style("darkgrid")
# sns.countplot(data = topPays,x='country')

#EXO 15

# sns.set_style('darkgrid')
# sns.countplot(data = donnee,x='rating')

#EXO 16

# donnee["year_added"]=pd.to_datetime(donnee["date_added"]).dt.year
# print(donnee['year_added'].dropna().astype('int'))
# print(donnee.columns)
# count = donnee.groupby(['type','year_added']).size().reset_index().rename(columns ={0:'Count'})
# sns.set_style('darkgrid')
# sns.pointplot(data = count,x='year_added',y='Count',hue = 'type')

#EXO 17 duration
# film = donnee[donnee['type']=='Movie']
# print(film)
# duree = film.duration.astype('string').str.replace('min',' ').astype('int')
# print(duree)

# sns.set_style("darkgrid")
# sns.distplot(duree)

#EXO 18
# serie = donnee[donnee['type']=='TV Show']
# print(serie['duration'])
# saison = serie.duration.astype('string').str.replace('[a-zA-Z]+',' ').astype('int')
# print(saison)
# serie = serie.join(saison,on = 'show_id',lsuffix ='_right')
# sns.set_style("darkgrid")
# sns.countplot(data = serie,x = 'duration')


