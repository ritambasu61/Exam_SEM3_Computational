#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:20:05 2020

@author: ritambasu
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x,r): # r is an array with r[0]=y and r[1]=z(=dy/dx)
   dydx=r[1]
   dzdx=4*(r[0]-x)
   return np.array([dydx,dzdx])

#defining exact solution
def f_exact(x):
    return((np.e)**2/((np.e)**4-1)*(np.exp(2*x)-np.exp(-2*x))+x)
    

candidate_sol=[] # candidate solutions for different v's as it's element 
y_vf=[] # stores the y(x_f) for different y'[0]=v guesses
initial_value_of_x=0
final_value_of_x=1
rel_error=[]



for v in np.arange(-5,5,0.05):
    trial_sol_for_particular_v=[]
    rel_error_for_particular_v=[]
    r=np.array([0.0,v])  # initial values y[0]=0,and y'[0]=v
    h=0.01
    x=initial_value_of_x 
    x_f=final_value_of_x
    x_sol=[]
    while x<=x_f+h:
       trial_sol_for_particular_v.append(r[0]) 
       x_sol.append(x)
       k1=h*f(x,r)
       k2=h*f(x+0.5*h,r+0.5*k1)
       k3=h*f(x+0.5*h,r+0.5*k2)
       k4=h*f(x+h,r+k3)
       r=r+(k1+2*k2+2*k3+k4)/6.0
       x=x+h
       rel_error_for_particular_v.append(abs(r[0]-f_exact(x))/f_exact(x))

    y_vf.append(r[0])
    rel_error.append(rel_error_for_particular_v)  
    candidate_sol.append(trial_sol_for_particular_v)
y_vf=np.array(y_vf)#array for v at final points    
x_sol=np.array(x_sol)


"""comparision between y(xf=1) for differentv's  
w.r.t to y(xf=1)=2 given in the problem """
index_of_min=np.argmin(abs(y_vf - 2))


#plotting_of the _numerically calculated solution
plt.plot(x_sol,candidate_sol[index_of_min],
           color='Red', marker='o',markersize=0.5,label="numerical solution")

#exct solution plotting
plt.plot(x_sol,f_exact(x_sol),color='Black',label="exact solution")


#percentage error plotting
plt.plot(x_sol,rel_error[index_of_min],ls='dashed',color='orange', marker='o',markersize=4,label="persentage relative error")


plt.xlabel('x',fontsize=15)
plt.ylabel('y(x)',fontsize=15)
plt.title('Solution by shotting Method',fontsize=20)
plt.legend(loc='best')
plt.show()