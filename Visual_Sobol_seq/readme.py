from SALib.sample import sobol_sequence
from SALib.sample import latin
import mann_kendall
import pearson
import numpy as np
import util
import projection_properties
import space_filling_measures

################################# Intro
# This file demonstrates the functionalities in this quick toolbox fo sample property visualisation
# CLI usage: python readme.py &> output.txt
#################################

################################# Ensemble characteristics
# Ensemble quick definition, following the SAlib standards

n = 100
dim = 7
names = []
for i in range(dim):
    names.append('x' + str(i+1))

problem = {
    'num_vars': dim,
    'names': names,
    'bounds': [[-1, 1]]*dim
}

################################# Examples
# Example: LHS
param_values = latin.sample(problem, n)

# Example: sobol
# sobol_values = sobol_sequence.sample(n, problem['num_vars'])
# param_values = util.scale_to_bounds(sobol_values, problem["bounds"])

# Rescale to the unit hypercube for the analysis
sample = util.scale_normalized(param_values, problem["bounds"])

#################################
# Correlation properties
[z_mk, pval_mk] = mann_kendall.test_sample(sample)
[rho, pval_pr] = pearson.test_sample(sample)
util.correlation_plots(z_mk, pval_mk, 'Mann-Kendall', problem['names'])
util.correlation_plots(rho, pval_pr, 'Pearson', problem['names'])

#################################
# Space-filling properties

# 1D projection
x = projection_properties.projection_1D(sample, problem['names'])
print('\nOn a [0, 1] scale 1D coverage is: ' + str(x))

# 2D projection (manageable number of variables, here fixed at 11)
if problem["num_vars"] < 11:
    projection_properties.projection_2D(sample, problem['names'])

# L2-star discrepancy
dl2 = space_filling_measures.discrepancy(sample)
print('\nL2-star discrepancy is: ' + str(dl2))

# Minimal distance between any two points
d = space_filling_measures.min_distance(sample, 1)
print('\nThe minimal distance between two points is: ' + str(d) + '\n')
