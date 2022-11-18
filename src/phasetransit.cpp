//
//  phasetransit.cpp
//  
//
//  Created by Felix Aarekol Forseth on 15/11/2022.
//

#include <stdio.h>
#include <iostream>
#include <armadillo>
#include "../include/Ising.hpp"
#include "../include/montecarlo.hpp"

int main(int argc, const char * argv[]) {
    // Constants
    int steps = 1e6;
    int burn = 2e5;
    
    //Parallelization loop. Takes time...
    std::vector<int> Ls = {40,60,80,100};
    int cores = 6;
    int rounds = 5;
    arma::vec Ts = arma::linspace(2.1, 2.4, cores*rounds);
    
    for (int l = 0; l < Ls.size(); l++){
        for (int j = 0; j < rounds; j++){ // for four steps.
            std::cout << j << std::endl;
            #pragma omp parallel for
            for (int i = j*cores; i < j*cores+cores; i++){ // for each core
                Isingmodel I(Ls[l]);
                I.initialize_model();
                MonteCarlo M(steps, Ts(i), std::to_string(Ls[l]) + ".txt");
                M.solver(I, true, false, false, burn);
            }
        }
    }
    
    return 0;
}
