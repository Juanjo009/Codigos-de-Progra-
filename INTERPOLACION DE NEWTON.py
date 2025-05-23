# -*- coding: utf-8 -*-
"""
Juan Jose Lara Ruiz 
Programacion Numerica 
Tarea 6 
Interpolacion Numerica

"""

import numpy as np
import matplotlib.pyplot as plt

valores_x = np.array([2, 3, 5, 7, 8 ])
valores_y = np.array([6, 19, 99, 291, 444])

def coeficientes(x, y):
    n = len(x)
    coeficiente = np.copy(y).astype(float)
    for j in range(1, n):
        coeficiente[j:n] = (coeficiente[j:n] - coeficiente[j - 1:n - 1]) / (x[j:n] - x[0:n - j])
    return coeficiente

def evaluacion (x_eval, x_data, coef):
    n = len(coef)
    result = coeficiente[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x_eval - x_data[i]) + coeficiente[i]
    return result

coeficiente = coeficientes(valores_x, valores_y)
x_estimar = 4
f4 = evaluacion(x_estimar, valores_x, coeficiente)
print(f"f(4) Estimacion : {f4}")

x_line = np.linspace(1, 7, 300)
y_line = [evaluacion(x, valores_x, coeficiente) for x in x_line]

plt.plot(valores_x, valores_y, 'pink', label='Datos usados')
plt.plot(x_line, y_line, label='Interpolación Newton', color='black')
plt.plot(x_estimar, f4, 'o', label='f(4) calculado')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación de Newton')
plt.legend()
plt.show()