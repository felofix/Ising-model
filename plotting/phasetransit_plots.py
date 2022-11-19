import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette('pastel')
sns.set_style('darkgrid')
info40 = np.loadtxt('plotting/datafiles/info_40_UO_1.00000-2.40000.txt')
info60 = np.loadtxt('plotting/datafiles/info_60_UO_1.00000-2.40000.txt')
info80 = np.loadtxt('plotting/datafiles/info_80_UO_1.00000-2.40000.txt')
info100 = np.loadtxt('plotting/datafiles/info_100_UO_1.00000-2.40000.txt')
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

# Times
t40 = info40[4::5][sortedindex40]
t60 = info60[4::5][sortedindex60]
t80 = info80[4::5][sortedindex80]
t100 = info60[4::5][sortedindex100]

# Energies.
E40 = info40[0::5][sortedindex40]
E60 = info60[0::5][sortedindex60]
E80 = info80[0::5][sortedindex80]
E100 = info100[0::5][sortedindex100]

# Magnetization
M40 = info40[1::5][sortedindex40]
M60 = info60[1::5][sortedindex60]
M80 = info80[1::5][sortedindex80]
M100 = info100[1::5][sortedindex100]

# Heat capacities.
HC40 = info40[2::5][sortedindex40]
HC60 = info60[2::5][sortedindex60]
HC80 = info80[2::5][sortedindex80]
HC100 = info100[2::5][sortedindex100]

# Suscebtilibity
S40 = info40[3::5][sortedindex40]
S60 = info60[3::5][sortedindex60]
S80 = info80[3::5][sortedindex80]
S100 = info100[3::5][sortedindex100]

# Plotting energies.
plt.plot(t40, E40,"--.", label = "L = 40")
plt.plot(t40, E60,"--." , label = "L = 60")
plt.plot(t40, E80,"--." , label = "L = 80")
plt.plot(t40, E100,"--." , label = "L = 100")
plt.xlabel('Temperature [K]')
plt.xlabel('Energy [J/$k_B$] ')
plt.savefig('plotting/figures/Energy of the four lattice sizes.pdf')
plt.legend()
plt.show()

# Plotting magnetization.
plt.plot(t40, M40,"--.", label = "L = 40")
plt.plot(t40, M60,"--." , label = "L = 60")
plt.plot(t40, M80,"--." , label = "L = 80")
plt.plot(t40, M100,"--." , label = "L = 100")
plt.xlabel('Temperature [K]')
plt.ylabel('Magnetization')
plt.savefig('plotting/figures/Magnetization of the four lattice sizes.pdf')
plt.legend()
plt.show()

# Plotting heat capacities.
plt.plot(t40, HC40,"--.", label = "L = 40")
plt.plot(t40, HC60,"--.", label = "L = 60")
plt.plot(t40, HC80,"--.", label = "L = 80")
plt.plot(t40, HC100,"--.", label = "L = 100")
plt.xlabel('Temperature [K]')
plt.ylabel('Heat capacity $C_v$ [$k_b$]')
plt.savefig('plotting/figures/Heat capacity of the four lattice sizes.pdf')
plt.legend()
plt.show()

# Plotting suscebtilibity.
plt.plot(t40, S40,"--.", label = "L = 40")
plt.plot(t40, S60,"--.", label = "L = 60")
plt.plot(t40, S80,"--.", label = "L = 80")
plt.plot(t40, S100,"--.", label = "L = 100")
plt.xlabel('Temperature [K]')
plt.ylabel('Magnetic suscebility $\chi$ [1/J]')
plt.savefig('plotting/figures/Suscebtilibity of the four lattice sizes.pdf')
plt.legend()
plt.show()

