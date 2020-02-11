#!/usr/bin/env python
#!/trinity/shared/opt/python-3.7.1/bin/python3.7
# coding: utf-8
import numpy as np
import pandas as pd
import json
import pickle
import csv
from pandas.io.json import json_normalize
import scipy
import SALib
from SALib.sample import saltelli
import os
import subprocess

def writting_files(str_values):
    soc1,soc2,soc3,soc4,soc5,soc6,soc7,soc8,soc9 = str_values 
    
    class NpEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            else:
                return super(NpEncoder, self).default(obj)

    site_file = './work_kshen/site-min-kshen.json' #site-min-kshen-3-layers.json'
    sim_file = './work_kshen/sim-min-kshen.json'

    with open(site_file) as sf:
        site_data = json.load(sf)

    with open(sim_file) as simf:
        sim_data = json.load(simf)   

    #selecting necessary keys
    keys = list(site_data['SiteParameters']['SoilProfileParameters'][0].keys())
    our_keys = list(keys.copy()[i] for i in [3])
    
    soc1=soc1
    soc2=soc2
    soc3=soc3
    soc4=soc4
    soc5=soc5
    soc6=soc6
    soc7=soc7
    soc8=soc8
    soc9=soc9

    soil_parameters_names = ['sand10', 'sand20', 'sand30', 'sand40','sand50', 'sand60', 'sand70', 'sand80', 'sand90']

    site_data_copy=site_data.copy()
    #writing main parameters
    site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[0]][0]=float(soc1) 
    site_data_copy['SiteParameters']['SoilProfileParameters'][1][our_keys[0]][0]=float(soc2)
    site_data_copy['SiteParameters']['SoilProfileParameters'][2][our_keys[0]][0]=float(soc3)
    site_data_copy['SiteParameters']['SoilProfileParameters'][3][our_keys[0]][0]=float(soc4)
    site_data_copy['SiteParameters']['SoilProfileParameters'][4][our_keys[0]][0]=float(soc5) 
    site_data_copy['SiteParameters']['SoilProfileParameters'][5][our_keys[0]][0]=float(soc6)
    site_data_copy['SiteParameters']['SoilProfileParameters'][6][our_keys[0]][0]=float(soc7)
    site_data_copy['SiteParameters']['SoilProfileParameters'][7][our_keys[0]][0]=float(soc8)
    site_data_copy['SiteParameters']['SoilProfileParameters'][8][our_keys[0]][0]=float(soc9)

    #constructing file name 
    sand10_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[0]][0])
    sand20_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][1][our_keys[0]][0])
    sand30_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][2][our_keys[0]][0])
    sand40_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][3][our_keys[0]][0])
    sand50_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][4][our_keys[0]][0])
    sand60_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][5][our_keys[0]][0])
    sand70_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][6][our_keys[0]][0])
    sand80_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][7][our_keys[0]][0])
    sand90_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][8][our_keys[0]][0])
    

    file_name = str(sand10_value)+'_'+str(sand20_value)+'_'+str(sand30_value)+'_'+str(sand40_value)+str(sand50_value)\
    +'_'+str(sand60_value)+'_'+str(sand70_value)+'_'+str(sand80_value)+'_'+str(sand90_value)
    site_file_name='site'+'_'+file_name+'.json'

    with open(site_file_name, 'w', encoding='utf-8') as sitef:
        json.dump(site_data_copy, sitef, ensure_ascii=False, indent=4, cls=NpEncoder)

    sim_data_copy=sim_data.copy()
    sim_data_copy['site.json']=site_file_name
    sim_data_copy['output']['file-name']='out'+'_'+file_name+'.csv'
    sim_file_name='sim'+'_'+file_name+'.json'

    with open(sim_file_name, 'w', encoding='utf-8') as simf:
        json.dump(sim_data_copy, simf, ensure_ascii=False, indent=4, cls=NpEncoder)
    os.system('sh monicarunner.sh')

param_values = np.load('batch.npy')
for st in range(len(param_values)):
    writting_files(param_values[st])
