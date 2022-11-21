# Ising model solver.

1. Run the makefile to create the main file for execution.

2. Apply 12 command line arguments,
./mainexec L, tstart, tend, datapoints, rounds, cycles, burnin, orderedness, quantities, energies, magnetization, matrix

where,

L = Length of lattice. (int) <br />
tstart = Tempertaure to start at. (float) <br />
tend = Temperature to end at. To run for one temperature use the same as tstart. (float) <br />
datapoints = Number of temperatures to simulate for. Use 1 if your are running one temperature (int) <br />
rounds = Here you should use datapoints/number of cores in your computer, or 1 if you are simulating one temperature. (int) <br />
cycles = Number of monte carlo cycles. (int) <br />
burnin = Number of cycles to discard. (int) <br />
orderedness = If you ising model should start out with spins ordered or unordered. (1 = True, 0 = False) <br />
quantities = Save temperature, mean energy, mean magnetization, heat capacity and susceptibility in a textfile. (1 = True, 0 = False) <br />
energies = Save energy after each cycle in a textfile. (1 = True, 0 = False) <br />
magnetization = Save magnetization after each cycle in a textfile. (1 = True, 0 = False) <br />
matrix = Save ising matrix after number of cycles. <br />
<br />
<br />
The textfiles will be saved in plotting/datafiles. Some example plotting files can be found in the plotting folder, the commands to run them can be found in the makeplot file. 

![alt text](https://img.memegenerator.net/instances/22594340.jpg)

Have fun!
