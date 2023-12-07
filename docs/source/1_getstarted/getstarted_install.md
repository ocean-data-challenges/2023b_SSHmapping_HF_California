# Installation

<br> 

<br>  

## _**How to get started ?**_

Clone the data challenge repo: 
```
git clone https://github.com/ocean-data-challenges/2024c_DC_4DMedSea-ESA.git
```
or using SSH: 
```
git clone git@github.com:ocean-data-challenges/2024c_DC_4DMedSea-ESA.git
```

create the data challenge conda environment, named env-dc-global-ose, by running the following command:
```
conda env create --file=dc_environment.yml 
```
and activate it with:

```
conda activate env-dc-4dmedsea-esa
```
then add it to the available kernels for jupyter to see: 
```
ipython kernel install --name "env-dc-4dmedsea-esa" --user
```
finally, select the "env-dc-global-ose" kernel in your notebook with Kernel > Change Kernel.

## You're now good to go ! 

