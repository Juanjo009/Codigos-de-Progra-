"""
Juan José Lara Ruiz 
Programación Numerica
Tarea 4 
Ecuaciones Lineales

"""
import numpy as np 
 
"""Método Determinantes"""

# Definir la matriz A
A = np.array([[1, 1, 1],
              [1, 2, 5],
              [1, 4, 25]])

# Definir el vector b
b = np.array([6, 12, 36])

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

""" Método Cholesky""" 

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

