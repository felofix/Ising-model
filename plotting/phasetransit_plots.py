import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette('pastel')
sns.set_style('darkgrid')
info40 = np.loadtxt('plotting/datafiles/info40.txt')
info60 = np.loadtxt('plotting/datafiles/info60.txt')
#info80 = np.loadtxt('plotting/datafiles/info80.txt')
t40 = info40[4::5]
t60 = info60[4::5]
#t80 = info80[4::5]
sort40 = np.sort(t40)
sort60 = np.sort(t60)
#sort80 = np.sort(t80)
sortedindex40 = []
sortedindex60 = []
#sortedindex80 = []

for i in range(len(t40)):
    sortedindex40.append(int(np.where(sort40[i] == t40)[0]))
    sortedindex60.append(int(np.where(sort60[i] == t60)[0]))
    #sortedindex80.append(int(np.where(sort80[i] == t80)[0]))

# Times
t40 = info40[4::5][sortedindex40]
t60 = info60[4::5][sortedindex60]
#t80 = info60[4::5][sortedindex80]

# Energies.
E40 = info40[0::5][sortedindex40]
E60 = info60[0::5][sortedindex60]
#E80 = info80[0::5][sortedindex80]

# Magnetization
#M40 = np.flip(np.sort(abs(info40[1::5][sortedindex40])))
#M60 = np.flip(np.sort(abs(info60[1::5][sortedindex60])))
M40 = abs(info40[1::5])
M60 = abs(info60[1::5])
#M80 = np.flip(np.sort(abs(info80[1::5][sortedindex80])))

# Heat capacities.
HC40 = info40[2::5][sortedindex40]
HC60 = info60[2::5][sortedindex60]
#HC80 = info80[2::5][sortedindex80]

# Suscebtilibity
S40 = info40[3::5][sortedindex40]
S60 = info60[3::5][sortedindex60]
#S80 = info80[3::5][sortedindex80]

# Plotting energies.
plt.plot(t40, E40,"--.", label = "L = 40")
plt.plot(t40, E60,"--." , label = "L = 60")
#plt.plot(t40, E80,"--." , label = "L = 80")
plt.xlabel('Temperature [K]')
plt.xlabel('Energy [J/$k_B$] ')
plt.legend()
plt.show()

# Plotting magnetization.
plt.plot(t40, M40,"--.", label = "L = 40")
plt.plot(t40, M60,"--." , label = "L = 60")
#plt.plot(t40, M80,"--." , label = "L = 80")
plt.xlabel('Temperature [K]')
plt.xlabel('Magnetization ')
plt.legend()
plt.show()

# Plotting heat capacities.
plt.plot(t40, HC40,"--.", label = "L = 40")
plt.plot(t40, HC60,"--.", label = "L = 60")
#plt.plot(t40, HC80,"--.", label = "L = 80")
plt.xlabel('Temperature [K]')
plt.ylabel('Heat capacity $C_v$ [J/$k_b$]')
plt.legend()
plt.show()

# Plotting suscebtilibity.
plt.plot(t40, S40,"--.", label = "L = 40")
plt.plot(t40, S60,"--.", label = "L = 60")
#plt.plot(t40, S80,"--.", label = "L = 80")
plt.xlabel('Temperature [K]')
plt.ylabel('Magnetic suscebility $\chi$ [J/$k_b$]')
plt.legend()
plt.show()
