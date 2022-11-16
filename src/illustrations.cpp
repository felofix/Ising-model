//
//  illustrations.cpp
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
    double T1 = 1;
    double T24 = 2.4;
    int steps = 1e6;
    
    Isingmodel I2T1U(40);   // 20x20, unordered, T1
    Isingmodel I2T24U(40);   // 20x20, unordered, T24
    
    I2T1U.initialize_model();
    I2T24U.initialize_model();
    
    MonteCarlo MT1U(steps, T1, "dontmatter.txt");
    MonteCarlo MI2T24U(steps, T24, "dontmatter.txt");
    
    MT1U.writematrixtofile(I2T1U, "plotting/datafiles/20x20_T1_spins_start.txt");
    
    MT1U.solver(I2T1U, false, false, false, 0);
    MI2T24U.solver(I2T24U, false, false, false, 0);
    
    MT1U.writematrixtofile(I2T1U, "plotting/datafiles/20x20_T1_spins_end.txt");
    MI2T24U.writematrixtofile(I2T24U, "plotting/datafiles/20x20_T24_spins_end.txt");
    
    return 0;
}
