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
