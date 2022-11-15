//
//  20x20.cpp
//  
//
//  Created by Felix Aarekol Forseth on 15/11/2022.
//

#include <stdio.h>
#include "../include/Ising.hpp"
#include "../include/montecarlo.hpp"

int main(int argc, const char * argv[]) {
    // Constants
    double T1 = 1;
    double T24 = 2.4;
    int steps = 1e6;
    
    // 20x20 simulation, shorter sim to illustrate burn-in-time.
    int L2 = 20;
    int steps20x = 200000;
    
    // unordered.
    Isingmodel I2T1U(L2);   // 20x20, unordered, T1
    Isingmodel I2T24U(L2);   // 20x20, unordered, T24
    I2T1U.initialize_model();
    I2T24U.initialize_model();
    MonteCarlo MT1U(steps20x, T1, "20x20_T1_UOrdered.txt");
    MonteCarlo MI2T24U(steps20x, T24, "20x20_T24_UOrdered.txt");
    MT1U.solver(I2T1U, false, true, true,0);
    MI2T24U.solver(I2T24U, false, true, true,0);
     
    // ordered.
    Isingmodel I2T1O(L2);   // 20x20, unordered, T1
    Isingmodel I2T24O(L2);   // 20x20, unordered, T24
    I2T1O.initilize_ordered();
    I2T24O.initilize_ordered();
    MonteCarlo MT1O(steps20x, T1, "20x20_T1_Ordered.txt");
    MonteCarlo MI2T24O(steps20x, T24, "20x20_T24_Ordered.txt");
    MT1O.solver(I2T1O, false, true, true,0);
    MI2T24O.solver(I2T24O, false, true, true,0);
    
    // 20x20 simulation, estimate energy functions.
    Isingmodel I4T1(L2);   // 20x20, unordered, T1
    Isingmodel I4T24(L2);   // 20x20, unordered, T24
    I4T1.initialize_model();
    I4T24.initialize_model();
    MonteCarlo M4T1(steps, T1, "20x20_T1energy.txt");
    MonteCarlo M4T24(steps, T24, "20x20_T24energy.txt");
    M4T1.solver(I4T1, false, true, false,0);
    M4T24.solver(I4T24, false, true, false,0);
    
    return 0;
}

