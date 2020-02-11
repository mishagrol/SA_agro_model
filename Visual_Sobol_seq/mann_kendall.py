import numpy as np
from scipy.special import erf

# Mann-Kendall test and associated plotting functions
# In here sampled states are a 2D where each line is an ensemble member and each column is a variable


# Mann-Kendall test (precision is the number of decimals)
# Outputs are the normalized statistic Z and the associated p-value
def mann_kendall_test(y, prec):

    n = len(y)
    x = np.int_(y*(10**prec))

    # Sign matrix and ties
    sm = np.zeros((n-1, n-1))
    for i in range(n-1):
        sm[i, i:n] = np.sign(x[i+1:n]-x[0:n-1-i])

    # Compute MK statistic
    s = np.sum(sm)

    # Count ties and their c
    # appel Mimiontributions to variance of the MK statistic
    [val, count] = np.unique(x, return_counts=True)
    [extent, ties] = np.unique(count, return_counts=True)
    tie_contribution = np.zeros(len(ties))
    for i in range(len(ties)):
        tie_contribution[i] = ties[i]*extent[i]*(extent[i]-1)*(2*extent[i]+5)

    # Compute the variance
    vs = (n*(n-1)*(2*n+5) - np.sum(tie_contribution))/18
    if vs < 0:
        print('WARNING: negative variance!!!')

    # Compute standard normal statistic
    z = (s-np.sign(s)) / np.sqrt(max(vs, 1))

    # Associated p-value
    pval = 1 - erf(abs(z) / np.sqrt(2))

    return [z, pval]


# Same as above, but for whole sample
# Outputs are the normalized statistic Z and the associated p-value
def test_sample(sample):

    # Local variables
    n = sample.shape[0]
    var = sample.shape[1]
    x = np.argsort(sample, axis=0)  # Ranks of the values in the ensemble, for each variable
    mk_res = np.zeros((var, var))
    pval = np.zeros((var, var))

    # MK test results
    for i in range(var):
        reorder_sample = np.zeros((n, var))
        for j in range(n):
            reorder_sample[j, :] = sample[x[j, i], :]
        for v in np.arange(i+1, var):
            [mk_res[i, v], pval[i, v]] = mann_kendall_test(reorder_sample[:, v], 5)
            [mk_res[v, i], pval[v, i]] = [mk_res[i, v], pval[i, v]]

    return [mk_res, pval]
