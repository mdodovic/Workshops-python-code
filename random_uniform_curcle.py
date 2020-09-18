import math as math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

X = []
Y = []

for i in range(5000):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)

    X.append(x)
    Y.append(y)

    X.append(-x)
    Y.append(y)    

    X.append(x)
    Y.append(-y)
    
    X.append(-x)
    Y.append(-y)
        
plt.figure(5)
plt.axis('equal')
plt.scatter(X,Y,s=0.005)
plt.show()

X = []
Y = []

for i in range(5000):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,(1-x*x)**0.5)

    X.append(x)
    Y.append(y)

    X.append(-x)
    Y.append(y)    

    X.append(x)
    Y.append(-y)
    
    X.append(-x)
    Y.append(-y)
        
plt.figure(5)
plt.axis('equal')
plt.scatter(X,Y,s=0.005)
plt.show()


X = []
Y = []

for i in range(15000):
    fi = np.random.uniform(0,2*np.pi)
    
    u = np.random.uniform(0,1)    
    
    r = (u*2)**0.5



    X.append(r*np.cos(fi))
    Y.append(r*np.sin(fi))

plt.figure(5)
plt.axis('equal')
plt.scatter(X,Y,s=0.005)
plt.show()

X = []
Y = []
Z = []

for i in range(5000):
    fi = np.random.uniform(0,2*np.pi)

    teta1 = np.random.uniform(-1,1)

    r1 = np.random.uniform(0,1)

    r = (3*r1)**(1/3)
    teta = np.arccos(teta1)    

    X.append(r*np.cos(fi)*np.sin(teta))
    Y.append(r*np.sin(fi)*np.sin(teta))
    Z.append(r*np.cos(teta))    

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, label='elipsa', s = 0.005)
plt.show()


X = []
Y = []

for i in range(100000):
    x = np.random.uniform(-1,1)
    y = np.random.uniform(-1,1)
    
    X.append(x * (1 - 0.5*y*y)**0.5)    
    Y.append(y * (1 - 0.5*x*x)**0.5)

plt.figure(5)
plt.axis('equal')
plt.scatter(X,Y,s=0.005)
plt.show()

