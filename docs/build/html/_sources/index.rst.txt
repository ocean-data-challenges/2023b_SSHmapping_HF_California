.. 2023b_SSHmapping_HF_California documentation master file, created by
   sphinx-quickstart on Fri Jul 21 14:53:11 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
    
    
=====================================
Mapping and separation Data Challenge
=====================================

.. role:: raw-html(raw)
    :format: html 

.. image:: _static/DC_HF_California_mapping-banner.png
    :width: 1200

:raw-html:`<br />`
   
Context and Motivation
======================
  
The goal is to investigate how to best reconstruct sequences of Sea Surface Height (SSH) maps and separate the balanced motions and the internal waves in the Californian SWOT cross-over from artificial SWOT satellite and conventional nadir altimetry observations. This data challenge follows an **Observation System Simulation Experiment** framework: "reference" full SSH are from a numerical simulation with a realistic, high-resolution ocean circulation model: the reference simulation. Satellite observations are simulated by sampling the reference simulation based on realistic orbits of past, existing or future altimetry satellites. A baseline reconstruction method is provided (see below) and the practical goal of the challenge is to beat this baseline according to scores also described below and in Jupyter notebooks.



.. image:: _static/DC-illustration_CaliXover.png
    :width: 500  
    :align: center

Data Challenge setup
====================
 
Reference simulation 
--------------------

The reference simulation is the MITgcm LLC4320 simulation. The simulation is run with tidal forcing. The SSH maps are available hourly. The barotropic tide and the dac have been removed from the reference run. Also, the balanced motions and the internal waves have been seperated using spatio-temporal filters
 
 

Observations
------------
The SSH observations are SWOT and conventional nadirs altimeter data simulated on the reference run. Hence, the barotropic tide is also not present in the SWOT observations. 


Three mapping experiments can be performed using SWOT: 
- without observation errors: **SWOT no noise** ('ssh_model' variable), 
- with KaRIn errors only: **SWOT KaRIn noise** ('ssh_karin' variable),
- with all observation errors: **SWOT all noise** ('ssh_obs' variable).

.. image:: _static/DC_illust_swot_calXover.png
    :width: 500  
    :align: center

As an illustration, see the [`demo_perform_oi`](https://github.com/SammyMetref/2022a_mapping_HFdynamic/blob/master/notebooks/demo_perform_oi.ipynb) notebook that performs an OI reconstruction in these three experiments. 
 
Data sequence and use
---------------------
 
The SSH reconstructions are assessed over the period from 2012-02-01 to 2012-04-30: 89 days.
For reconstruction methods that need a spin-up, the **observations** can be used from 2012-01-04 until the beginning of the evaluation period. This spin-up period is not included in the evaluation. For reconstruction methods that need learning from full fields, the **reference data** and the **observations** can be used from 2012-06-01 to 2012-10-29. The reference data between 2012-05-01 and 2012-05-31 should never be used so that any learning period or other method-related-training period can be considered uncorrelated to the evaluation period.

.. image:: _static/DC-data_availability.png
    :width: 1200

  
Evaluation
---------- 

The metrics used to evaluate the mapping and separation are: 


 
 

:raw-html:`<br />`
 
    
.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Get started

   1_getstarted/getstarted_install.md
   1_getstarted/getstarted_navigate.md
   1_getstarted/getstarted_data.md 
   1_getstarted/getstarted_eval.md
 
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Scripts

   6_scripts/modules.rst

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Metrics details

   5_metrics_det/metrics_balancedmotion.md