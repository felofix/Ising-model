import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def mean_epsilon(energies, N):
	return np.mean(energies/N)

def mean_mag(magnetizations, N):
	return np.mean(abs(magnetizations/N))

def spes_heat_cap(energies, N, B, T):
	return (1/N)*(B/T)*np.var(energies)

def suceptibility(magnetizations, N, B, T):
	return (1/N)*(B)*np.var(magnetizations)

def equilibration_e(energies, N):
	mean_epsilons = np.zeros(len(energies))
	for i in range(1, len(mean_epsilons)):
		mean_epsilons[i] = mean_epsilon(energies[:i], N)
	return mean_epsilons

def equilibration_m(magnetizations, N):
	mean_mags = np.zeros(len(magnetizations))
	for i in range(1, len(mean_mags)):
		mean_mags[i] = mean_mag(magnetizations[:i], N)
	return mean_mags

n1 = 4
energies22 = np.loadtxt('plotting/datafiles/energiesT12x2.txt')
m22 = np.loadtxt('plotting/datafiles/magnetizationsT12x2.txt')
cycles = np.linspace(0, 10000, 10000)
equiE22 = equilibration_e(energies22[:10000], n1)
equiM22 = equilibration_m(m22[:10000], n1)
analyticale = -2
analyticalm = 1
delta = 0.002
colors = sns.color_palette('pastel')
sns.set_style('darkgrid')

# Find convergance.
absdiffE = np.where(abs(analyticale - equiE22) < delta)[0][0]
absdiffM = np.where(abs(analyticalm - equiM22) < delta)[0][0]

# Plotting equilibrium energies.
plt.xlabel("Monte Carlo cycles")
plt.ylabel("$<\epsilon> [J]$")
plt.axhline(y = analyticale, color = '#EC5A46', linestyle='--', label=f'$<\epsilon>$ = -2 [J]')
plt.plot(cycles, equiE22)
plt.plot(absdiffE, equiE22[absdiffE], 'bo', label='Absolute error < 0.002')
plt.legend()
plt.savefig("plotting/figures/Mean energy development for 2x2.pdf")
plt.show()

# Plotting equilibrium magnetizations.
plt.xlabel("Monte Carlo cycles")
plt.ylabel("$<|m|>$")
plt.axhline(y = analyticalm, color = '#EC5A46', linestyle='--', label=f'$<\|m|>$ = 1 [J]')
plt.plot(cycles, equiM22)
plt.plot(absdiffM, equiM22[absdiffM], 'bo', label='Absolute error < 0.002')
plt.legend()
plt.savefig("plotting/figures/Mean magnetization development for 2x2.pdf")
plt.show()
