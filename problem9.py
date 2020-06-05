#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:29:49 2020

@author: ritambasu
"""

import numpy as np


#defining a function for Singular value decomposition for m*n matrix
def svd(matrix,row,col):
    
    aTa=np.dot(np.transpose(matrix),matrix)
    aaT=np.dot(matrix,np.transpose(matrix))
    aTa_eig=np.linalg.eigh(aTa)
    aaT_eig=np.linalg.eigh(aaT)
 
    
    #constructing the diagonal D matrix
    D=np.zeros(min(row,col))
    minimum=min(row,col)
    if minimum==row:
        for i in range(minimum):
            D[i]=np.sqrt(aaT_eig[0][i])
    else:
        for i in range(minimum):
            D[i]=np.sqrt(aTa_eig[0][i])
    
    U=np.transpose(aaT_eig[1])
    
    VT=aTa_eig[1]
    return (U,D,VT)


#defing the matrix A
a1=np.array([[2,1],[1,0],[0,1]])#matrix 1 as a1
a2=np.array([[1,1,0],[1,0,1],[0,1,1]])#matrix 2 as a2


#printing my singular values for 1st matrix
u1,d1,vt1=svd(a1,3,2)
d1=np.sort(d1)#sorting to look good in printing
print ("Problem1:\nmy coded singular values of a1:\n",d1)
#comparing results with linalg.svt
U1,D1,V1=np.linalg.svd(a1)
D1=np.sort(D1)
print("numpy.linalg singular values of a1:\n",D1,"\n\nProblem2:")


#printing my singular values for 2nd matrix
u2,d2,vt2=svd(a2,3,3)
d2=np.sort(d2)#sorting to look good in printing
print ("my coded singular values of a1:\n",d2)
#comparing results with linalg.svt
U2,D2,V2=np.linalg.svd(a2)
D2=np.sort(D2)
print("numpy.linalg singular values of a1:\n",D2)





