# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:34:38 2021

@author: issam
"""
import numpy as np
import matplotlib.pyplot as plt

# Exercice 1 : 
def S(n):
    X = np.random.uniform(0, 1,n)
    plt.plot(X)
    plt.show()
    return np.mean(X)

#Exercice 2 : 
def y(a):
    X=np.random.poisson(10)
    print("X = ", X)
    if X==a:
        return 1
    else : 
        return 0

def Esp(a,n):
    x=0
    for i in range(n):
        x+=y(a)
    return (1/n)*x
        
#Exercice 3 : 
    
def u(a) : 
    X=np.random.uniform(0,1)
    if X<a:
        return 1
    else : 
        return 0
def Espt(a):
    return a

def Esp1(a,n):
    x=0
    for i in range(n):
        x+=u(a)
    return (1/n)*x
    

  