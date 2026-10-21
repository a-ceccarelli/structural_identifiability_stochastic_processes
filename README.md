# Structural identifiability of partially-observed stochastic processes: from single-particle trajectories to total particle density data

This repository contains the code associated with the manuscript:

**Arianna Ceccarelli, Alexander P. Browning and Ruth E. Baker (2026).**  
*Structural identifiability of partially-observed stochastic processes: from single-particle trajectories to total particle density data.*
https://arxiv.org/abs/2605.13504

## Overview

The manuscript investigates the structural identifiability of velocity-jump stochastic processes under different observation schemes, considering both individual particle trajectories and total particle density data.

This repository contains Python code for numerical simulations and figure generation, together with Mathematica notebooks for symbolic calculations supporting the structural identifiability analysis.

## Repository contents

### Numerical simulations and figures

The `.ipynb` files contain the numerical simulations and figures, which use Python, and require the installation of the libraries NumPy, SciPy, Matplotlib and Pandas.

The following directories contain the code and files associated with figures in the main manuscript and supplementary material.

| Directory | Corresponding figures |
|---|---|
| `FIGURE_1/` | Figure 1 |
| `FIGURE_2/` | Figure 2 |
| `FIGURE_S2_S3A/` | Supplementary Figures S2 and S3A |
| `FIGURE_S3/` | Supplementary Figure S3 |
| `FIGURE_S4/` | Supplementary Figure S4 |
| `FIGURE_S5/` | Supplementary Figure S5 |

The file `functions.py` contains functions for simulating velocity-jump processes, including random initial conditions, switching between states, discrete-time observations and optional Gaussian observation noise.

The repository also contains the following files, generated using Apple Grapher (macOS):

- `FIGURE_3A.gcx` and `FIGURE_3B.gcx`: graphical files associated with Figure 3.
- `FIGURE_S1.gcx`: graphical file associated with Supplementary Figure S1.


### Mathematica notebook

The following Wolfram Mathematica notebooks contain symbolic calculations supporting the structural identifiability analysis presented in the manuscript and supplementary material. 
The `.nb` files can be opened and evaluated in Mathematica, while the corresponding `.pdf` files provide a readable version of the calculations without requiring Mathematica.

| File | Description |
|---|---|
| `Section_4.1_coefficients_c1-c8.nb` | Derivation and verification of the coefficients c<sub>1</sub>, ..., c<sub>8</sub> of the scalar input-output PDE for the total particle density, as presented in Section 4.1. |
| `Section_4.1_S5_example_A_and_equivalent.nb` | Calculations associated with Example A and the construction of distinct parameter sets yielding the same input-output PDE coefficients, as discussed in Section 4.1 and Supplementary Section S5. |
| `Section_4.2_locally_SI_coefficients.nb` | Symbolic calculations supporting the local structural identifiability analysis in Section 4.2, including the additional coefficients obtained from the initial conditions and the determination of equivalent parameter sets. |
| `Section_S4_v2=v3.nb` | Calculations for the case of coinciding velocities, v<sub>2</sub> = v<sub>3</sub>, supporting the identifiability analysis of this special case in the Supplementary Information Section S4. |

Each Mathematica notebook is accompanied by a PDF version with the same filename.
