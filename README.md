## Overview
This repo shows some of the code that was used in the paper shown at https://www.sciencedirect.com/science/article/pii/S2352710224027347?dgcid=author

The paper goes into depth for the purpose, inspiration, rationale, methodology of the code, so I'll only provide a short summary here.
Generally, the code takes a library of stock elements, calculates each elements' axial force capacity, constructs a force diagram based on 
the predetermined pattern, geometric constraints, and loading. The force diagrams are then used to build a truss spanning 12m. A genetic algorithm
is then used to "cut" the truss members from the available stock while minimizing wasted material. Generally the idea is to generate a user defined number of 
truss designs that have high D/C ratios and can be built from the provided stock library.

## Running the code:

First the required packages should be downloaded, all packages are listed in the requirements.txt file.

Once all the packages have been correctly installed the 'main.py' file can be run which will generate the designs.

## Modifiable parameters

* polyNum - Number of polygons to be in the design (options are only 6, 10 and 14) defined in 'main.py'

* 'ang[1,2]Crit' - 2D array of acceptable angle criteria. Note that modifying these numbers may result in designs that are not feasible. Located in the polygons object that is defined in the data<Polygon #>.py files. Each polygon has its own set of angular criteria and can be directly edited.

## Comments
I am still commenting on the code, so if something doesnt make sense reach out.
