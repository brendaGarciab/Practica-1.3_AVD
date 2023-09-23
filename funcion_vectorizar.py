# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:26:26 2023

@author: bg665
"""

## pip install numpy

### Funcion que recibe un vector y lo vectoriza 

import numpy as np

def vectorizar_secuencia(secuencia):
    
    # Función para vectorizar con NumPy
    
    # Args:
    # secuencia (iterable): La secuencia que se desea vectorizar

    
    vector = np.array(secuencia)
    return vector 


#%%
### Prueba de funcionamiento

#import numpy as np

#def vectorizar_secuencia(secuencia):
    #vector = np.array(secuencia)
    #return vector

# Prueba 1: Vectorizar una lista
lista = [1, 2, 3, 4, 5]
resultado = vectorizar_secuencia(lista)
print(resultado)

# Prueba 2: Vectorizar una tupla
tupla = (5, 4, 3, 2, 1)
resultado = vectorizar_secuencia(tupla)
print(resultado)

# Prueba 3: Vectorizar una cadena de texto
cadena = "Hola"
resultado = vectorizar_secuencia(cadena)
print(resultado)

# Prueba 4: Vectorizar una lista de flotantes
lista_flotantes = [0.1, 0.2, 0.3, 0.4, 0.5]
resultado = vectorizar_secuencia(lista_flotantes)
print(resultado)

# Prueba 5: Vectorizar una lista vacía
lista_vacia = []
resultado = vectorizar_secuencia(lista_vacia)
print(resultado)

# Prueba 6: Vectorizar una tupla de cadenas
tupla_cadenas = ("Python", "es", "genial")
resultado = vectorizar_secuencia(tupla_cadenas)
print(resultado)
