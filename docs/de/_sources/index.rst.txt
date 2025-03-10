==============================
CoKLIMAx II Projekthintergrund
==============================

Das Projekt **CoKLIMAx - Nutzung von Copernicus-Daten zur klimaresilienten Stadtplanung am Beispiel von Wasser, Wärme und Vegetation** zielt darauf ab, klimaresiliente Stadtplanungsstrategien zu entwickeln, die auf der Nutzung von **Copernicus-Daten und -Informationen** basieren. Angesichts der zunehmenden Herausforderungen durch den Klimawandel - wie steigende Temperaturen, häufigeres Auftreten von Extremwetterereignissen und deren Auswirkungen auf die städtische Infrastruktur und Bevölkerung - fokussiert das Projekt darauf, **technische Werkzeuge und Arbeitsprozesse zu schaffen**, die den Zugang und die Nutzung relevanter Klima- und Umweltdaten für kommunale Akteure vereinfachen. Ziel ist es, **Kommunen fundierte Entscheidungsgrundlagen bereitzustellen**, um den Herausforderungen des Klimawandels - insbesondere in den Bereichen **Wärme, Wasser und Vegetation** - effektiv zu begegnen.

Dafür werden **niedrigschwellige Werkzeuge und effiziente Arbeitsprozesse zur Datenerfassung, -verarbeitung, - auswertung und -anwendung entwickelt**. Ein zentrales Element ist die **AMCDS-Toolbox**, die Copernicus-Daten mit lokalen Informationen kombiniert und so Planungsprozesse unterstützt. Dabei sollen nicht nur technische Lösungen entwickelt werden, sondern auch **die organisatorischen und planerischen Prozesse in Kommunen optimiert werden, um die Entscheidungsfindung und Umsetzung von Klimaanpassungsmaßnahmen zu erleichtern**. Es leistet somit einen wichtigen Beitrag zur Förderung der Klimaresilienz und nachhaltigen Stadtentwicklung.

**Förderkennzeichen:**

  * 50EW2103 - CoKLIMAx (Phase I):  11.2024 - 10.2024
  * 50EW2410 - CoKLIMAx (Phase II): 10.2024 - 05.2025


*Gefördert im Rahmen der Förderrichtlinie „Entwicklung und Implementierungsvorbereitung von Copernicus Diensten für den öffentlichen Bedarf zum Thema Klimaanpassungsstrategien für kommunale Anwendungen in Deutschland“. des Bundesministeriums für Digitales und Verkehr (BMDV).*

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