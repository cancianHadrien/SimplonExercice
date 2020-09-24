#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:42:31 2020

@author: simplon
"""


from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from sqlalchemy import create_engine
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

engine = create_engine("mysql+pymysql://hadrien:H01011997C@localhost/netflix")

TMPL_DIR = "/home/simplon/Exercices/SimplonExercice/NetlfixDashboard/tmpl"
fichier = "rapport.jinja"

templateLoader = FileSystemLoader(searchpath=TMPL_DIR)
templateEnv=Environment(loader = templateLoader)
template = templateEnv.get_template(fichier)

SQL_Query5 = pd.read_sql_query("select dir_name from directors;",engine)
max_id = SQL_Query5.shape[0]-1
max_id = str(max_id)
print("Veuillez choisir un nombre entre 0 et "+max_id)
id = int(input())
nom = '"'+SQL_Query5.loc[id]['dir_name']+'"'
print(nom)

SQL_Query = pd.read_sql_query("Select count(ca_title) as nombre_film,category.cat_name as categories "
                              "from catalogue join catalogue_directors "
                              "on catalogue.ca_id = catalogue_directors.ca_id "
                             "join directors on catalogue_directors.dir_id= "
                             "directors.dir_id join catalogue_category on "
                             "catalogue_category.ca_id = catalogue.ca_id "
                             "join category on catalogue_category.cat_id "
                             "= category.cat_id where dir_name ="+nom+""
                             "group by categories; ",engine)
print(SQL_Query)
SQL_Query2 = pd.read_sql_query("Select ca_title,category.cat_name as categories  from catalogue "
                               "join catalogue_directors on catalogue.ca_id = "
                               "catalogue_directors.ca_id join directors on "
                               "catalogue_directors.dir_id= directors.dir_id "
                               "join catalogue_category on catalogue_category.ca_id = catalogue.ca_id "
                               "join category on catalogue_category.cat_id = category.cat_id "
                               "where directors.dir_name = "+nom+" order by ca_title,categories;",engine)

SQL_Query3 = pd.read_sql_query("Select count(ca_title) as nombre_film,ca_rating as rating from catalogue "
                               "join catalogue_directors on catalogue.ca_id = "
                               "catalogue_directors.ca_id join directors on "
                               "catalogue_directors.dir_id= directors.dir_id "
                               "where directors.dir_name = "+nom+""
                               "group by ca_rating;",engine)

SQL_Query4 = pd.read_sql_query("Select count(ca_title) as nombre_film,category.cat_name as categories "
                              "from catalogue join catalogue_category on "
                              "catalogue_category.ca_id = catalogue.ca_id "
                              "join category on catalogue_category.cat_id = category.cat_id"
                              " group by categories",engine)

SQL_Query6 = pd.read_sql_query("Select count(ca_title) as nombre_film,year(ca_date) as date_ajout "
                               "from catalogue group by date_ajout;",engine)
sns.lineplot(data = SQL_Query6,x = 'date_ajout',y='nombre_film')
plt.savefig("/home/simplon/Exercices/SimplonExercice/NetlfixDashboard/HistoriqueFrequenceFilm.png",format="png")
sns.catplot(
    data=SQL_Query, kind ='bar',
    x = 'nombre_film',y = 'categories',
     )
plt.savefig("/home/simplon/Exercices/SimplonExercice/NetlfixDashboard/categories.png",format ="png")
sns.catplot(
    data=SQL_Query3, kind ='bar',
    x = 'rating',y = 'nombre_film',
     )
plt.savefig("/home/simplon/Exercices/SimplonExercice/NetlfixDashboard/rating.png",format ="png")
sns.catplot(
    data=SQL_Query4, kind ='bar',
    x = 'nombre_film',y = 'categories'
     )

img_path = "/home/simplon/Exercices/SimplonExercice/NetlfixDashboard/categories.png"
img_path2 = "/home/simplon/Exercices/SimplonExercice/NetlfixDashboard/rating.png"
img_path3 = "/home/simplon/Exercices/SimplonExercice/NetlfixDashboard/nbr_categories.png"
img_path4 = "/home/simplon/Exercices/SimplonExercice/NetlfixDashboard/HistoriqueFrequenceFilm.png"
data ={
       'nom':nom,
       'films_dir': SQL_Query2,
       'img src':img_path,
       'img src':img_path2,
       'img src':img_path3,
       'img src':img_path4
       }

print(template.render( data ))


outputText = template.render(data)
html_file = open('/home/simplon/Exercices/SimplonExercice/NetlfixDashboard/tmplindex.html','w')
html_file.write(outputText)
html_file.close()
