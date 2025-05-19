# -*- coding: utf-8 -*-
"""
Juan José Lara Ruiz 
Programacion Numerica 
Método biseccion 

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
xr=-2.1913

num_iteraciones=5

for i in range (1,num_iteraciones+1): 
    a_viejo=a
    b_viejo=b
    xi=(a+b)/2
    fa=fx(xi)
    fb=fx(b)
    fxi=fx(xi)
    if fa*fxi<0: 
        b=xi 
    else: 
        a=xi
    print('==================================================\n')
    print(f'i={i}) | a={a} | b={b} | xi={xi} | error={error_relativo(xr,xi)}')
    
    

x=np.linspace(-5,5,100)
plt.plot(x,fx(x))
plt.plot(xi ,fx(xi), 'go')
plt.grid()
plt.show()    
    
