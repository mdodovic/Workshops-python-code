import numpy as np
import matplotlib.pyplot as plt

def intenzitet(a,b,c):
    return (a*a + b*b + c*c)**0.5

class telo:
    x = 0
    y = 0
    z = 0
    vx = 0
    vxh = 0
    vy = 0
    vyh = 0
    vz = 0
    vzh = 0
    ax = 0
    ay = 0
    az = 0    
    m = 0
    
    def __init__(self,x,y,z,vx,vxh,vy,vyh,vz,vzh,ax,ay,az,m,Ek,Ep):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vxh = vxh
        self.vy = vy
        self.vyh = vyh
        self.vz = vz
        self.vzh = vzh
        self.ax = ax
        self.ay = ay
        self.az = az
        self.m = m

 
tela = []        
N = 2

tela.append(telo(1.5e11,0,0,0,0,2*3.14159*1.5e11/(365*24*3600),0,0,0,0,0,0,6e24,0,0))
tela.append(telo(0,0,0,0,0,0,0,0,0,0,0,0,2e30,0,0))        
x = []
y = []
z = []

Vreme = []
G = 6.67e-11 #m^3*kg^-1*s^-2
dt = 86400#s
t=0
tmax=86400*365*500#s


T = []
#E0 = 1/2 * intensity(tela[0].vx, tela[0].vy, tela[0].vz)**2 * tela[0].m - G*tela[0].m*tela[1].m/intensity(tela[0].vx, tela[0].vy, tela[0].vz)
E = []

E.append(1/2 * intenzitet(tela[0].vx, tela[0].vy, tela[0].vz)**2 * tela[0].m - G*tela[0].m*tela[1].m/intenzitet(tela[0].vx, tela[0].vy, tela[0].vz))
Vreme.append(0)



while t<=tmax:
    print(t/tmax*100)
    
    for i in range(N):
        Fx = 0
        Fy = 0
        Fz = 0
        for j in range(N):
            if(i != j):
                r = (intenzitet(tela[i].x - tela[j].x,tela[i].y - tela[j].y, tela[i].z - tela[j].z))
                Fx += - G*tela[i].m * tela[j].m *(tela[i].x - tela[j].x) / (r**3)   
                Fy += - G*tela[i].m * tela[j].m *(tela[i].y - tela[j].y) / (r**3)
                Fz += - G*tela[i].m * tela[j].m *(tela[i].z - tela[j].z) / (r**3)
        tela[i].ax = Fx / tela[i].m
        tela[i].ay = Fy / tela[i].m
        tela[i].az = Fz / tela[i].m


    for i in range(N):
        tela[i].vx = tela[i].vx + tela[i].ax * dt
        tela[i].vy += tela[i].ay * dt
        tela[i].vz += tela[i].az * dt


    for i in range(N):
        tela[i].x += tela[i].vx * dt
        tela[i].y += tela[i].vy * dt
        tela[i].z += tela[i].vz * dt
        x.append(tela[i].x)
        y.append(tela[i].y)
        z.append(tela[i].z)


    t+=dt
    E.append(1/2 * intenzitet(tela[0].vx, tela[0].vy, tela[0].vz)**2 * tela[0].m - G*tela[0].m*tela[1].m/intenzitet(tela[0].vx, tela[0].vy, tela[0].vz))	
    Vreme.append(t)

plt.scatter(x,y,s = 0.1)
plt.xlabel("$X[AJ]$")
plt.ylabel("$Y[AJ]$")
plt.savefig("1")
plt.show()

print(len(T))
print(len(E))
plt.scatter(Vreme,E,s = 0.1)
plt.xlabel("$T$")
plt.ylabel("$E$")
plt.savefig("2")
plt.show()

