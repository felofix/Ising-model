import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def mean_epsilon(energies, N): # Calculating mean energy per spin.
	return np.mean(energies/N)

def mean_mag(magnetizations, N): # Calculating magnetization per spin.
	return np.mean(abs(magnetizations/N))

def equilibration_e(energies, N):  # loop to see how the mean energy changes.
    mean_epsilons = np.zeros(len(energies))
    for i in range(1, len(mean_epsilons)):
        mean_epsilons[i] = mean_epsilon(energies[:i], N)
    return mean_epsilons

def equilibration_m(magnetizations, N): # loop to see how the mean magnetization changes.
	mean_mags = np.zeros(len(magnetizations))
	for i in range(1, len(mean_mags)):
		mean_mags[i] = mean_mag(magnetizations[:i], N)
	return mean_mags

# Energies.
energiesUT1 = np.loadtxt('plotting/datafiles/energies_20_UO_1.00000-1.00000.txt')
energiesOT1 = np.loadtxt('plotting/datafiles/energies_20_O_1.00000-1.00000.txt')
energiesUT24 = np.loadtxt('plotting/datafiles/energies_20_UO_2.400000-2.400000.txt')
energiesOT24 = np.loadtxt('plotting/datafiles/energies_20_O_2.400000-2.400000.txt')

# Magnetizations.
magnetUT1 = np.loadtxt('plotting/datafiles/magnetizations_20_UO_1.00000-1.00000.txt')
magnetOT1 = np.loadtxt('plotting/datafiles/magnetizations_20_O_1.00000-1.00000.txt')
magnetUT24 = np.loadtxt('plotting/datafiles/magnetizations_20_UO_2.400000-2.400000.txt')
magnetOT24 = np.loadtxt('plotting/datafiles/magnetizations_20_O_2.400000-2.400000.txt')

n20 = 400
cycles = np.linspace(0, len(energiesUT1), len(energiesUT1))
colors = sns.color_palette('pastel')
sns.set_style('darkgrid')

equiEUT1 = equilibration_e(energiesUT1, n20)
equiEOT1 = equilibration_e(energiesOT1, n20)
equiEUT24 = equilibration_e(energiesUT24, n20)
equiEOT24 = equilibration_e(energiesOT24, n20)

equiMUT1 = equilibration_m(magnetUT1, n20)
equiMOT1 = equilibration_m(magnetOT1, n20)
equiMUT24 = equilibration_m(magnetUT24, n20)
equiMOT24 = equilibration_m(magnetOT24, n20)


# Plotting equilibrium energies for T = 1.
plt.xlabel("$log_{10}$ of Monte Carlo cycles")
plt.ylabel("$<\epsilon> [J]$")
plt.plot(np.log10(cycles), equiEUT1, label='Unordered')
plt.plot(np.log10(cycles), equiEOT1,color = '#EC5A46', label='Ordered')
plt.legend()
plt.savefig("plotting/figures/Mean energy development for 20x20 with T = 1 J.pdf")
plt.show()

# Plotting equilibrium energies for T = 2.4.
plt.xlabel("$log_{10}$ of Monte Carlo cycles")
plt.ylabel("$<\epsilon> [J]$")
plt.plot(np.log10(cycles), equiEUT24, label='Ordered')
plt.plot(np.log10(cycles), equiEOT24,color = '#EC5A46', label='Unordered')
plt.legend()
plt.savefig("plotting/figures/Mean energy development for 20x20 with T = 2.4 J.pdf")
plt.show()

# Plotting equilibrium magnetizations for T = 1.
plt.xlabel("$log_{10}$ of Monte Carlo cycles")
plt.ylabel("$<|m|>$")
plt.plot(np.log10(cycles), equiMUT1, label='Unordered')
plt.plot(np.log10(cycles), equiMOT1,color = '#EC5A46', label='Ordered')
plt.legend()
plt.savefig("plotting/figures/Mean magnetization development for 20x20 with T = 1 J.pdf")
plt.show()

# Plotting equilibrium magnetizations for T = 2.4.
plt.xlabel("$log_{10}$ of Monte Carlo cycles")
plt.ylabel("$<|m|>$")
plt.plot(np.log10(cycles), equiMUT24, label='Unordered')
plt.plot(np.log10(cycles), equiMOT24,color = '#EC5A46', label='Ordered')
plt.legend()
plt.savefig("plotting/figures/Mean magnetization development for 20x20 with T = 2.4 J.pdf")
plt.show()

