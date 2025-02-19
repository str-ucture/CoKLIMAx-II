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

  /rst_kurs1/cds-api-installieren-und-herunterladen
  /rst_kurs1/netcdf-einfuhrung

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