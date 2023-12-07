# Download the data

<br> 

<br>  

The data are hosted and can be accessed on the MEOM server opendap [here](https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/MEOM/OCEAN_DATA_CHALLENGES/2024c_DC_4DMedSea-ESA/catalog.html).  

## Data information

The dataset is presented with the following directory structure:

### 1) Data for experiment: obs/

**Nadir alongtrack data (L3 products) for SSH map reconstruction**

```
.
|-- obs
|   |-- alg 
|   |   |-- dt_europe_alg_phy_l3_2017* 
|   |-- c2 
|   |   |-- dt_europe_c2_phy_l3_2017* 
|   |-- j2g 
|   |   |-- dt_europe_j2g_phy_l3_2017* 
|   |-- j2n 
|   |   |-- dt_europe_j2n_phy_l3_2017* 
|   |-- j3 
|   |   |-- dt_europe_j3_phy_l3_2017* 
|   |-- s3a
|   |   |-- dt_europe_s3a_phy_l3_2017* 
``` 

### 2) Data for evaluation: eval/

**Independant nadir alongtrack data (L3 products) for SSH evaluation**

```
.
|-- eval
|   |-- indep_nadirs
|   |   |-- h2ag
|   |   |   |-- dt_europe_h2ag_phy_l3_2017*		% Haiyang-2A (H2A) Drifting Phase Europe Ocean Along track SSALTO/DUACS Sea Surface Height L3 product 
```

**Independant drifters for currents evaluation**

```
.
|-- eval
|   |-- independent_drifters 
```

**Auxiliary data for diagnostics**

```
.
|-- eval
|   |-- sad
|   |-- distance_to_nearest_coastline_60.nc
|   |-- land_water_mask_60.nc
|   |-- variance_cmems_dt_allsat.nc

```

### 3) Data for comparison

**Reconstruction maps for comparison**

```
.
|-- maps
|   |-- DUACS			% DUACS reconstruction with all sat (including evaluation)			
|   |-- MIOST		% MIOST reconstruction 
```


## Download and read the data

The data can be downloaded locally using the wget command. We recommand that the data be stored in the `data/` repository. 
For example, to download and unzip the experiment `obs/` data:


```
cd data/ 
wget https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/MEOM/OCEAN_DATA_CHALLENGES/2024c_DC_4DMedSea-ESA/obs.tar.gz 
tar -xvf obs.tar.gz  
rm -f obs.tar.gz
```

**Example notebook**

A notebook to illustrate how to download and read the global data is available 
 

