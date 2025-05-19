# -*- coding: utf-8 -*-
"""
Juan Jose Lara Ruiz 
Programacion Numerica 
Tarea 2 
Método Newton-Raphson
 
"""
import matplotlib.pyplot as plt 
import numpy as np 

#funcion normal 

def fx(x): 
    return 8*x*np.sin(x)*(np.exp(-x))-1

def f2(x): 
    return 8 *np.exp(-x) *(np.sin(x) + x*np.cos(x)-x*np.sin(x))

def error_relativo (va,vn): 
    return np.abs((va-vn)/va)*100

xi=0.3


num_iteraciones=5
xv = xi

for i in range (1,num_iteraciones+1): 
  xn= xi - fx(xi)/f2(xi)
  print('====================================================================\n')
  print(f'i={i}  | xi={xi} | error={error_relativo(xn,xv)}')
  
  xv=xn

    

x=np.linspace(-5,5,100)
plt.plot(x,fx(x))
plt.plot(xi ,fx(xi), 'bo')
plt.grid()
plt.show()    
