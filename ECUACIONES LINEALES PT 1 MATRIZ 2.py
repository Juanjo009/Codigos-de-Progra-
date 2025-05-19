"""
Juan Jose Lara Ruiz 
Programacion Numerica 
Tarea 4 
Ecuaciones Lineales 

"""
import numpy as np

"""Solucion Gaussiana"""

#Variables del sistema de ecuaciones
A = np.array([[1, 1, 1],
              [1, 2, 5],
              [1, 4, 25]])

# Definir el vector de términos independientes b
b = np.array([6, 12, 36])

# Resolucion del sistema Ax = b
t = np.linalg.solve(A, b)

print("La solución es:", t)

"""Solucion Matriz Inversa """

# Definir la matriz de coeficientes A
A = np.array([[1, 1, 1],
              [1, 2, 5],
              [1, 4, 25]])

# Definir el vector de términos independientes b
b = np.array([6, 12, 36])

# Calcular la inversa de A
A_inv = np.linalg.inv(A)

# Multiplicar A_inv por b para obtener la solución
x = np.matmul(A_inv, b)

print("La matriz inversa de A es:")
print(A_inv)
print("La solución del sistema es:", x)



