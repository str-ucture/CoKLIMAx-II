============================================
CoKLIMAx II Ressourcen zur Datenverarbeitung
============================================

Herzlich willkommen in der CoKLIMAx II Dokumentation. Hier finden Sie Informationen und Werkzeuge, die Ihnen den Umgang mit großen Klimadatensätzen in der städischen Verwaltungspraxis erleichtern können. Die Ressourcen sind innerhalb von :ref:`Jupyter Notebooks Bibliothek <jupyter-notebooks-library>` aufgebaut, mit deren Hilfe Sie Klimadaten aus dem Angebot des :ref:`Copernicus Climate Data Store (CDS) <cds>` herunterladen, bearbeiten und visualisieren können.

Im ersten Teil der Dokumentation geht es um die Vorbereitung Ihres Computers auf die Arbeit mit den Daten. Sobald Sie der Anleitung gefolgt sind können Sie loslegen. Um den Umgang mit den CDS-Daten zu lernen können Sie die vorbereiteten Kurs-Elemente durcharbeiten. Für fortgeschritte Nutzende haben wir eine Reihe verschiedener :ref:`Jupyter Notebooks Bibliothek <jupyter-notebooks-library>` vorbereitet, die Sie mit entsprechenden Fähigkeiten nach Belieben modifizieren können. Die Notebooks befassen sich über den CDS hinaus auch mit der Verarbeitung von Satellitendaten, wie zum Beispiel den hochaufgelösten Bildern des Sentinel-II Satelliten. 

.. toctree::
  :maxdepth: 2
  :caption: Inhalte:

  /rst_inhalte/01-softwarekenntnisse
  /rst_inhalte/02-kurselemente
  /rst_inhalte/03-cds

.. toctree::
  :maxdepth: 2
  :caption: Kurs 1:

  /rst_kurs1/01-cds-api-installieren-und-herunterladen
  /rst_kurs1/02-netcdf-einfuhrung

.. toctree::
  :maxdepth: 2
  :caption: Kurs 2:

  /notebooks/kurs2_einfache_cds/01-satellite-lake-water-level
  /notebooks/kurs2_einfache_cds/02-satellite-lake-water-temperature
  /notebooks/kurs2_einfache_cds/03-sis-temperature-statistics

.. toctree::
  :maxdepth: 2
  :caption: The Jupyter Notebook Bibliothek:
  
  /rst_jupyter_bibliothek/index
  /rst_jupyter_bibliothek/cds_data/index
  /rst_jupyter_bibliothek/satellite_data/index
  /rst_jupyter_bibliothek/visualizations/index