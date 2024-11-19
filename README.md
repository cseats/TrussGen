## Overview
This repo shows some of the code that was used in the paper shown at https://www.sciencedirect.com/science/article/pii/S2352710224027347?dgcid=author

The paper goes into depth for the purpose, inspiration, rationale, methodology of the code, so I'll only provide a short summary here.
Generally, the code takes a library of stock elements, calculates each elements' axial force capacity, constructs a force diagram based on 
the predetermined pattern, geometric constraints, and loading. The force diagrams are then used to build a truss spanning 12m. A genetic algorithm
is then used to "cut" the truss members from the available stock while minimizing wasted material. Generally the idea is to generate a user defined number of 
truss designs that have high D/C ratios and can be built from the provided stock library.

## Running the code:

