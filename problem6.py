#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:37:36 2020

@author: ritambasu
"""

import matplotlib.pyplot as plt
from scipy.integrate import odeint 
import numpy as np


"""Here we have used the vector methodto to solve simaltenious differential equations"""

#defining initial values 
y10=1/3
y20=1/3



#defining the vector function f(t,y)
def f(y,x): # y is an array with y[0]=y1(t),y[1]=y2(t)
   f0=32*y[0]+(66*y[1])+(2/3*x)+2/3#dy1dx
   f1=-66*y[0]-(133*y[1])-(1/3*x)-1/3#dy2dx
   return np.array([f0,f1])

y=np.array([y10,y20])  # initial values of vector y

#argument that my code is fine
"""though the equations are stiff in nature but if I use h to be small then 
    RK4 works perfectly fine. This can coded more accurately if we can use euler
    backword integration method"""

h=0.01#choosing h to match the analytical solution
y1=[]
y2=[]

x_arr=[]
x=0 # initial value of x
while x<=0.5+h:
    y1.append(y[0])
    y2.append(y[1])
    x_arr.append(x)
    k1=h*f(y,x)
    k2=h*f(y+0.5*k1,x+0.5*h)
    k3=h*f(y+0.5*k2,x+0.5*h)
    k4=h*f(y+k3,x+h)
    y=y+(k1+2*k2+2*k3+k4)/6.0
    x=x+h

x_arr=np.array(x_arr)

#solving ode by scipy
y0=np.array([y10,y20])  # initial values of vector y
x_num=np.linspace(0.0,0.5,100)
y_num=odeint(f,y0,x_num)
y1_num=y_num[:,0]
y2_num=y_num[:,1]

#plotting scipy solutions
plt.scatter(x_num,y1_num,color='Yellow',marker='^',s=15,label="scipy y1(t)")
plt.scatter(x_num,y2_num,color='Orange',marker='^',s=15,label="scipy y2(t)")

#comparison of actual solution with computed solution through plotting  
plt.plot(x_arr,y1,label="numerical y1(t)")
plt.plot(x_arr,y2,label="numerical y2(t)")

#plotting exact solutions calculated by using mathematica
plt.scatter(x_arr,1/3*(2*x_arr-np.exp(-100*x_arr)+2*np.exp(-x_arr)),color='Red', marker='o',s=10,label="Exact y1(t)")
plt.scatter(x_arr,1/3*(-x_arr+2*np.exp(-100*x_arr)-np.exp(-x_arr)),color='Black', marker='o',s=10,label="Exact y2(t)")

plt.xlabel('t',fontsize=16)
plt.ylabel('y(t)',fontsize=16)
plt.title('Solving simaltenious differential equations',fontsize=20)
plt.legend(loc='best')
plt.show()

