# -*- coding: utf-8 -*
"""
Juan Jose Lara Ruiz
Programacion Numerica 
Ejercicio 1 Y 2 

"""

import numpy as np

m = 4.5

if not isinstance(m, int):
    print("No es un número entero")
elif m <= 0:
    print("Es un número positivo")
else:
    print("Es un número entero positivo")
    X = [np.random.randint(1, 9) for _ in range(m)]
    print(f"Vector: {X}")