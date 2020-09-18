import numpy as np
import matplotlib.pyplot as plt

def intensity(a,b,c):
    return np.sqrt(a*a + b*b + c*c)
class telo:
    x = 0
    y = 0
    z = 0
    vx = 0
    vy = 0
    vz = 0
    ax = 0
    ay = 0
    az = 0
    m = 0
    v1x = 0
    v2x = 0
    v3x = 0
    v4x = 0
    v1y = 0
    v2y = 0
    v3y = 0
    v4y = 0
    v1z = 0
    v2z = 0
    v3z = 0
    v4z = 0
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0
    z1 = 0
    z2 = 0
    z3 = 0
    z4 = 0
    a1x = 0
    a2x = 0
    a3x = 0
    a1y = 0
    a4x = 0
    a2y = 0
    a3y = 0
    a4y = 0
    a1z = 0
    a2z = 0
    a3z = 0
    a4z = 0

    def __init__(self,x,y,z,vx,vy,vz,ax,ay,az,m):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.ax = ax
        self.ay = ay
        self.az = az
        self.m = m

tela = []
N = 2

tela.append(telo(1.5e11,0,0,0,30000,0,0,0,0,6e24))
tela.append(telo(0,0,0,0,0,0,0,0,0,2e30))


x = []
y = []
z = []
G = 6.67e-11
dt = 86400#s
t=0
tmax=86400*365*10#s

T = []
E0 = 1/2 * intensity(tela[0].vx, tela[0].vy, tela[0].vz)**2 * tela[0].m - G*tela[0].m*tela[1].m/intensity(tela[0].vx, tela[0].vy, tela[0].vz)
E = []
E.append(1/2 * intensity(tela[0].vx, tela[0].vy, tela[0].vz)**2 * tela[0].m - G*tela[0].m*tela[1].m/intensity(tela[0].vx, tela[0].vy, tela[0].vz) - E0)

#E.append(1/2 * intensity(tela[0].vx, tela[0].vy, tela[0].vz)**2 * tela[0].m - G*tela[0].m*tela[1].m/intensity(tela[0].vx, tela[0].vy, tela[0].vz))
#E.append(1/2 * intensity(tela[0].vx, tela[0].vy, tela[0].vz)**2 * tela[0].m - G*tela[0].m*tela[1].m/intensity(tela[0].vx, tela[0].vy, tela[0].vz))

T.append(0)

while t < tmax:
    print (t/tmax*100)
    #1
    for i in range(N):
        tela[i].v1x = tela[i].vx
        tela[i].v1y = tela[i].vy
        tela[i].v1z = tela[i].vz
        tela[i].x1 = tela[i].x
        tela[i].y1 = tela[i].y
        tela[i].z1 = tela[i].z
    for i in range(N):
        Fx = 0
        Fy = 0
        Fz = 0
        for j in range(N):
            if(i!=j):
                r = ((tela[i].x1 - tela[j].x1)**2 + (tela[i].y1 - tela[j].y1)**2 + (tela[i].z1 - tela[j].z1)**2)**(0.5)
                Fx += - G*tela[i].m * tela[j].m *(tela[i].x1 - tela[j].x1) / (r * r * r)
                Fy += - G*tela[i].m * tela[j].m *(tela[i].y1 - tela[j].y1) / (r * r * r)
                Fz += - G*tela[i].m * tela[j].m *(tela[i].z1 - tela[j].z1) / (r * r * r)
        tela[i].a1x = Fx / tela[i].m
        tela[i].a1y = Fy / tela[i].m
        tela[i].a1z = Fz / tela[i].m
    #2
    for i in range(N):
        tela[i].v2x = tela[i].vx + tela[i].a1x * dt/2
        tela[i].v2y = tela[i].vy + tela[i].a1y * dt/2
        tela[i].v2z = tela[i].vz + tela[i].a1z * dt/2
        tela[i].x2 = tela[i].x + tela[i].v2x * dt/2
        tela[i].y2 = tela[i].y + tela[i].v2y * dt/2
        tela[i].z2 = tela[i].z + tela[i].v2z * dt/2
    for i in range(N):
        Fx = 0
        Fy = 0
        Fz = 0
        for j in range(N):
            if(i!=j):
                r = ((tela[i].x2 - tela[j].x2)**2 + (tela[i].y2 - tela[j].y2)**2 + (tela[i].z2 - tela[j].z2)**2)**(0.5)
                Fx += - G*tela[i].m * tela[j].m *(tela[i].x2 - tela[j].x2) / (r * r * r)
                Fy += - G*tela[i].m * tela[j].m *(tela[i].y2 - tela[j].y2) / (r * r * r)
                Fz += - G*tela[i].m * tela[j].m *(tela[i].z2 - tela[j].z2) / (r * r * r)
        tela[i].a2x = Fx / tela[i].m
        tela[i].a2y = Fy / tela[i].m
        tela[i].a2z = Fz / tela[i].m
    #3
    for i in range(N):
        tela[i].v3x = tela[i].vx + tela[i].a2x * dt/2
        tela[i].v3y = tela[i].vy + tela[i].a2y * dt/2
        tela[i].v3z = tela[i].vz + tela[i].a2z * dt/2
        tela[i].x3 = tela[i].x + tela[i].v3x * dt/2
        tela[i].y3 = tela[i].y + tela[i].v3y * dt/2
        tela[i].z3 = tela[i].z + tela[i].v3z * dt/2
    for i in range(N):
        Fx = 0
        Fy = 0
        Fz = 0
        for j in range(N):
            if(i!=j):
                r = ((tela[i].x3 - tela[j].x3)**2 + (tela[i].y3 - tela[j].y3)**2 + (tela[i].z3 - tela[j].z3)**2)**(0.5)
                Fx += - G*tela[i].m * tela[j].m *(tela[i].x3 - tela[j].x3) / (r * r * r)
                Fy += - G*tela[i].m * tela[j].m *(tela[i].y3 - tela[j].y3) / (r * r * r)
                Fz += - G*tela[i].m * tela[j].m *(tela[i].z3 - tela[j].z3) / (r * r * r)
        tela[i].a3x = Fx / tela[i].m
        tela[i].a3y = Fy / tela[i].m
        tela[i].a3z = Fz / tela[i].m

    #4

    for i in range(N):
        tela[i].v4x = tela[i].vx + tela[i].a3x * dt
        tela[i].v4y = tela[i].vy + tela[i].a3y * dt
        tela[i].v4z = tela[i].vz + tela[i].a3z * dt
        tela[i].x4 = tela[i].x + tela[i].v4x * dt
        tela[i].y4 = tela[i].y + tela[i].v4y * dt
        tela[i].z4 = tela[i].z + tela[i].v4z * dt

    for i in range(N):
        Fx = 0
        Fy = 0
        Fz = 0
        for j in range(N):
            if(i!=j):
                r = ((tela[i].x4 - tela[j].x4)**2 + (tela[i].y4 - tela[j].y4)**2 + (tela[i].z4 - tela[j].z4)**2)**(0.5)
                Fx += - G*tela[i].m * tela[j].m *(tela[i].x4 - tela[j].x4) / (r * r * r)
                Fy += - G*tela[i].m * tela[j].m *(tela[i].y4 - tela[j].y4) / (r * r * r)
                Fz += - G*tela[i].m * tela[j].m *(tela[i].z4 - tela[j].z4) / (r * r * r)
        tela[i].a4x = Fx / tela[i].m
        tela[i].a4y = Fy / tela[i].m
        tela[i].a4z = Fz / tela[i].m
        
    #final
    for i in range(N):
        tela[i].x += dt/6.0 * (tela[i].v1x + 2*tela[i].v2x + 2*tela[i].v3x + tela[i].v4x)
        tela[i].y += dt/6.0 * (tela[i].v1y + 2*tela[i].v2y + 2*tela[i].v3y + tela[i].v4y)
        tela[i].z += dt/6.0 * (tela[i].v1z + 2*tela[i].v2z + 2*tela[i].v3z + tela[i].v4z)
        tela[i].vx += dt/6.0 * (tela[i].a1x + 2*tela[i].a2x + 2*tela[i].a3x + tela[i].a4x)
        tela[i].vy += dt/6.0 * (tela[i].a1y + 2*tela[i].a2y + 2*tela[i].a3y + tela[i].a4y)
        tela[i].vz += dt/6.0 * (tela[i].a1z + 2*tela[i].a2z + 2*tela[i].a3z + tela[i].a4z)
        #print (tela[0].vx, tela[0].vy, tela[0].vz)
        x.append(tela[i].x - tela[1].x)
        y.append(tela[i].y - tela[1].y)
        z.append(tela[i].z - tela[1].z)
        #print tela[0].vx, tela[0].vy, tela[0].vz


    E.append(1/2 * intensity(tela[0].vx, tela[0].vy, tela[0].vz)**2 * tela[0].m - G*tela[0].m*tela[1].m/intensity(tela[0].vx, tela[0].vy, tela[0].vz) - E0)
    T.append(t)

    t += dt


plt.plot(T,E)
#print("x-z")
#plt.scatter(x,z)############
#print("y-z")
#plt.scatter(y,z)############
plt.show()


print("x-y")
plt.scatter(x,y,s=0.1)
#print("x-z")
#plt.scatter(x,z)############
#print("y-z")
#plt.scatter(y,z)############
plt.show()
