"""
Created on Sat Sep 23 19:02:25 2023

@author: Bren Guzmán
"""
#%% LIBRERÍAS
from Funciones import recommend
import pandas as pd

#%% CARGAR ARCHIVO
df = pd.read_excel('database.xlsx', index_col=None)
columnas = ['Title', 'Genres', 'Actor1', 'Actor2', 'Actor3', 'Director']
df = df[columnas]

#%% INTERFAZ DE USUARIO

while True:
    print("Welcome to movie recommender!")
    user_query = input("Enter your query (e.g. 'Horror movies'): ")
    num_recommendations = int(input("Number of recommendations to display: "))
    distance_type = input("Distance type ('cosine', 'jaccard'): ")

    recommend(user_query, df, distance_type, num_recommendations)

    another_query = input("\nDo you want to do another search? (y/n): ")
    if another_query.lower() != 'y':
        print("\nSee you soon! :)")
        break

