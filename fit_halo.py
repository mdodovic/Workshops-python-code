import numpy as np
import scipy as scipy
import pylab 
import math as math
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
import matplotlib.lines as mlines
from scipy.optimize import curve_fit


def halo (x,rh,sc):
    return sc/( (x/rh)*(1+x/rh)**2 )



NIZM,NIZX,NIZY,NIZZ,NIZVX,NIZVY,NIZVZ= np.loadtxt("C:/Users/matij/Desktop/M31_izolacija/txt/DBH2/halo_000.txt", unpack=True)
#povrsinska gustina
N=len(NIZM)
Rad2=[]
Rad3=[]
for i in range(N):
    Rad2.append((NIZX[i]**2 + NIZY[i]**2)**0.5)
#max2=int(max(Rad2))
#print(max2)
rez=0.01
rl=0.01
rd=rl+rez
rmax=2
Rho=[]
R=[]

while rl<=rmax:
    m=0    
    for i in range(N):
        r2 = Rad2[i]
        if rl <= r2 and r2 < rd:
            m += NIZM[i]
    S=np.pi*(rd**2 - rl**2)
    Rho.append(m/S) #povrsinska gustina!!!
    R.append(rl)
    rl += rez
    rd += rez
#R[0] = 1e-13

file = open('C:/Users/matij/Desktop/parametar.txt','w')
for i in range(len(R)):
    file.write(str(R[i]) + '\n')
file.close()

file = open('C:/Users/matij/Desktop/parametar2.txt','w')
for i in range(len(R)):
    file.write(str(Rho[i]) + '\n')
file.close()


par,cov = curve_fit( halo, R, Rho )



plt.plot(R,Rho, c='black')
plt.plot(R,halo(R,*par),c='r')
plt.show()


print(par)


