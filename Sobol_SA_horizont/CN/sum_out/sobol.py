import os
import sys
sys.path.append('/trinity/home/m.gasanov/monica/sensitivity/sobol/SALib')

from SALib.analyze import sobol
from SALib.sample import saltelli
from SALib.test_functions import Ishigami
from SALib.util import read_param_file
from numpy import genfromtxt

# Read the parameter range file and generate samples
#problem = read_param_file('../../src/SALib/test_functions/params/Ishigami.txt')
problem = {
    'num_vars':9,
    'names':['CN_0-30', 'CN_30-40', 'CN_40-50', 'CN_50-60',\
             'CN_60-70', 'CN_70-80', 'CN_80-90', 'CN_90-100', 'CN_100-200'],
    'bounds':[[10.9, 12.4],
              [10.9, 12.4],
              [10.9, 12.4],
              [10.9, 12.4],
              [10.9, 12.4],
              [10.9, 12.4],
              [10.9, 12.4],
              [10.9, 12.4],
              [10.9, 12.4]]
}
#param_values = saltelli.sample(problem, 100000)

# Generate samples
list_os_csv=['soybean-000-2015.csv', 'sugar-beet-2011.csv', 'sugar-beet-2017.csv',
'spring-barley-2012.csv', 'sugar-beet-2014.csv']
# Run the "model" and save the output in a text file
# This will happen offline for external models
#Y = Ishigami.evaluate(param_values)
# Perform the sensitivity analysis using the model output
# Specify which column of the output file to analyze (zero-indexed)
for i in list_os_csv:
    all_data_csv = genfromtxt(str(i), delimiter=',')
    output = all_data_csv[:,2]
    print(i)
    Si = sobol.analyze(problem, output, calc_second_order=True, conf_level=0.95, print_to_console=True)
# Returns a dictionary with keys 'S1', 'S1_conf', 'ST', and 'ST_conf'
# e.g. Si['S1'] contains the first-order index for each parameter,
# in the same order as the parameter file
# The optional second-order indices are now returned in keys 'S2', 'S2_conf'
# These are both upper triangular DxD matrices with nan's in the duplicate
# entries.
# Optional keyword arguments parallel=True and n_processors=(int) for parallel execution
# using multiprocessing

# First-order indices expected with Saltelli sampling:
# x1: 0.3139
# x2: 0.4424
# x3: 0.0
