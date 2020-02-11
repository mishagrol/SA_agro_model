#!/usr/bin/env python
# coding: utf-8

# In[136]:


import numpy as np
import scipy
import matplotlib
import pandas as pd
from numpy import genfromtxt
import json
import sys
from SALib.sample import saltelli
from SALib.analyze import sobol
import subprocess


# In[138]:


problem = {
    'num_vars':9,
    'names':['sand10', 'sand20', 'sand30', 'sand40',\
             'sand50', 'sand60', 'sand70', 'sand80', 'sand90'],
    'bounds':[[0.01, 0.30],
              [0.01, 0.30],
              [0.01, 0.30],
              [0.01, 0.30],
              [0.01, 0.30],
              [0.01, 0.30],
              [0.01, 0.30],
              [0.01, 0.30],
              [0.01, 0.30]]
}
param_values = saltelli.sample(problem, 100000)


# In[139]:


#create a lot of batch files (small arrays)
batches =np.split(param_values, 100)


# In[152]:


# make list with names for arrays files (.npy)
list_of_batch=[]
for i in range(100,200):
    list_of_batch.append('batch'+str(i)+'.npy')


# In[142]:


# save batch arrays to local directory
for name, img in zip(list_of_batch, batches):
    np.save(name, img)

