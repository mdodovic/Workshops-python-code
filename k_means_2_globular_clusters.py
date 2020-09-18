# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:17:16 2018

@author: matij
"""

import numpy as np
import matplotlib.pyplot as plt


u, g, r, i, z, Sk = np.loadtxt('sdss_colors.csv',delimiter = ',', unpack = True)

N = len(u)
xRaz = np.zeros(N)
yRaz = np.zeros(N)

for i in range(N):
    xRaz[i] = u[i] - g[i]
    yRaz[i] = g[i] - r[i]

plt.scatter(xRaz, yRaz, s=0.005, c='black')
plt.xlim(-0.5,2.5)
plt.ylim(-0.5,1.5)
plt.xlabel("$u-g$")
plt.ylabel("$g-r$")
plt.savefig("iteracija_0", dpi = 300)    

plt.show()

def rast(x1,y1,x2,y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def cm(K):
    N = len(K)
    sx1 = 0
    sy1 = 0
    sx2 = 0
    sy2 = 0
    br1 = 0
    br2 = 0
    for i in range(N):
        if K[i] == 1:
            sx1 += xRaz[i]
            sy1 += yRaz[i]
            br1 += 1
        if K[i] == 2:
            sx2 += xRaz[i]
            sy2 += yRaz[i]
            br2 += 1
    
    return sx1/br1, sy1/br1, sx2/br2, sy2/br2

def plot(K, num):
    N = len(K)
    b1 = 0
    b2 = 0
    for i in range(N):
        if K[i] == 1:
            b1 += 1
        
        if K[i] == 2:
            b2 += 1

    j = 0    
    x1 = np.zeros(b1)
    y1 = np.zeros(b1)
    k = 0
    x2 = np.zeros(b2)
    y2 = np.zeros(b2)

    for i in range(N):
        if K[i] == 1:
            x1[j] = xRaz[i]    
            y1[j] = yRaz[i]
            j += 1
        
        if K[i] == 2:
            x2[k] = xRaz[i]    
            y2[k] = yRaz[i]
            k += 1        
    
    plt.scatter(x1, y1, s=0.5, c='red', facecolor='0.5', lw = 0)
    plt.scatter(x2, y2, s=0.5, c='blue', facecolor='0.5', lw = 0)
    plt.xlim(-0.5,2.5)
    plt.ylim(-0.5,1.5)
    plt.xlabel("$u-g$")
    plt.ylabel("$g-r$")
    plt.savefig("iteracija_" + str(num), dpi = 300)    
    plt.show()
  
#x1 = rnd.uniform(-0.5,2.5)
#y1 = rnd.uniform(-0.5,1.5)

#y2 = rnd.uniform(-0.5,2.5)
#x2 = rnd.uniform(-0.5,1.5)

x1 = 0.6830104571311884
y1 = 0.33101327847443573
x2 = 2.42081762282727
y2 = 0.19600761919595922

K = np.zeros(N)

#K[0] = 1
#Isto = False



k = 1
epsilon = 1e-2
while 1:
    
#    print(k)
    k += 1
#    Isto = True
    
    for i in range(N):
        if rast(x1,y1,xRaz[i],yRaz[i]) > rast(x2,y2,xRaz[i],yRaz[i]):

#            if(K[i] == 2):
#                Isto = False

            K[i] = 1
        else:

#            if(K[i] == 1):
#                Isto = False

            K[i] = 2

    x1s = x1
    x2s = x2
    y1s = y1
    y2s = y2
    
    x1,y1,x2,y2 = cm(K)
    
    if k % 5 == 0:
        plot(K,k)        

    if np.abs(x1s - x2) <= epsilon and  np.abs(x2s - x1) <= epsilon and np.abs(y1s - y2) <= epsilon and np.abs(y2s - y1) <= epsilon:
        break
    
    
plot(K,k)
