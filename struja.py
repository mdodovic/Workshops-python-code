import numpy as np
import matplotlib.pyplot as plt

C = 1 #F
U = 1 #V
R = 1 #OM

q0 = C*U

Qn = []
Qa = []
t = []
Qn.append(q0)
Qa.append(q0)
t.append(0)

dt = 100

Q = []
T = []

while dt <= 1e6:
    
    i = 0
    while Qn[i] >= 0.2:
        dq1 = -dt*Qn[i]/R/C
        dq2 = -dt*(Qn[i] + 0.5*dq1)/R/C
        dq3 = -dt*(Qn[i] + 0.5*dq2)/R/C
        dq4 = -dt*(Qn[i] + dq3)/R/C   
        dq = (dq1 + 2*dq2 + 2*dq3 + dq4)/6    
        Qn.append(Qn[i] + dq)
    
        Qa.append((np.e)**(-1/R/C *t[i]))
    
        t.append(t[i] + dt)
        i+=1
    
    Q.append(np.abs(Qa[i-1]-Qn[i-1]))
    T.append(dt)        
    
    dt = dt + 1
    
plt.plot(np.abs(np.log10(T)),np.abs(np.log10(Q)))
plt.xscale('log')
plt.yscale('log')
#plt.ylim(-0.2042,-0.204)
plt.show()
