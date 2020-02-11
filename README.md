# SA_agro_model
Sensitivity analysis of agro-model with Sobol' method .  
Here we present our results in folders results_csv and result_plots . 
![Scheme_of_crop_rotation](https://github.com/mishagrol/SA_agro_model/blob/master/Crop_rotaion.png)
How to start (example with one core):  
1)Install MONICA model (https://github.com/zalf-rpm/monica/wiki/How-to-compile-MONICA-(Linux))  
or use Docker (docker pull mishagasanov/monica-beta)  
2)clone directory  

`git clone https://github.com/mishagrol/SA_agro_model.git`  
`cd SA_agro_model/Sobol_SA_topsoil/N_100`  
`sh monica.sh`  

The scheme of acceleration of model calculation . 
![Scheme_of_crop_rotation](https://github.com/mishagrol/SA_agro_model/blob/master/HPC_crop_rotation.png)
