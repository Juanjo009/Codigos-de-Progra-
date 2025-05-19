# -*- coding: utf-8 -*-
"""
Juan José Lara Ruiz 
Programación Numerica
Tarea 4 
Ecuaciones Lineales

"""
import numpy as np 
 
"""Método Determinantes"""

# Definir la matriz A
A = np.array([[1, 2, 1],
              [3, 8, 1],
              [0, 4, 1]])

# Definir el vector b
b = np.array([2, 12, 2])

# Calcular el determinante de A
det_A = np.linalg.det(A)

if det_A == 0:
    print("El sistema no tiene solución única (det(A) = 0).")
else:
    # Inicializar la solución
    x = []

    # Iterar sobre cada columna de A
    for i in range(A.shape[1]):
        
        # Crear la matriz A_n reemplazando la columna i por el vector b
        A_i = np.copy(A)
        A_i[:, i] = b

        # Calcular el determinante de A_i
        det_A_i = np.linalg.det(A_i)

        # Calcular la solución para x_i
        x_i = det_A_i / det_A
        x.append(x_i)

    print("La solución del sistema es:\n", x)
    

"""Algoritmo de Doolittle para el método LU"""

L = np.zeros((3,3))
U = np.zeros((3,3))

#Elementos de la diagonal principal de L son unos

L[0][0] = 1
L[1][1] = 1
L[2][2] = 1

U[0,:] = A[0,:]

L[1][0] = A[1][0]/U[0][0]
U[1][1] = A[1][1]-L[1][0]*U[0][1]
U[1][2] = A[1][2]-L[1][0]*U[0][2]
L[2][0] = A[2][0]/U[0][0]
L[2][1] = (A[2][1]-L[2][0]*U[0][1])/U[1][1]
U[2][2] = (A[2][2]-L[2][0]*U[0][2])-L[2][1]*U[1][2]

# Mostrar resultados
print("\nMatriz L:")
print(L)
print("\nMatriz U:")
print(U)

# Comprobar resultados: A = L @ U
print("\nComprobación: L @ U:")
print(np.matmul(L, U))

"""Método Cholesky"""

print("\n Método Cholesky")

CH=np.zeros((3,3))
CH[0][0] = np.sqrt(A[0,0])
CH[1][0] = (A[1,0])/(CH[0,0])
CH[2][0] = (A[2,0])/(CH[0,0])
CH[1][1] = np.sqrt((A[1,1])-(CH[1,0]*CH[1,0]))
CH[2][1] = ((A[2,1])-(CH[1,0]*CH[2,0]))/(CH[1,1])
CH[2][2] = np.sqrt((A[2,2])-pow(CH[2,0],2)-pow(CH[2,1],2))

CHtrans= CH.T
print(CH)
print("\n",CHtrans)

"""Jacobi-Gauss Seidel"""

print("\nJacobi-Gauss Seidel")

# Matriz de coeficientes A
A = np.array([[1, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, -10]])

# Vector de términos independientes b
b = np.array([7.85, 19.3, 71.4])

# Función para calcular error relativo
def error(vr, vn):
    return abs((vr - vn) / vr) * 100

# Inicialización de variables
x1_v = 0
x2_v = 0
x3_v = 0
n_iter = 5

# Iteraciones
for k in range(1, n_iter + 1):
    x1 = (-A[0, 1] * x2_v - A[0, 2] * x3_v + b[0]) / A[0, 0]
    x2 = (-A[1, 0] * x1_v - A[1, 2] * x3_v + b[1]) / A[1, 1]
    x3 = (-A[2, 0] * x1_v - A[2, 1] * x2_v + b[2]) / A[2, 2]
    
    print(f"i={k} x1 = {x1:.4f} x2 = {x2:.4f} x3 = {x3:.4f}")
    
    # Cálculo de errores relativos
    print(f"error x1 = {error(x1, x1_v):.4f}, error x2 = {error(x2, x2_v):.4f}, error x3 = {error(x3, x3_v):.4f}")
    
    # Actualizar valores
    x1_v = x1
    x2_v = x2
    x3_v = x3

