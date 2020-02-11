# SA_agro_model
Sensitivity analysis of agro-model with Sobol' method .  
Here we present our results in folders results_csv and result_plots . 
![Scheme_of_crop_rotation](https://github.com/mishagrol/SA_agro_model/blob/master/Crop_rotaion.png)  
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| SOC | right-aligned | $1600 |
| Sand | Soil sand content | $$kg /times kg^{-1}$$| $0.01 | $0.30 |
| Clay | are neat      |    $1 |  
| Clay | are neat      |    $1 |  
| Clay | are neat      |    $1 |  
Parameter &  Description & Unit & Minimum value & Maximum value\\
\hline
| SOC | Soil organic carbon & \%   & 2.58 & 6.20\\
|Sand & Soil sand fraction & $kg*kg^{-1}$ & 0.01 & 0.30\\
| Clay &  Soil clay fraction & $kg*kg^{-1}$& 0.01 & 0.30\\
pH} &  Soil pH value & - & 4.6 & 6.9\\
CN} & Soil carbon:nitrogen ratio & - & 10.9 & 12.4\\
BD} & Soil bulk density & $kg*m^{-3}$& 900.0 & 1350.0\\

How to start (example with one core):  
1)Install MONICA model (https://github.com/zalf-rpm/monica/wiki/How-to-compile-MONICA-(Linux))  
or use Docker (docker pull mishagasanov/monica-beta)  

[]http://SALib.github.io/SALib/  
  
3)clone directory and run shell script  

`git clone https://github.com/mishagrol/SA_agro_model.git`  
`cd SA_agro_model/Sobol_SA_topsoil/N_100`  
`sh monica.sh`  

The scheme of acceleration of model calculation . 
![Scheme_of_crop_rotation](https://github.com/mishagrol/SA_agro_model/blob/master/HPC_crop_rotation.png)
