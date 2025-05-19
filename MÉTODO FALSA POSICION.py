# -*- coding: utf-8 -*-
"""
Juan José Lara Ruiz 
Programación Numerica
Tarea 3 
Método Falsa Posicion

"""

import matplotlib.pyplot as plt 
import numpy as np 

#funcion normal 
def fx(x): 
    return 2*x*np.cos(2*x)-(x+1)**2

def error_relativo (va,vn): 
    return np.abs((va-vn)/va)*100

a=-3
b=-2
xn=-2.1913

num_iteraciones=5

for i in range (num_iteraciones): 
    p1=fx(a)
    p2=fx(b)
    xi=b-((p2*(a-b))/(p1-p2))
    p3=fx(xi)
    if p1*p3<0: 
        b=xi 
    else: 
        a=xi
    print('=======================================================================================================================\n')
    print(f'i={i+1}) | f(a)={p1} | fx(b)={p2} | a={a} |  b={b}  |  xi={xi} | error={error_relativo(xn,xi)}')
    

x=np.linspace(-5,5,100)
plt.plot(x,fx(x))
plt.plot(xi ,fx(xi), 'go')
plt.grid()
plt.show()    
    
