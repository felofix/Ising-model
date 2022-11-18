import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

N = 400
colors = sns.color_palette('pastel')
sns.set_style('darkgrid')

T1data = np.loadtxt("plotting/datafiles/energies20x20_T1energy.txt")/N
T24data = np.loadtxt("plotting/datafiles/energies20x20_T24energy.txt")/N

h1 = sns.histplot(data=T1data, stat="probability",  bins = 500, binwidth=0.2)
h1.set_xlabel('$\epsilon$ [J]')
plt.savefig('plotting/figures/Normalized histogram T = 1 J.pdf')
plt.show()

h2 = sns.histplot(data=T24data, stat="probability",  bins = 500, binwidth=0.2)
h2.set_xlabel('$\epsilon$ [J]')
plt.savefig('plotting/figures/Normalized histogram T = 2.4 J.pdf')
plt.show()
