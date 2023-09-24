# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:15:11 2023

@author: Bren Guzmán
"""
###LIBRERÍAS
import math
import numpy as np
#import pandas as pd

###DISTANCIA COSENO
def cosine_distance(vector1, vector2):
    # Calcula el producto punto de los vectores
    dot_product = sum(vector1[i] * vector2[i] for i in range(len(vector1)))

    # Calcula la magnitud de cada vector
    magnitude1 = math.sqrt(sum(x ** 2 for x in vector1))
    magnitude2 = math.sqrt(sum(x ** 2 for x in vector2))

    # Calcula la distancia de coseno
    similarity = dot_product / (magnitude1 * magnitude2)
    cosine_distance = 1 - similarity

    return cosine_distance

# Ejemplo de uso coseno
'''
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]

distance = cosine_distance(vector_a, vector_b)
print("Distancia de coseno entre los vectores:", distance)
'''

###DISTANCIA JACCARD
def jaccard_distance(vector1, vector2):
    intersection = np.sum(np.logical_and(vector1, vector2))
    union = np.sum(np.logical_or(vector1, vector2))
    jaccard_similarity = intersection / union
    jaccard_distance = 1 - jaccard_similarity
    return jaccard_distance

# Ejemplo de uso jaccard
'''
set_a = [1, 2, 3]
set_b = [4, 5, 6]

distance = jaccard_distance(set_a, set_b)
print("Distancia de Jaccard entre los conjuntos:", distance)
'''

###VECTORIZAR QUERY Y REGISTRO
def vectorize(query, df, record_index):
 
    # Obtener el registro específico del DataFrame en el índice dado
    record = df.iloc[record_index]
    query = query.lower()

    # Combinar las columnas relevantes en una sola cadena 
    
    #combined_text = str(record['Title']) + " " + str(record['Genres']) + " " + str(record['Actor1']) + " " + str(record['Actor2']) + " " + str(record['Actor3']) + " " + str(record['Director'])
    combined_text = str(record['Title']).lower() + " " + str(record['Genres']).lower() + " " + str(record['Actor1']).lower() + " " + str(record['Actor2']).lower() + " " + str(record['Actor3']).lower() + " " + str(record['Director']).lower()


    # Tokenizar la consulta del usuario y el registro
    query_tokens = query.split()
    record_tokens = combined_text.split()

    # Crear un conjunto de todas las palabras únicas en la consulta y el registro
    all_words = set(query_tokens).union(set(record_tokens))

    # Función para vectorizar un texto en función de las palabras únicas
    def vectorize_text(text_tokens, unique_words):
        vector = [1 if word in text_tokens else 0 for word in unique_words]
        return np.array(vector)

    # Vectorizar la consulta del usuario y el registro
    query_vector = vectorize_text(query_tokens, all_words)
    record_vector = vectorize_text(record_tokens, all_words)

    return query_vector, record_vector

# Ejemplo de vectorizar
'''
data = {'Title': ["Movie 1", "Movie 2", "Movie 3"],
        'Genres': ["action comedy romance", "comedy drama", "action adventure"],
        'Actor1': ["Chris Evans", "Tom Hiddleston", "Tom Ellis"],
        'Actor2': ["David Tennant", "Jeff Goldblum", "Richard Gere"],
        'Actor3': ["Ryan Reynolds", "Tom Cavanagh", "Penn Badgley"],
        'Director': ["Christopher Nolan", "Peter Jackson", "Martin Scorsese"]}
df = pd.DataFrame(data)

user_query = "I want a comedy with drama"
record_index = 2  # Índice del registro en el DataFrame

query_vector, record_vector = vectorize(user_query, df, record_index)
print("Vector de la consulta:", query_vector)
print("Vector del registro en el índice", record_index, ":", record_vector)
'''
