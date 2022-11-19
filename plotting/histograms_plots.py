import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

N = 400
colors = sns.color_palette('pastel')
sns.set_style('darkgrid')
T1data = np.loadtxt('plotting/datafiles/energies_20_UO_1.00000-1.00000.txt')/N
T24data = np.loadtxt('plotting/datafiles/energies_20_UO_2.40000-2.40000.txt')/N

h1 = sns.histplot(data=T1data, stat="probability", bins = 500, binwidth=0.01)
h1.set_xlabel('$\epsilon$ [J]')
plt.savefig('plotting/figures/Normalized histogram T = 1 J.pdf')
plt.show()

h2 = sns.histplot(data=T24data, stat="probability", bins = 500, binwidth=0.01)
h2.set_xlabel('$\epsilon$ [J]')
plt.savefig('plotting/figures/Normalized histogram T = 2.4 J.pdf')
plt.show()
