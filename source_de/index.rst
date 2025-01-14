============================================
CoKLIMAx II Ressourcen zur Datenverarbeitung
============================================

Herzlich willkommen in der CoKLIMAx II Dokumentation. Hier finden Sie Informationen und Werkzeuge, die Ihnen den Umgang mit großen Klimadatensätzen in der städischen Verwaltungspraxis erleichtern können. Die Ressourcen sind innerhalb von :ref:`Jupyter Notebooks <einfuehrung-jupyter>` aufgebaut, mit deren Hilfe Sie Klimadaten aus dem Angebot des :ref:`Copernicus Climate Data Store (CDS) <cds>` herunterladen, bearbeiten und visualisieren können. Im ersten Teil der Dokumentation geht es um die Vorbereitung Ihres Computers auf die Arbeit mit den Daten. Sobald Sie der Anleitung gefolgt sind können Sie loslegen. Um den Umgang mit den CDS-Daten zu lernen können Sie die vorbereiteten Kurs-Elemente durcharbeiten. Für fortgeschritte Nutzende haben wir eine Reihe verschiedener :ref:`Notebooks <einfuehrung-jupyter>` vorbereitet, die Sie mit entsprechenden Fähigkeiten nach Belieben modifizieren können. Die Notebooks befassen sich über den CDS hinaus auch mit der Verarbeitung von Satellitendaten, wie zum Beispiel den hochaufgelösten Bildern des Sentinel-II Satelliten. 


.. toctree::
  :maxdepth: 2
  :caption: INHALTE:

  ./rst_intro/notwendige_software_und_kenntnisse
  ./rst_intro/der_kurz_elemente
  ./rst_intro/der_cds
  ./rst_intro/der_jupyter

.. toctree::
  :maxdepth: 2
  :caption: Kurs 1:

  ./notebooks/kurs1/herunterladen_ersten_datensatzes
  ./notebooks/kurs1/analysis_and_visualization

.. toctree::
  :maxdepth: 2
  :caption: Kurs 2:

  ./notebooks/kurs2/01 satellite-lake-water-level
  ./notebooks/kurs2/02 satellite-lake-water-temperature
  ./notebooks/kurs2/03 sis-temperature-statistics

.. toctree::
  :maxdepth: 2
  :caption: Kurs 3:

  ./notebooks/kurs3/01 senthub_downloader

.. toctree::
  :maxdepth: 2
  :caption: Kurs Note Defined:

  ./notebooks/kurs_not_defined/01 alpine-monthly-precipitation
  ./notebooks/kurs_not_defined/02 sis-heat-wave-and-cold-spells
  ./notebooks/kurs_not_defined/03 sis-health-vector
  ./notebooks/kurs_not_defined/04 climate-indicators
  ./notebooks/kurs_not_defined/05 sis-biodiversity-era5-regional
  ./notebooks/kurs_not_defined/06 era5_land_hourly
  ./notebooks/kurs_not_defined/07 era5-land-monthly
  ./notebooks/kurs_not_defined/08 landsat-with-landsatxplore

Before you begin
----------------

Prerequisites (For a better experience)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Python 3.7 or higher**. (`Python 3.10 <https://www.python.org/downloads/release/python-31015/>`_ is recommended)
- An **Integrated Development Environment (IDE)**. (e.g., `Visual Studio Code <https://code.visualstudio.com/>`_)
- **Jupyter Notebook** is installed and accessible within your IDE.
- An active **CDS Account** with API credentials.
    - If you don't have one, register at `CDS Registration Page <https://cds.climate.copernicus.eu/>`_.