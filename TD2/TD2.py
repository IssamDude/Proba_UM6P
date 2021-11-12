# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:22:11 2021

@author: issam
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rd
import math

#Exercice 2 : 
    
def Uni(a,b) : 
    return rd.uniform(a,b)

def T():
    U=Uni(0,1)
    if U<0.3 : 
        t=3
    elif U>=0.3 and U<0.5 :
        t=4
    else : 
        t=7
    return t
    
def algo():
    k=1
    n=0
    while (k<=6):
        t=T()
        if t==4 : 
            k+=1
            n+=1
        else :
            n+=1
    return n
        
#Exercice 3 :

def T2(x, n) : 
    
    k=0
    for i in range (n) : 
        u=Uni(0,1)
        v=Uni(0,1)
        if (u<x) and (v<x) : 
            k+=1
        else : 
            pass
           
    return k, (x**2)*n

def T3(x, n) : 
    
    k=0
    for i in range (n) : 
        u=Uni(0,1)
        v=Uni(0,1)
        if (u>x) and (v>x) : 
            k+=1
        else : 
            pass
           
    return k, ((1-x)**2)*n

fdfd
    