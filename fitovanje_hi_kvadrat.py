import numpy as np;
import matplotlib.pyplot as plt;
X,Y,Sigma = np.loadtxt('prviz.txt', unpack=True, delimiter = ' ');
N=len(X);

plt.show();
a=1.3;
b=0.068;
def f(a,b,x):
    return a*np.exp(-b*x);

def hi(a,b,x,y,z,N):
    h=0;
    for i in range (N):
        h+=((y[i]-f(a,b,x[i]))**2)/(2*z[i]*z[i]);
    return h;
    
m=hi(1.3,0.0068,X,Y,Sigma,N);
#m1=hi(1.2,0.007400000000000004,X,Y,Sigma,N)
#print(m);
#print(m1);
min=m
i=0.5
inda=0
indb=0
while i<1.5:
    j=0.001
    while j<0.01:
        a=i;
        b=j;
        min = hi(a,b,X,Y,Sigma,N);
        #print(min);
        if min < m:
            m=min;
            inda=i
            indb=j
        j+=0.0001
    i+=0.01
print(inda);
print(indb);

#plt.scatter(X,Y)
plt.errorbar(X, Y, yerr = Sigma, fmt= ".")
plt.plot(X,inda*np.exp(-indb*X),color = 'red')