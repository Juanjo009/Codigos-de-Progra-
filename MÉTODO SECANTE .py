"""
Juan Jose Lara Ruiz 
Programación Numerica 
Tarea 2 
Método Secante 
 
"""
import matplotlib.pyplot as plt 
import numpy as np 

#funcion normal 

def fx(x): 
    return 8*x*np.sin(x)*(np.exp(-x))-1

def error_relativo (va,vn): 
    return np.abs((va-vn)/va)*100

xo=-0.3
xi1=0.5

num_iteraciones=5

for i in range (1,num_iteraciones+1):
    x_nueva=xo-(f(xo)*(xi1-x0)/(f(xi1)-f(x0)))
  print('===================================================\n')  
  print(f'i={i+1}| x_i= {x_nueva}')
    

x=np.linspace(-5,5,100)
plt.plot(x,fx(x))
plt.plot(xi ,fx(xi), 'oo')
plt.grid()
plt.show()    

 
    
    
    