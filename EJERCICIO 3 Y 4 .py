# -*- coding: utf-8 -*-
"""
Juan Jose Lara Ruiz
Programacion Numerica 
Ejercicio 3 Y 4 

"""

import numpy as np


m = 3
X = [np.random.randint(1, 6) for _ in range(m)]
print(f"Vector:{X}")
matriz = []
for i in range(m):
    fila = []
    for j in range(1, m + 1):
        fila.append(X[i] * j)
    matriz.append(fila)
print("Matriz:")
for fila in matriz:
    print(fila)

for fila in matriz:
    print(fila)

matriz2 = []
for i in range(m):
    fila = []
    for j in range(m):
        fila.append(X[j] * (i+1))
    matriz2.append(fila)
print("Matriz:")
for fila in matriz2:
    print(fila)


