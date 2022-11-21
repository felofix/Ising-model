//
//  main.cpp
//  
//
//  Created by Felix Aarekol Forseth on 18/11/2022.
//

#include <stdio.h>
#include <iostream>
#include <armadillo>
#include <cstdlib>
#include "../include/Ising.hpp"
#include "../include/montecarlo.hpp"
#include <thread>

int main(int argc, const char * argv[]) {
    if (argc != 13){ // Checking if there is enough command-line.argumets.
        std::cout << "You have entered to few arguments." << std::endl;
        return 0;
    }
    
    // Constants for overview.
    int L = atoi(argv[1]);
    double tstart = atof(argv[2]);
    double tend = atof(argv[3]);
    int datapoints = atoi(argv[4]);
    int rounds = atoi(argv[5]);
    int cycles = atoi(argv[6]);
    int burnin = atoi(argv[7]);
    int orderedness = atoi(argv[8]);
    int quantities = atoi(argv[9]);
    int energies = atoi(argv[10]);
    int magnetization = atoi(argv[11]);
    int matrix = atoi(argv[12]);
    
    arma::vec Ts = arma::linspace(tstart, tend, datapoints);
    
    for (int j = 0; j < floor(datapoints / rounds); j++){ // for each step.
        #pragma omp parallel for
        for (int i = j*rounds; i < j*rounds+rounds; i++){ // for each core.
            if (orderedness){           // Ordered spins.
                Isingmodel I(L);
                I.initilize_ordered();
                MonteCarlo M(cycles, Ts(i), std::to_string(L) + "_" + "O" + "_" + std::to_string(tstart) + "-" + std::to_string(tend) + ".txt");
                M.solver(I, quantities, energies, magnetization, burnin, matrix);
            }
            else{                      // Unordered spins. 
                Isingmodel I(L);
                I.initialize_model();
                MonteCarlo M(cycles, Ts(i), std::to_string(L) + "_" + "UO" + "_" + std::to_string(tstart) + "-" + std::to_string(tend) + ".txt");
                M.solver(I, quantities, energies, magnetization, burnin, matrix);
            }
        }
    }
    
    return 0;
}
