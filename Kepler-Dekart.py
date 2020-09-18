#Konverzija dekart->kepler
import math as math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
### Unos


M = np.loadtxt("C:/Users/matij/Desktop/Medjuseminarski zadatak 2017/Srednja_anomalija,M.txt", unpack=True) 
#M[rad]
#Srednja anomalija je promenjiva u vremenu, ona se cita iz txt fajla

a=9.53074007187 #velika poluosa [AU]
e = 0.0560576324559 #ekscentricitet []
i = 2.5000645502667456 #inklinacija [rad]
OMEGA = 1.9830265929803637#longituda uzlaznog cvora [rad]
omega = 1.5877624180554277#argument perihela [rad]
###

###Glavni Program

#konstante

GM = 1.98891691172467E+30 * 6.67e-11
eps = 10**(-15)


N = len(M)
#koordinate i intenzitet
x=[]
y=[]
z=[]
r=[]

#moment impulsa, intenzitet i po koorrdinatama
l=[]
lx=[]
ly=[]
lz=[]

#brzine po koordinatama
vx=[]
vy=[]
vz=[]


for k in range(N):
    #ekscentricna anomalija    
    Exc = M[k]
    Exc_n = M[k] + e*np.sin(Exc)
    while(np.abs(Exc - Exc_n) > eps):
        Exc = Exc_n
        Exc_n = M[k] + e*math.sin(Exc)


    #prava anomalija
    ni = 2 * np.arctan(  ((1+e)/(1-e))**0.5 * np.tan(Exc/2)) #prava anomalija
    
    r.append(a * (1 - e * e)/(1+e*np.cos(ni))) #radijus
    
    l.append((GM * a * (1 - e**2))**0.5) #moment impulsa

    x.append( r[k] * (np.cos(OMEGA) * np.cos(omega + ni) - np.sin(OMEGA) * np.sin(omega + ni) * np.cos(i)) )

    y.append( r[k] * (np.sin(OMEGA) * np.cos(omega+ni) + np.cos(OMEGA) * np.sin(omega + ni) * np.cos(i)) )


    z.append( r[k] * (np.sin(i) * np.sin(omega+ni)) )

    p = a * (1 - e**2)
    
    vx.append( x[k] * l[k] * e * np.sin(ni) / (r[k] * p) - l[k] / r[k] * (np.cos(OMEGA) * np.sin(omega + ni) + np.sin(OMEGA) * np.cos(omega + ni) * np.cos(i)) )

    vy.append( y[k] * l[k] * e * np.sin(ni) / (r[k] * p) - l[k] / r[k] * (np.sin(OMEGA) * np.sin(omega + ni) - np.cos(OMEGA) * np.cos(omega + ni) * np.cos(i)) )
    
    vz.append( z[k] * l[k] * e * np.sin(ni) / (r[k] * p) + l[k] / r[k] * np.sin(i) * np.cos(omega + ni) )

#ispis i plotovanje

print("Putanjski elementi su u .txt fajlu")

file = open("Putanjski elementi,x,y,z,vx,vy,vz.txt","w")
for i in range(N):
    file.write(str(x[i]) + str(y[i]) + str(z[i]) + str(vx[i]) + str(vy[i]) + str(vz[i]) + "\n")


mpl.rcParams['legend.fontsize'] = 10 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X[AJ]')
ax.set_xlim(-10, 10)
ax.set_ylabel('Y[AJ]')
ax.set_ylim(-10, 10)
ax.set_zlabel('Z[AJ]')
ax.set_zlim(-10, 10)
ax.plot(x, y, z, label='elipsa')
ax.legend()
plt.show()
