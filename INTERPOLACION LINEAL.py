# -*- coding: utf-8 -*-
"""
Juan Jose Lara Ruiz 
Programacion Numerica 
Tarea 6 
Interpolacion Numerica 

"""
import numpy as np
import matplotlib.pyplot as plt

x0, x1 = 3,5
y0, y1 = 19,99

def interpolacion_lineal(x):
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

x_estimar = 4
f4 = interpolacion_lineal(x_estimar)
print(f"f(4) estimado (lineal): {f4}")

x_vals = np.array([x0, x1])
y_vals = np.array([y0, y1])
x_line = np.linspace(2.5, 5.5, 100)
y_line = interpolacion_lineal(x_line)

plt.plot(x_vals, y_vals, linestyle=':')
plt.plot(x_vals, y_vals, 'blue', label='Datos usados')
plt.plot(x_line, y_line, label='Interpolación lineal', color='orange')
plt.plot(x_estimar, f4, 'ro', label='f(4) calculado')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación Lineal')
plt.legend()
plt.show()
