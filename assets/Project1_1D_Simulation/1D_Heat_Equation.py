import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.show()

n = 10
h = 2.0/n #the distance stepped used is 1/10 but n can be anything

A = np.zeros((n+1,n+1))
A[0,0] = 1
A[n,n] = 1
for i in range(1,n):
    A[i,i-1] = 1
    A[i,i] = -2
    A[i,i+1] = 1

print(A)

b = np.zeros(n+1)
b[0:n] = 0
b[n] = 100
print(b)

y = np.linalg.solve(A,b)
print(y) 
x = np.linspace(0,2,n+1)

plt.figure(figsize=(8,6))
plt.plot(x,y,'-o')
plt.xlabel('x')
plt.ylabel('T')
plt.title('1D Heat Equation Solution')
plt.show()