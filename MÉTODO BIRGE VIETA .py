# -*- coding: utf-8 -*-
"""
Juan José Lara Ruiz 
Programación Numerica
Tarea 3 
Método Birge-Vieta

"""
import numpy as np
import matplotlib.pyplot as plt 

def fx(x): 
    return x**3 - 5*x**2 + 5*x - 1

def error_relativo (va,vn): 
    return np.abs((va-vn)/va)*100

a=np.array ([1,-5,5,-1])
x_i = 0.8

b = np.empty(len(a))
c = np.empty(len(a))

num_itera = 10 
n = len(a)

for i in range(1,num_itera+1): 
    for j in range(n): 
        if j==0:
            b[j] = a[j]
            c[j] = a[j]
            
        else:
            b[j] = a[j]+ x_i*b[j-1]
            c[j] = b[j]+ x_i*c[j-1]
            
        x_i_viejo = x_i 
            
    x_i = x_i - (b[n-1]/c[n-2])
        
    print (f'Iteracion: {i} \n')
    print (f'xi = {x_i_viejo}')   
    print (b)
    print (c)
        
x=np.linspace(-5,5,100)
plt.plot(x,fx(x))
plt.plot(x,fx(x), 'go')
plt.grid()
plt.show()

