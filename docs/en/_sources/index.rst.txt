============================================
CoKLIMAx II Resources for Data Processing
============================================

Welcome to the CoKLIMAx II documentation. Here you will find information and tools that can facilitate working with large climate datasets in urban administration practice. The resources are structured within :ref:`Jupyter Notebooks <einfuehrung-jupyter>`, which allow you to download, process, and visualize climate data from the :ref:`Copernicus Climate Data Store (CDS) <cds>`. 

The first part of the documentation focuses on preparing your computer for working with the data. Once you have followed the instructions, you can get started. To learn how to work with CDS data, you can go through the prepared course elements. For advanced users, we have prepared a range of different :ref:`Notebooks <einfuehrung-jupyter>` that you can modify as needed based on your skills. The notebooks also cover processing satellite data, such as high-resolution images from the Sentinel-II satellite, beyond the scope of CDS.

.. toctree::
  :maxdepth: 2
  :caption: Contents:

  ./rst_inhalte/SoftwareKenntnisse
  ./rst_inhalte/Kurs-Elemente
  ./rst_inhalte/CDS

.. toctree::
   :maxdepth: 2
   :caption: The Jupyter-Notebook Library:

   ./rst_jupyter/Einfuehrung_Jupyter

.. toctree::
  :maxdepth: 2
  :caption: Course 1:

  ./notebooks/kurs1/herunterladen_ersten_datensatzes
  ./notebooks/kurs1/analysis_and_visualization

.. toctree::
  :maxdepth: 2
  :caption: Course 2:

  ./notebooks/kurs2/01 satellite-lake-water-level
  ./notebooks/kurs2/02 satellite-lake-water-temperature
  ./notebooks/kurs2/03 sis-temperature-statistics

.. toctree::
  :maxdepth: 2
  :caption: Course 3:

  ./notebooks/kurs3/01 senthub_downloader

.. toctree::
  :maxdepth: 2
  :caption: Course Not Defined:

  ./notebooks/kurs_not_defined/01 alpine-monthly-precipitation
  ./notebooks/kurs_not_defined/02 sis-heat-wave-and-cold-spells
  ./notebooks/kurs_not_defined/03 sis-health-vector
  ./notebooks/kurs_not_defined/04 climate-indicators
  ./notebooks/kurs_not_defined/05 sis-biodiversity-era5-regional
  ./notebooks/kurs_not_defined/06 era5_land_hourly
  ./notebooks/kurs_not_defined/07 era5-land-monthly
  ./notebooks/kurs_not_defined/08 landsat-with-landsatxplore
  ./notebooks/kurs_not_defined/09 Sentinel2-without-esri