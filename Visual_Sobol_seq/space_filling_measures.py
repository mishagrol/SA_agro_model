import numpy as np
import matplotlib.pyplot as plt


# Assumes the samle has N points (lines) in p dimensions (columns)
# Assumes sample drawn from unit hypercube of dimension p
# L2-star discrepancy formula from
def discrepancy(sample):

    [n, p] = sample.shape

    # First term of the L2-star discrepancy formula
    dl2 = 1.0/(3.0**p)

    # Second term of the L2-star discrepancy formula
    sum_1 = 0.0
    for k in range(n):
        for i in range(n):
            prod = 1.0
            for j in range(p):
                prod = prod * (1 - max(sample[k, j], sample[i, j]))
            sum_1 = sum_1 + prod
    dl2 += sum_1 / n ** 2

    # Third term of the L2-star discrepancy formula
    sum_2 = 0.0
    for i in range(n):
        prod = 1
        for j in range(p):
            prod *= (1 - sample[i, j]**2)
        sum_2 = sum_2 + prod
    dl2 -= sum_2 * (2**(1-p)) / n

    return dl2


# Returns the minimal distance between two points
# Assumes sample drawn from unit hypercube of dimension p
def min_distance(sample, show):

    n = sample.shape[0]
    dist = np.ones((n, n))  # ones and not zeros because we are interested in abstracting min distance

    # Finding distance between points
    for i in range(n):
        for j in np.arange(i+1, n):
            dist[i, j] = np.sqrt(np.sum((sample[i, :] - sample[j, :])**2))
            dist[j, i] = dist[i, j]  # For the plot

    # If wanted: plots the distribution of minimal distances from all points
    if show == 1:
        plt.plot(np.arange(1, n+1), np.sort(np.amin(dist, axis=1)))
        plt.xlim(1, n)
        plt.xlabel('Sorted ensemble members')
        plt.ylabel('Min Euclidean distance to any other point')
        plt.savefig('Distances.png', dpi=400)
        plt.clf()

    # Space-filling index is minimal distance between any two points
    return np.amin(dist)
