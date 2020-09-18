#Konverzija dekart->kepler
import math as math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
### Unos
t,x,y,z = np.loadtxt("podaci,t,x,y,z.txt", unpack=True)
#t - vreme[dan]
#x - koordinata po x[AJ]
#y - koordinata po y[AJ]
#z - koordinata po z[AJ]

### Funkcije

def brzina_koord(t1,t2,r1,r2):
    v_koord = (r1-r2)/(t1-t2);
    return v_koord;

def intenzitet(a,b,c):
    it=(a*a+b*b+c*c)**0.5;
    return it;

def srednja_vrednost(x,n):
    s=0;
    for i in range(n):
            s=s+x[i];
    return abs(s/n);
    
###Glavni Program
    
#konstante
Mass=1.98891691172467e30 #Masa sunca [kg]
G=1.4872216e-34 #Gravitaciona konstanta [AJ^3*kg^(-1)*dan^(-2)]

N=len(t)-1; #broj clanova niza
#intenzitet radijus vektora    
r=[]
for i in range(N):
    r.append(intenzitet(x[i],y[i],z[i]));        
#brzine
vx=[];
vy=[];
vz=[];
v=[];
for i in range(N):
    vx.append(brzina_koord(t[i],t[i+1],x[i],x[i+1])); 
    vy.append(brzina_koord(t[i],t[i+1],y[i],y[i+1]));
    vz.append(brzina_koord(t[i],t[i+1],z[i],z[i+1]));
    v.append(intenzitet(vx[i],vy[i],vz[i]));        
#specificni momenti impulsa
lx=[]
ly=[]
lz=[]
l=[]
for i in range(N):
    lx.append(y[i]*vz[i] - z[i]*vy[i]);
    ly.append(z[i]*vx[i] - x[i]*vz[i]);
    lz.append(x[i]*vy[i] - y[i]*vx[i]);
    l.append(intenzitet(lx[i],ly[i],lz[i]));

E=[] #ukupna energija
for i in range(N):
    E.append(v[i]*v[i]/2 - G*Mass/r[i])    
    

a=[] #!velika poluosa
e=[] #!ekscentricitet
inc=[] #!inklinacija
OM=[] #!longituda uzlaznog cvora
teta=[] #prava anomalija
om=[] #!argument perihela
f=[] #zbir arg. perihla i prave anomalije
Exc=[] #ekscentricna anomalija
M=[] #!srednja anomalija 
tau=[] #vreme prolaska kroz perihel
for k in range(N):
    #putanjski elementi

    a.append(-G*Mass/2/E[k]) 
        
    e.append((1-l[k]*l[k]/(a[k]*G*Mass))**0.5)
    
    inc.append(math.acos(lz[k]/l[k]))

    OM.append(math.atan2(lx[k],-ly[k]))

    teta.append(math.acos((a[k]*(1-e[k]*e[k])-r[k])/e[k]/r[k]))
       
    f.append(math.atan2((z[k]/(math.sin(inc[k]))),(x[k]*math.cos(OM[k])+y[k]*math.sin(OM[k]))))    
    
    om.append(f[k]-teta[k])
    
    Exc.append(2*math.atan(((1-e[k])/1+e[k])**0.5 * math.tan(teta[k]))) 
        
    M.append(Exc[k]-e[k]*math.sin(Exc[k]))

    tau.append(t[k] - M[k]/((G*Mass/(a[k]*a[k]*a[k]))**0.5))

M.append(M[0])
for br1 in range(N-1):
    for br2 in range(br1+1, N):
        if M[br1] > M[br2]:
            tmp=M[br1]
            M[br1]=M[br2]
            M[br2]=tmp


#ispis + plotovanje        
        
print("Velika poluosa: ",srednja_vrednost(a,N))
print("Ekscentricitet: ",srednja_vrednost(e,N))
print("Inklinacija",math.degrees(srednja_vrednost(inc,N)))
print("Longituda uzlaznog cvora",math.degrees(srednja_vrednost(OM,N)))
#print("Prava anomalija",srednja_vrednost(teta,N))
print("Argument perihela",math.degrees(srednja_vrednost(om,N)))
#print("Ekscentricna anomalija",srednja_vrednost(Exc,N))
print("Srednja anomalija, kao niz, upisana je u .txt fajl",)

file = open("Srednja_anomalija,M.txt","w")
for i in range(N):
    file.write(str(M[i]) + "\n")

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
