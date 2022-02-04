 
# High frequency dynamic mapping Data Challenge 2022a

This repository contains codes and sample notebooks of a data challenge for downloading and processing the high frequency SSH mapping with artificial SWOT data in the Californian SWOT X-over.

![Data Sequence](figures/DC-illustration_CaliXover.png)

The quickstart demo_oi can be run online by clicking here:
[![Colab](figures/logo_colab.png=30x20)](https://colab.research.google.com/drive/1ddJqtmcLAVf4QqFNx34MwLVK0fEJfJV6?usp=sharing)


## Motivation

The goal is to investigate how to best reconstruct sequences of Sea Surface Height (SSH) maps in the Californian SWOT cross-over from artificial SWOT satellite altimetry observations. This data challenge follows an _Observation System Simulation Experiment_ framework: "reference" full SSH are from a numerical simulation with a realistic, high-resolution ocean circulation model: the reference simulation. Satellite observations are simulated by sampling the reference simulation based on realistic orbits of past, existing or future altimetry satellites. A baseline reconstruction method is provided (see below) and the practical goal of the challenge is to beat this baseline according to scores also described below and in Jupyter notebooks.

### Reference simulation
The reference simulation is the MITgcm simulation. The simulation is run with tidal forcing. 

### Observations
The SSH observations are SWOT altimeter data. This nadir altimeters constellation was operating during the 2003-2005 period and is still considered as a historical optimal constellation in terms of spatio-temporal coverage. The data challenge simulates the addition of SWOT to this reference constellation. No observation error is considered in this challenge.

### Data sequence and use
 
The SSH reconstructions are assessed over the period from 2012-02-01 to 2012-04-30: 42 days.
For reconstruction methods that need a spin-up, the **observations** can be used from 2012-10-01 until the beginning of the evaluation period (21 days). This spin-up period is not included in the evaluation. For reconstruction methods that need learning from full fields, the **reference data** can be used from 2013-01-02 to 2013-09-30. The reference data between 2012-12-02 and 2013-01-02 should never be used so that any learning period or other method-related-training period can be considered uncorrelated to the evaluation period.

![Data Sequence](figures/DC-data_availability.png)

## Leaderboard

| Method     |   µ(RMSE) |   σ(RMSE) |   λx (degree) |   λt (days) | Notes                     | Reference        |
|:-----------|------------------------:|---------------------:|-------------------------:|-----------------------:|:--------------------------|:-----------------|
| OI SWOT no noise |                    0.62 |                 0.01 |                      4.4 |                  38.93 | Covariances not optimized | quickstart.ipynb |
| | | | | | | |
| OI SWOT KaRIn noise |                    0.64 |                 0.01 |                     4.44 |                  39.06 | Covariances not optimized | quickstart.ipynb |
| | | | | | | |
| OI SWOT all noise |                    0.42 |                 0.03 |                     4.55 |                  38.64 | Covariances not optimized | quickstart.ipynb | 

**µ(RMSE)**: average RMSE score.  
**σ(RMSE)**: standard deviation of the RMSE score.  
**λx**: minimum spatial scale resolved.  
**λt**: minimum time scale resolved. 
 
## Quick start
You can follow the quickstart guide in [this notebook](https://github.com/SammyMetref/2022a_mapping_HFdynamic/blob/master/quickstart_demo_oi.ipynb) or launch it directly from <a href="https://colab.research.google.com/drive/1ddJqtmcLAVf4QqFNx34MwLVK0fEJfJV6?usp=sharing" target="_blank">CoLab</a>.

## Download the data
The data are hosted on TBD .

They are presented with the following directory structure:


## Baseline and evaluation

### Baseline
The baseline mapping method is optimal interpolation (OI), in the spirit of the present-day standard for DUACS products provided by AVISO. OI is implemented in the [`baseline_oi`](https://github.com/ocean-data-challenges/2020a_SSH_mapping_NATL60/blob/master/notebooks/baseline_oi.ipynb) Jupyter notebook. The SSH reconstructions are saved as a NetCDF file in the `results` directory. The content of this directory is git-ignored.
   
### Evaluation

The evaluation of the mapping methods is based on the comparison of the SSH reconstructions with the *reference* dataset. It includes two scores, one based on the Root-Mean-Square Error (RMSE), the other based on Fourier wavenumber spectra. The evaluation notebook [`example_data_eval`](https://github.com/ocean-data-challenges/2020a_SSH_mapping_NATL60/blob/master/notebooks/example_data_eval.ipynb) implements the computation of these two scores as they could appear in the leaderboard. The notebook also provides additional, graphical diagnostics based on RMSE and spectra.

## Data processing

Cross-functional modules are gathered in the `src` directory. They include tools for regridding, plots, evaluation, writing and reading NetCDF files. The directory also contains a module that implements the baseline method.  

## Acknowledgement

The structure of this data challenge was to a large extent inspired by [ocean data challenge (2020a)](https://github.com/ocean-data-challenges/2020a_SSH_mapping_NATL60).
