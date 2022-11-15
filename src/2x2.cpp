//
//  2x21.cpp
//  
//
//  Created by Felix Aarekol Forseth on 15/11/2022.
//

#include <iostream>
#include <armadillo>
#include "../include/Ising.hpp"
#include "../include/montecarlo.hpp"

int main(int argc, const char * argv[]) {
    // Constants
    double T1 = 1;
    double T24 = 2.4;
    int steps = 1e6;
    
    // 2x2 simulation.
    int L2 = 2;
    Isingmodel I1(L2);
    I1.initialize_model();
    MonteCarlo M1(steps, T1, "T12x2.txt");
    M1.solver(I1, false, true, true, 0);
    
    return 0;
}
