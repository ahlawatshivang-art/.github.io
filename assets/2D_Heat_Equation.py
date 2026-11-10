import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

n = 10
deltat = .001
c = 1.0
deltaS = 1/n-1
T = np.zeros((n,n))

#initial conditions
T[0:1] = 100
for t in range(10000):
    T_new = T.copy()
    for i in range(1,n-1):
        for j in range(1,n-1):
            T_new[i,j] = T[i,j] + c*deltat/deltaS**2 *(T[i-1,j] + T[i+1,j] - 4*T[i,j] + T[i,j-1] + T[i,j+1])
    T = T_new

#visualization
cmap = mcolors.LinearSegmentedColormap.from_list("blue_red", ["blue", "red"])
fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(T, cmap=cmap, vmin=0, vmax=100)


ax.set_title("2D Heat Equation Simulation")
plt.tight_layout()
plt.show()
