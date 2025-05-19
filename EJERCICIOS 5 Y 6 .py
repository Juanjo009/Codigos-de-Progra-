# -*- coding: utf-8 -*-
"""
Juan Jose Lara Ruiz 
Programacion Numerica 
Ejercicios 5 y 6 

"""
import numpy as np 
import matplotlib.pyplot as mat 

m = 3
X = [np.random.randint(1, 6) for _ in range(m)]
print(f"Vector:{X}")
multiplos = []
for i in range(m):
    fila = []
    for j in range(1, m + 1):
        fila.append(X[i] * j)
    multiplos.append(fila)
print("Multiplos_columna(m):")
for fila in multiplos:
    print(fila)


multiplos = []
for i in range(m):
    fila = []
    for j in range(m):
        fila.append(X[j] * (i+1))
    multiplos.append(fila)
print("Multiplos_fila(m):")
for fila in multiplos:
    print(fila)

x = np.linspace(1*np.pi,2*np.pi,100)
t1 = np.cos(x)
t2 = np.sin(x)
t3 = np.tan(x)

mat.plot(x,t1, 'green',label='x**2')
mat.plot(x,t2, 'gray',label='sin(x)')
mat.plot(x,t3, 'blue',label='x**2')

mat.legend(loc='best')
mat.xlabel('eje x')
mat.ylabel('eje y')
mat.title('3 funciones')
mat.grid()
mat.show()