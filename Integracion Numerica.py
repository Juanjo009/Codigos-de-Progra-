# -*- coding: utf-8 -*-
"""

Juan Jose Lara Ruiz 
Programacion Numerica 
Tarea 5 Derivacion numerica 
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from sympy import symbols, integrate 

f1 = lambda x: 2*np.cos(2*x)
f2 = lambda x: -x**2-x/2+4
f3 = lambda x: np.exp(-x**2)  

a = [0,1,0]
b = [np.pi/4,1,1]
funciones = [f1,f2,f3]

def simpson_13(f,a,b):
    x1 = (b-a)/2
    I = (b-a)*((f(a)+4*f(x1)+f(b))/6)
    return round(I,4)

print('   Valores analíticos    ')
x_sim = symbols('x')

for funcion in funciones:
    print(f'El valor de la integral de la función es {integrate(funcion(x_sim),x_sim)}')

print('    Valores Simpson    \n')

for i in range(len(a)):
    print(f'La integral de la función {i} en simpson 1/3 es: {simpson_13(funciones[i],a[i],b[i])}')