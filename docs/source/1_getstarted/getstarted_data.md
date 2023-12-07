
# Download the data

## Data information

The data are available [here](https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/MEOM/OCEAN_DATA_CHALLENGES/2023b_SSHmapping_HF_California/catalog.html). They are presented with the following directory structure:

- dc_obs_swot/: SWOT data, observations from SWOTsimulator on MITgcm reference;

```
.
|-- dc_obs_swot
|   |--    SSH_SWOT_XXXXXX.nc

```
where XXXXX are the dates specifications.

- dc_obs_nadirs/: conventional nadirs data, observations from SWOTsimulator on MITgcm reference;

```
.
|-- dc_obs_nadirs/*/
|   |-- SSH_NADIR_XXXXX.nc

```
where * can be one of the available satellites: swot/ (which is the swot nadir), alg/, c2/, j3/, s3a/ and s3b/ ; and XXXXX dates specifications.


- dc_ref_eval: evaluation data, SSH reference from MITgcm during the evaluation period;

```
|-- dc_ref_eval
|   |-- 2023b_SSHmapping_HF_California_eval_****-**-**.nc

where ****-**-** stands for year, month and day. 
```

<!--
- dc_mod: training/validation data, SSH MITgcm outside of the evaluation period.
  
```
|-- dc_mod
|   |-- 2022a_SSH_mapping_CalXover_model_****-**-**.nc

where ****-**-** stands for year, month and day. 

```
-->

## Download and read the data


To start out download the *observation* dataset (dc_obs) from the temporary data server, use:
```shell
wget https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/MEOM/OCEAN_DATA_CHALLENGES/2023b_SSHmapping_HF_California/dc_obs_swot.tar.gz
```
and
```shell
wget https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/MEOM/OCEAN_DATA_CHALLENGES/2023b_SSHmapping_HF_California/dc_obs_nadirs.tar.gz
```

the *reference* dataset for the evaluation (dc_ref_eval) using (*this step may take several minutes*):

```shell
wget https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/MEOM/OCEAN_DATA_CHALLENGES/2023b_SSHmapping_HF_California/dc_ref_eval.tar.gz
```
<!--
the *model* dataset for training/validation (dc_ref_eval) using (*this step may take several minutes*):

```shell
wget https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/MEOM/OCEAN_DATA_CHALLENGES/2023b_SSHmapping_HF_California/dc_mod.tar.gz
```
-->

and then uncompress the files using `tar -xvf <file>.tar.gz`. You may also use `ftp`, `rsync` or `curl`to donwload the data.


 

