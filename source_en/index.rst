======================
CoKLIMAx II Background
======================

The **CoKLIMAx project** aims to develop climate-resilient urban planning strategies based on **Copernicus data and information**. In response to the growing challenges of climate change—such as rising temperatures, increasing occurrences of extreme weather events, and their impact on urban infrastructure and populations—the project focuses on creating **technical tools and workflows** that facilitate access to and use of relevant climate and environmental data for municipal stakeholders. The goal is to **provide municipalities with well-founded decision-making tools** to effectively address climate change challenges, particularly in the areas of **heat, water, and vegetation**.

To achieve this, **low-threshold tools and efficient processes for data collection, processing, analysis, and application are being developed**. A key component is the **AMCDS-Toolbox**, which integrates Copernicus data with local information to support urban planning processes. Beyond technical solutions, the project also aims to **optimize organizational and planning processes within municipalities** to facilitate decision-making and the implementation of climate adaptation measures.
By doing so, **CoKLIMAx makes an important contribution to promoting climate resilience and sustainable urban development.**

**Funding Reference:**

  * 50EW2103 - CoKLIMAx (Phase I):  11.2024 - 10.2024
  * 50EW2410 - CoKLIMAx (Phase II): 10.2024 - 05.2025

*Funded under the directive "Development and Implementation Preparation of Copernicus Services for Public Needs on Climate Adaptation Strategies for Municipal Applications in Germany" by the German Federal Ministry for Digital and Transport (BMDV).*

=========================================
CoKLIMAx II Resources for Data Processing
=========================================

Welcome to the CoKLIMAx II Documentation. Here you will find information and tools that can help you deal with large climate datasets in urban management practice. The resources are structured within :ref:`Jupyter Notebooks Library <jupyter-notebooks-library>`, which allow you to download, edit, and visualize climate data from the :ref:`Copernicus Climate Data Store (CDS) <cds>`. 

The first part of the documentation focuses on preparing your computer for working with the data. Once you have followed the instructions, you can get started. To learn how to work with CDS data, you can go through the prepared course elements. For advanced users, we have prepared a range of different notebooks within a :ref:`Jupyter Notebook Library <jupyter-notebooks-library>` that you can modify as needed baszced on your skills. In addition to CDS, the notebooks also cover processing satellite data, such as high-resolution images from the Sentinel-II satellite.

.. toctree::
  :maxdepth: 2
  :caption: Contents:

  /rst_inhalte/01-softwarekenntnisse
  /rst_inhalte/02-kurselemente
  /rst_inhalte/03-cds

.. toctree::
  :maxdepth: 2
  :caption: Course 1:

  /rst_kurs1/01-cds-api-installieren-und-herunterladen
  /rst_kurs1/02-netcdf-einfuhrung

.. toctree::
  :maxdepth: 2
  :caption: Course 2:

  /notebooks/kurs2_einfache_cds/01-satellite-lake-water-level
  /notebooks/kurs2_einfache_cds/02-satellite-lake-water-temperature
  /notebooks/kurs2_einfache_cds/03-sis-temperature-statistics

.. toctree::
  :maxdepth: 2
  :caption: The Jupyter Notebook Library:
  
  /rst_jupyter_bibliothek/index
  /rst_jupyter_bibliothek/cds_data/index
  /rst_jupyter_bibliothek/satellite_data/index
  /rst_jupyter_bibliothek/visualizations/index