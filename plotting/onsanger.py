import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

L = np.array([40, 60, 80, 100])

info40 = np.loadtxt('plotting/datafiles/info40.txt')
info60 = np.loadtxt('plotting/datafiles/info60.txt')
info80 = np.loadtxt('plotting/datafiles/info80.txt')
info100 = np.loadtxt('plotting/datafiles/info100.txt')

t40 = info40[4::5]
t60 = info60[4::5]
t80 = info80[4::5]
t100 = info100[4::5]
sort40 = np.sort(t40)
sort60 = np.sort(t60)
sort80 = np.sort(t80)
sort100 = np.sort(t100)
sortedindex40 = []
sortedindex60 = []
sortedindex80 = []
sortedindex100 = []

for i in range(len(t40)):
    sortedindex40.append(int(np.where(sort40[i] == t40)[0]))
    sortedindex60.append(int(np.where(sort60[i] == t60)[0]))
    sortedindex80.append(int(np.where(sort80[i] == t80)[0]))
    sortedindex100.append(int(np.where(sort100[i] == t100)[0]))

maxcv40 = np.max(info40[2::5][sortedindex40])
maxcv60 = np.max(info60[2::5][sortedindex60])
maxcv80 = np.max(info80[2::5][sortedindex80])
maxcv100 = np.max(info100[2::5][sortedindex100])
wheremax40 = np.where(info40[2::5][sortedindex40] == maxcv40)
wheremax60 = np.where(info60[2::5][sortedindex60] == maxcv60)
wheremax80 = np.where(info80[2::5][sortedindex80] == maxcv80)
wheremax100 = np.where(info100[2::5][sortedindex100] == maxcv100)
tc = np.array([t40[wheremax40][0], t60[wheremax60][0], t80[wheremax80][0], t100[wheremax100][0]])

# Printing the critical temperatures 
for i in range(len(tc)):
    print(f"T_c({40+i*20}) = {tc[i]}")
print(f"T_c (inf) = {linregress(1/L, tc).intercept}")

# Plottig the linear regresion
temp = np.linspace(L[0], L[-1], L(tc))
plt.scatter(temp, tc, label = "Data", color = "k")
plt.plot(temp, linregress(1/L, tc).intercept + temp*linregress(1/L, tc).slope, label = "Linear regression")
plt.xlabel("Lattice length $L$")
plt.ylabel("Critical temperature $T_c(L)")
plt.savefig('plotting/figures/Linear_regression.pdf')