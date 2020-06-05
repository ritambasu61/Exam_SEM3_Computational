#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:29:12 2020

@author: ritambasu
"""

import numpy as np
from matplotlib import pyplot as plt
#Problem10

def f(x):
    if abs(x)<1.0:
        return(1.0)
    return(0.0)    

 
#fourier transform through dft by using numpy.fft by using the progamming meterial taught in the class 
xmin=-5
xmax=5
numpoints=[512,1024,2048]
karr=[]
ft_arr=[]
for i in range(len(numpoints)):
    dx=(xmax-xmin)/(numpoints[i]-1)
    sampled_data=np.zeros(numpoints[i])
    xarr=np.zeros(numpoints[i])
    for j in range (numpoints[i]):
        sampled_data[j]=f(xmin+j*dx)
        xarr[j]=xmin+j*dx
    dft=np.real(np.fft.fft(sampled_data,norm='ortho'))
    k=2*np.pi*np.fft.fftfreq(numpoints[i],d=dx)
    factor=np.exp(-1j*k*xmin)
    ft=np.real(dx*np.sqrt(numpoints[i]/(2.0*np.pi))*factor*dft)
    karr.append(k)
    ft_arr.append(ft)
    #plt.plot(karr[i],ft_arr[i])

    
#plottings
plt.plot(karr[0],ft_arr[0],'r',label='ft for sample 1(512)')
plt.plot(karr[1],ft_arr[1],'b',label='ft for sample 2(1024)')
plt.plot(karr[2],ft_arr[2],'y',label='ft for sample 3(2048)')
plt.xlabel('x',fontsize=15)
plt.ylabel(r'$\tilde{f}$(k)',fontsize=15)
plt.legend(loc='best')
plt.show()
