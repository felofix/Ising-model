import numpy as np
import matplotlib.pyplot as plt

matrixstart = np.loadtxt('plotting/datafiles/20x20_T1_spins_start.txt')
matrixendT1 = np.loadtxt('plotting/datafiles/20x20_T1_spins_end.txt')
matrixendT2 = np.loadtxt('plotting/datafiles/20x20_T24_spins_end.txt')


plt.imshow(matrixstart, cmap='Blues')
plt.savefig('plotting/figures/Matrix at start.pdf')
plt.show()

plt.imshow(matrixendT1, cmap='Blues')
plt.savefig('plotting/figures/Matrix at end with t1.pdf')
plt.show()

plt.imshow(matrixendT2, cmap='Blues')
plt.savefig('plotting/figures/Matrix at end with t2.pdf')
plt.show()

