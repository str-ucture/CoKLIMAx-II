.. _kurs1-cds-api-installation-and-download:

=================================
CDS API Installation und Download
=================================

---------
Lernziele
---------

* :ref:`Einrichtung der API des Copernicus Climate Data Store (CDS API) <setup-api>`
	* :ref:`Persönlicher API-Key <personal-api-key>`
	* :ref:`Installation der CDS-API <install-cds-api>`
* :ref:`Download des ersten Klima-Datensatzes <cds-download>`
	* :ref:`Erstellen der API-Request <api-request>`
	* :ref:`Die API-Request im Jupyter Notebook <api-jupyter>`

----

Wir haben für Sie ein Jupyter Notebook vorbereitet, bei dem Sie lediglich den Ausgabeordner und Ihren API-Schlüssel anpassen müssen. Das Notebook können Sie unter folgendem Link herunterladen:

.. raw:: html

   <div class="download-button">
       <a href="../_static/notebooks/cds-api-installieren-und-herunterladen.ipynb" download>⇩ CDS API Installation und Download (Notebook)</a>
   </div>

Öffnen Sie das Notebook in Jupyter Lab und folgen Sie den Anweisungen. Alternativ können Sie den Python-Codeausschnitt in Ihr Jupyter-Notebook kopieren und die Zellen ausführen.

.. image:: /_static/gif/01-tutorial-02.gif
   :width: 600px
   :align: center
   :class: no-scaled-link

----

.. _setup-api:

-----------------------
Einrichtung der CDS API
-----------------------

Zur Einrichtung der CDS API (Application Programming Interface, notwendige Installation um Daten aus dem CDS herunterzuladen) benötigen Sie einen Nutzeraccount im Copernicus Climate Data Store (CDS). Diesen richten Sie direkt über den `CDS <https://cds.climate.copernicus.eu/>`_ ein.

Falls Sie noch keinen Nutzeraccount haben erstellen Sie sich einen Account über die Startseite. Oben rechts im Fenster klicken Sie auf **"Login - Register"**. Das Dialogfenster erscheint wie unten angezeigt. Erstellen Sie sich einen ECMWF-Account wie beschrieben und loggen Sie sich dann mit Ihrem ECMWF-Nutzernamen und Passwort im Copernicus CDS ein.

.. image:: /_static/03-kurs-1-cds-1.png
	:width: 600px
	:align: center
	:class: no-scaled-link
	:alt: CDS Login - Register

.. _personal-api-key:

^^^^^^^^^^^^^^^^^^^^^^^
1. Persönlicher API-Key
^^^^^^^^^^^^^^^^^^^^^^^

Nach dem Login können Sie sich in Ihrem Account Ihre API-Informationen ansehen. Den API-Key (oder API-Token) benötigen Sie im nächsten Schritt.

.. image:: /_static/03-kurs-1-cds-2.png
	:width: 600px
	:align: center
	:class: no-scaled-link
	:alt: CDS Profile

Scrollen Sie nach unten zum Abschnitt **API-Token** und klicken Sie auf die Schaltfläche „Kopieren“, um Ihren API-Key zu kopieren. Öffnen Sie als Nächstes das **CDS API Installation and Download Notebook** und ersetzen Sie den vorhandenen Schlüssel bei ``api_key = "Ihr persönlicher API-Key"``.

.. image:: /_static/03-kurs-1-cds-3.png
   :width: 600px
   :align: center
   :class: no-scaled-link
   :alt: CDS API key

Alternativ können Sie den folgenden Code kopieren und den API-Schlüssel ersetzen:

	.. code-block:: python
		
		import cdsapi
		api_key = "Ihr persönlicher API-Key"
		api_url = "https://cds.climate.copernicus.eu/api"

.. _install-cds-api:

^^^^^^^^^^^^^^^^^^^^^^^^^^^
2. Installation der CDS API
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nun sind Sie bereit, die CDS API zu installieren. Öffnen Sie die CMD (Eingabeaufforderung) und geben Sie folgenden Befehl ein

	.. code-block:: shell

		pip install cdsapi

Sie sollten nun alle Voraussetzungen erfüllt haben um Daten aus dem CDS herunterzuladen. Im nächsten Schritt probieren wir dies mit einem Testdatensatz aus.

----

.. _cds-download:

-----------------------------------
Download von Klimadaten aus dem CDS
-----------------------------------

Unser Testdatensatz ist der **Reanalyse-Datensatz ERA5**. Falls Sie sich mit dem Datensatz gut auskennen, können Sie den Infokasten überspringen und gleich zum :ref:`nächsten Schritt <api-request>` übergehen.

.. note::
	Der ERA5-Klimadatensatz ist eine umfangreiche Sammlung von Wetter- und Klimadaten, die von der 	Europäischen Organisation für die Nutzung meteorologischer Satelliten (ECMWF) erstellt wurde. Es 	handelt sich dabei um eine historische Wetter- und Klimadatenbank, die auf modernen Rechenmodellen und 	Satellitenmessungen basiert. ERA5 umfasst kontinuierliche Wetterdaten der letzten Jahrzehnte, von 1950 	bis in die Gegenwart. Diese Daten umfassen unter anderem Temperatur, Luftfeuchtigkeit oder 	Windgeschwindigkeit.

	In Wissenschaft und Klimaforschung wird der ERA5-Datensatz genutzt, um langfristige Klimatrends zu 	untersuchen. Zum Beispiel kann anhand der Daten analysiert werden, wie sich die Temperaturen im 	Verlauf von Jahrzehnten verändert haben oder wie sich die Frequenz von Extremwetterereignissen 	entwickelt.

	Kurz gesagt, der ERA5-Datensatz ist eine wertvolle Wissensquelle für viele verschiedene Disziplinen 	und Bereiche, weil er fundierte und verlässliche Daten für die Analyse des globale Klimasystems 	bereitstellt. Der ERA5-Datensatz dient auch als Grundlage für die Entwicklung von Klimamodellen und 	Wettervorhersagen. Er hilft, genauere und realistischere Prognosen zu erstellen, was für zukünftiges 	Risikomanagement relevant ist.

.. _api-request:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Erstellen der API-Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Die im CDS verfügbaren Datensätze können durch die räumliche und zeitliche Abdeckung schnell mehrere Gigabyte Größe erreichen. Im CDS haben Sie die Möglichkeit, individuell Variablen, Zeiträume und Regionen auszwählen, damit der Datensatz nicht unnötig Speicherplatz auf Ihrem Computer verbraucht. Für den Test laden wir nur einen kleinen Teil des Datensatzes herunter (eine Variable für einen Tag im Oktober 2024).

Um die gewünschten Daten automatisiert über die CDS API herunterzuladen müssen Sie zunächst einen API request code erzeugen. Dafür gehen Sie in den Copernicus Climate Data store, loggen sich ein und suchen nach dem Datensatz `ERA5-Land hourly data from 1950 to present <https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview>`_

Gehen Sie auf den `Download <https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=download>`_ tab und wählen Sie die Parameter wie folgt aus:

	* **Temperature**: 2m temperature
	* **Year**: 2024
	* **Month**: October
	* **Day**: 01
	* **Time**: Select all

Die Region Ihrer Wahl könnnen Sie im Bereich **"Geographical Area"** festlegen. Dies sollten Sie tun, damit der Datensatz nicht für den gesamten, verfügbaren Bereich heruntergeladen wird.

Wir haben für Sie die Koordinaten für die Region rund um den Bodensee vorbereitet, der Test-Region des CoKLIMAx-Projekts.

.. image:: /_static/04-kurs-1-cds-4.png
	:width: 600px
	:align: center
	:class: no-scaled-link
	:alt: Download Region

.. note::
	Ihre eigenen Wunschkoordinaten können Sie sich ganz einfach im von uns entwickelten `Bbox-Generator <https://str-ucture.github.io/bbox-extractor/>`_ erstellen. Kopieren Sie sich die Koordinaten in die Zwischenablage oder in ein Textdokument. Diese können später auch noch direkt im Jupyter-Notebook eingegeben werden. Alternativ können Sie den Begrenzungsrahmenwert in ``"area": ​​[48.7, 7, 47.1, 11]`` aktualisieren, um den Datenumfang zu definieren, siehe :ref:`Sub-region Bounding Box <dataset-and-request-parameters>`

Für die weiteren Parameter Datenformat und Komprimierung setzen Sie die Felder in der Eingabemaske bitte wie in der folgenden Abbildung gezeigt.

.. image:: /_static/04-kurs-1-cds-5.png
	:width: 600px
	:align: center
	:class: no-scaled-link
	:alt: Data and Download Fromat

Sobald Sie die Nutzungsbedingungen akzeptiert haben müssen Sie nur noch auf **Show API request code** klicken und der automatisch generierte API request code erscheint. Für unsere Testdaten sieht dieser wie folgt aus:

.. _dataset-and-request-parameters:

	.. code-block:: python

		# Datensatz und Anfrageparameter definieren
		dataset = "reanalysis-era5-land"
		request = {
				"variable": ["2m_temperature"],
				"year": "2024",
				"month": "10",
				"day": ["01"],
				"time": [
				"00:00", "01:00", "02:00",
				"03:00", "04:00", "05:00",
				"06:00", "07:00", "08:00",
				"09:00", "10:00", "11:00",
				"12:00", "13:00", "14:00",
				"15:00", "16:00", "17:00",
				"18:00", "19:00", "20:00",
				"21:00", "22:00", "23:00"
			],
			"data_format": "netcdf",
			"download_format": "zip",
			"area": [48.7, 7, 47.1, 11]
		}

	.. code-block:: python

		client = cdsapi.Client()

		# Dateiname definieren und herunterladen
		download_folder = os.path.join(os.getcwd(), "CDSdata")		
		os.makedirs(download_folder, exist_ok=True)  # Verzeichnis erstellen, falls nicht vorhanden

		# Download-Dateipfad definieren
		download_filepath = os.path.join(download_folder, f"{dataset}.zip")

		# Laden Sie den Datensatz herunter
		client.retrieve(dataset, request, download_filepath)


.. _api-jupyter:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2. Die API-Request im Jupyter Notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Öffnen Sie Ihr Jupyter lab über die Eingabeaufforderung (cmd)

	.. code-block::

		jupyter lab

Falls das Öffnen des **Jupyter Lab** nicht funktioniert gehen Sie am besten noch einmal die Anleitung durch, die wir :ref:`hier <software-knowledge>` für Sie vorbereitet haben.