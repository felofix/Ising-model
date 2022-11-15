g++ src/2x2.cpp src/Ising.cpp src/montecarlo.cpp -std=c++11 -larmadillo -Xpreprocessor -fopenmp -o twoXtwo -lomp -O2
g++ src/20x20.cpp src/Ising.cpp src/montecarlo.cpp -std=c++11 -larmadillo -Xpreprocessor -fopenmp -o twentyXtwenty -lomp -O2
g++ src/phasetransit.cpp src/Ising.cpp src/montecarlo.cpp -std=c++11 -larmadillo -Xpreprocessor -fopenmp -o phasetransit -lomp -O2
g++ src/illustrations.cpp src/Ising.cpp src/montecarlo.cpp -std=c++11 -larmadillo -Xpreprocessor -fopenmp -o illustrations -lomp -O2
