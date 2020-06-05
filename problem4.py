#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:09:29 2020

@author: ritambasu
"""

import numpy as np
from matplotlib import pyplot as plt



sampled_data=np.random.uniform(0,1,1024)
 
#fourier transform through dft by using numpy.fft.fft 
xmin=0
dx=1
numpoints=len(sampled_data)
dft=np.fft.fft(sampled_data,n=numpoints,norm='ortho')
k=2*np.pi*np.fft.fftfreq(numpoints,d=dx)


"""Now the following process for convoluting R i.e
correlation fuction by convolution sampled data function with itself using
numpy.Though the same code can be use for conlvolution as spcified in problem 9"""


#Q(b) power spectrum computation_through convolution of corelation funtion R

#defining frequency array kq to plot dft w.r.t it
kq=np.fft.fftfreq(numpoints,dx)

#defining fourier transformed variable say(k) corresponding to data points say(x)
k=2*np.pi*kq
factor1=np.exp(-1j*k*xmin)

#Defining corelation function using Periodogram estimator
R=np.convolve(sampled_data,sampled_data,'same')/(2*numpoints) 

#Defining power spectrum to be forier transform of the correlation function
Power=np.abs(dx*np.sqrt(numpoints/(2.0*np.pi))*factor1*np.fft.fft(R,norm='ortho'))



#Q(a)
#plotting of sampled data
step_arr=np.arange(0,numpoints,1)
plt.scatter(step_arr,sampled_data)
plt.xlabel('step',fontsize=16)
plt.ylabel('sampled function value',fontsize=16)
plt.show()


#plotting of power spectrum
plt.plot(k,Power)
plt.title('Power Spectrum ',fontsize=15)
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'Power spectrum',fontsize=16)
plt.show()

#plotting the power spectrum bins
plt.hist(Power,bins=5,histtype='bar') 
plt.title('Actual Binned power spectrum ',fontsize=15)
plt.xlabel(r'Power spectrum',fontsize=16)
plt.ylabel(r'Occurance',fontsize=16)
plt.show()



#Q(d)
'''This plot is correct because this like the fourier transform of 
constant function and as we can assume that this numpy.random.uniform generates 
uniformly distributed random numbers in a certain range so it's pdf or sampled data 
also behaves as a PDF of a constant function. So my plots are correct upto a constant factor.'''
#Q(c)
print("Maximum value of k=",max(k),"\nMinimum value of k=",min(k))#these are close to pi
             