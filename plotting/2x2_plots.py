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
    mean1 = np.mean(magnetizations**2)
    mean2 = (np.mean(abs(magnetizations)))**2
    return (1/N)*(B)*(mean1 - mean2)

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
 
def equilibration_cv(energies, N):
    heat_caps = np.zeros(len(energies))
    for i in range(1, len(energies)):
        heat_caps[i] = spes_heat_cap(energies[:i], N, B, T)
    return heat_caps

def equilibration_sus(magnetizations, N):
    susses = np.zeros(len(magnetizations))
    for i in range(1, len(susses)):
        susses[i] = suceptibility(magnetizations[:i], N, B, T)
    return susses

N = 4
B = 1
T = 1
energies22 = np.loadtxt('plotting/datafiles/energiesT12x2.txt')
m22 = np.loadtxt('plotting/datafiles/magnetizationsT12x2.txt')
cycles = np.linspace(1, 250001, 25000)
equiE22 = equilibration_e(energies22[:250000], N)
equiM22 = equilibration_m(m22[:250000], N)
equiCV22 = equilibration_cv(energies22[:250000], N)
equisus22 = equilibration_sus(m22[:250000], N)
analyticale = -1.9959
analyticalm = 0.9986
analyticalcv = 0.0320
analyticalsus = 0.0040
delta = 0.001
colors = sns.color_palette('pastel')
sns.set_style('darkgrid')

# Find convergance.
absdiffE = np.where(abs(analyticale - equiE22) < delta)[0][0]
absdiffM = np.where(abs(analyticalm - equiM22) < delta)[0][0]
absdiffcv = np.where(abs(analyticalcv - equiCV22) < delta)[0][0]
absdiffsus = np.where(abs(analyticalsus - equisus22) < delta)[0][0]

print(f"Mean energy per spin = {equiE22[absdiffE]} gotten after {absdiffE} cycles.")
print(f"Mean magnetization per spin = {equiM22[absdiffM]} gotten after {absdiffM} cycles.")
print(f"Specific heat capcity = {equiCV22[absdiffcv]} gotten after {absdiffcv} cycles.")
print(f"Susceptibility = {equisus22[absdiffsus]} gotten after {absdiffsus} cycles.")
