.. _kurs1-netcdf-introduction:

=================
NetCDF Einführung
=================

---------
Lernziele
---------

* :ref:`Aufbau und Umgang mit einer Datei im NetCDF-Format <netcdf-how-to>`
	* :ref:`Entpacken der NetCDF zip-Datei <netcdf-unzip>`
  	* :ref:`Untersuchen der NetCDF-Datei <netcdf-investigate>`
* :ref:`Visualisierung mit einer gewählten Region und einer Zeitreihe <netcdf-visualize>`
	* :ref:`Daten lesen und untersuchen <read-and-explore-data>`
	* :ref:`Diagramm erstellen (ausgewählter Monat) <create-a-plot-of-a-month>`
	* :ref:`Diagramm erstellen (Zeitreihe) <create-a-plot-time-series>`

----

Alle Schritte aus diesem Kurs sind auch in einem gebrauchsfertigen Notizbuch verfügbar, das Sie unter den folgenden Links herunterladen können:

.. raw:: html

   <div class="download-button">
       <a href="../_static/notebooks/netcdf-introduction-part1.ipynb" download>⇩ NetCDF Einführung: Teil 1</a>
   </div>

.. raw:: html

   <div class="download-button">
       <a href="../_static/notebooks/netcdf-introduction-part2.ipynb" download>⇩ NetCDF Introduction: Teil 2</a>
   </div>

Öffnen Sie das Notizbuch in Jupyter Lab und folgen Sie den Anweisungen. Alternativ können Sie den Python-Code-Schnipsel in Ihr Jupyter Notebook kopieren und die Zelle ausführen.

----

.. _netcdf-how-to:

-------------------------
Umgang mit NetCDF-Dateien
-------------------------

NetCDF (Network Common Data Form) ist ein Datenformat, das speziell für wissenschaftliche Daten entwickelt wurde. Es wurde in den späten 1980er-Jahren vom Unidata-Programm des University Corporation for Atmospheric Research (UCAR) entwickelt. Ziel war es, ein standardisiertes Format für die Speicherung und den Austausch von multidimensionalen Daten bereitzustellen, das besonders für Anwendungen in der Klimaforschung, Meteorologie und Ozeanographie geeignet ist. NetCDF hat sich seitdem zu einem zentralen Werkzeug für die Arbeit mit raum- und zeitbezogenen Daten entwickelt.

Für weitere Informationen besuchen Sie die `UCAR-Websites <https://docs.unidata.ucar.edu/netcdf-c/current/faq.html>`_.

Um mit den NetCDF Dateien arbeiten zu können installieren Sie zunächst die notwendigen Python Bibliotheken

	.. code-block:: shell

		pip install netCDF4 xarray numpy matplotlib

.. _netcdf-unzip:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. NetCDF-Zip-Datei entpacken
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Öffnen Sie Ihr Jupyter lab über die Eingabeaufforderung (cmd):

	.. code-block:: shell

		jupyter lab

Öffnen Sie ein Notebook in einem Ordner Ihrer Wahl. Sie können den „CDSdata“ Ordner aus dem ersten Kursmodul (:ref:`CDS API Installation und Download <kurs1-cds-api-installation-and-download>`) nehmen, in diesem befinden sich die Daten, mit denen wir arbeiten wollen.

Die Datei die Sie im ersten Kursmodul (:ref:`CDS API Installation und Download <kurs1-cds-api-installation-and-download>`) heruntergeladen haben ist im NetCDF-Format, jedoch noch in einer Zip Datei komprimiert. Alternativ können Sie den Datensatz von **CDS API Installation und Download** hier herunterladen und in den Ordner „CDSdata“ innerhalb des aktuellen Arbeitsordners in Jupyter Lab verschieben:

.. raw:: html

   <div class="download-button">
       <a href="../_static/notebooks/CDSdata/reanalysis-era5-land.zip" download>⇩ ERA5-Land (Datensatz)</a>
   </div>

Zunächst entpacken Sie die Daten, kopieren Sie sich folgenden Block in Ihr Notebook und modifizieren Sie die Zeilen wie benötigt.

	..  code-block:: python

		import zipfile
		import os

		# Pfad zur ZIP-Datei (im selben Verzeichnis oder absoluter Pfad)
		zip_datei = './CDSdata/reanalysis-era5-land.zip'  # Passen Sie den Pfad bei Bedarf an

		# Zielverzeichnis zum Entpacken
		zielverzeichnis = 'Era5Data'
		os.makedirs(zielverzeichnis, exist_ok=True)  # Verzeichnis erstellen, falls nicht vorhanden
		
		# ZIP-Datei öffnen und extrahieren
			with zipfile.ZipFile(zip_datei, 'r') as zip_ref:
				zip_ref.extractall(zielverzeichnis)
			print(f"ZIP-Datei erfolgreich in '{zielverzeichnis}' entpackt.")

Nun schauen Sie sich die Datei genauer an. 

.. _netcdf-investigate:

^^^^^^^^^^^^^^^^^^^^^^^^^^^
2. NetCDF-Datei untersuchen
^^^^^^^^^^^^^^^^^^^^^^^^^^^

NetCDF Dateien sind in Dimensionen, Variablen und Attributen aufgebaut. Dabei sind Dimensionen die Achsen, an denen sich die Variablen bewegen. Achsen können beispielsweise geographische Länge und Breite sein, oder verschiedene Höhenlevel. Variablen sind die meteorologischen Parameter, die in der Datei beinhaltet sind. Beispielsweise Temperatur, Luftdruck oder Windgeschwindigkeiten. Attribute einer NetCDF-Datei sind die Metadaten und beinhalten Einheiten der Variablen, Beschreibungen und die Quellen/Autoren der Daten.

Zunächst verschaffen Sie sich einen Überblick über den Datensatz.

	.. code-block:: python
		
		import netCDF4 as nc

		# Datei öffnen
		dataset = nc.Dataset('./ERA5Data/data_0.nc', 'r')

		# Metadaten anzeigen
		print(dataset)

Der ``print``-Command gibt Ihnen die wichtigsten Informationen über die vorliegende Datei als lesbaren Text wieder. Sie können auf einen Blick sehen, welche Variablen enthalten sind, welche Formate diese Variablen haben oder auch wie viele Zeitschritte verfügbar sind.

Es gibt viele weitere Möglichkeiten schnell mehr Informationen über eine NetCDF-Datei zu erhalten. Sie können sich die **keys**, also die Kurznamen der Variablen anzeigen lassen und dadurch den ``print``-Command auf eine einzelne anwenden. Mit dem nächsten Code-Block können Sie auf einen Bloick sehen, ob die ``2m-Temperatur``-Werte unseres Test-Datensatzes valide erscheinen.

	.. code-block:: python

		# Variablen auflisten
		print(dataset.variables.keys())

		# Zugriff auf eine Variable
		temperatur = dataset.variables['t2m'][:]
		print(temperatur)

Wenn Sie die verschiedenen Commands für den schnellen Überblick ausprobiert haben, können Sie mit den verschiedenen Visualisierungsmöglichkeiten weiter machen.

----

.. _netcdf-visualize:

-------------------------------------------------------------
Visualisierung mit einer gewählten Region und einer Zeitreihe -------------------------------------------------------------

Um für die Visualisierung mehr Möglichkeiten zu haben benötigen Sie einen weiteren Datensatz. Diesen haben wir Ihnen bereits zum Download zur Verfügung gestellt. Es handelt sich genau wie im vorangegangenen Abschnitt um einen Datensatz aus der ERA-5 Reanalyse, die Monatsmittel der 2m-Temperatur für eine vordefinierte Region in Süddeutschland.

.. raw:: html
    
    <div class="download-button">
        <a href="../_static/notebooks/era5-land-monthly/download/reanalysis-era5-land-monthly-means_2m_temperature_1950_2024.nc" download>⇩ Datensatz zur Visualisierung</a>
    </div>

Zunächst sollten Sie die Pfade für Ihren Output definieren. Damit sollen Sie jedes Notebook beginnen, um sicherzugehen, dass Sie Ihre erzeugten Daten und Plots wiederfinden. Es sorgt auch dafür, dass Ihr Code flexibler wird. Durch die Aliase (Bsp. "output_folder") für die Speicherpfade ersparen Sie sich mühsames durchsuchen Ihres Notebooks, falls sich diese einmal ändern sollten. Sie müssen nur die Pfade im ersten Codeblock anpassen, der Rest erledigt sich durch die Aliase von alleine.

	.. code-block:: python

		import os

		# ---- Verzeichnisse unten angeben ----
		download_folder = r"./era5-land-monthly/download"  # Ordner für heruntergeladene Daten
		output_folder = r"./era5-land-monthly/output"  # Ordner für die endgültigen Ausgaben
		# ---- Ende der Benutzereingaben ----

		# Verzeichnis erstellen, falls nicht vorhanden
		os.makedirs(download_folder, exist_ok=True)
		os.makedirs(output_folder, exist_ok=True)

.. _read-and-explore-data:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Einlesen und Kennenlernen der Daten
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Im Folgenden nutzen wir einige nützliche Python Bibliotheken, wie zum Beispiel die Datenanalyse-Bibliothek **pandas**. Weiterführende Informationen zu den einzelnen Bibliotheken finden Sie online, diese sind nicht in den Ressourcen von **CoKLIMAx II** inkludiert. Die Code-Böcke enthalten Kommentare, die die einzelnen Arbeitschritte in Textform dokumentieren.

Definieren Sie zusätzlich zu den Speicherpfaden auch die Pfade zu den Dateien, mit denen Sie arbeiten möchten.

	.. code-block:: python

		# Geben Sie den Dateinamen des Datensatzes an und erstellen Sie seinen vollständigen Pfad.
		filename = "reanalysis-era5-land-monthly-means_2m_temperature_1950_2024.nc"
		filepath = os.path.join(download_folder, filename)

		# Anzeige des konstruierten Dateipfads zur Überprüfung
		print(f"Dataset file path: {filepath}")

Nun verschaffen Sie sich einen Überblick über die Datei, die räumliche und zeitliche Ausdehnung, sowie die verfügbaren Variablen und Zeitschritte.

    .. code-block:: python

        import netCDF4 as nc

        # Öffne die NetCDF-Datei im Lesemodus
        dataset = nc.Dataset(filepath, mode='r')

        # Liste alle Variablen im Datensatz auf
        variables_list = dataset.variables.keys()
        print(f"Verfügbare Variablen: {list(variables_list)}")

        # Extrahiere Koordinatendaten und die Daten der Hauptvariablen
        lon_list = dataset['longitude'][:]  # Längengrad extrahieren
        lat_list = dataset['latitude'][:]  # Breitengrad extrahieren

    .. code-block:: python

        import pandas as pd

        test_variable = 't2m'
        variable_data = dataset[test_variable]

        # Erstelle eine Zusammenfassung der Hauptvariablen
        summary = {
            "Variablenname": test_variable,
            "Datentyp": variable_data.dtype,
            "Form": variable_data.shape,
            "Variableninfo": f"{test_variable}({', '.join(variable_data.dimensions)})",
            "Einheiten": getattr(variable_data, "units", "N/A"),
            "Long Name": getattr(variable_data, "long_name", "N/A"),
        }

        # Zeige die Datensatz-Zusammenfassung als DataFrame für bessere Visualisierung
        nc_summary = pd.DataFrame(list(summary.items()), columns=['Beschreibung', 'Bemerkungen'])

        # Zeige das Zusammenfassungs-DataFrame an
        nc_summary

    .. code-block:: python

        import numpy as np
        import pandas as pd

        # Konfiguriere die Anzeigeeinstellungen von pandas für bessere Lesbarkeit
        pd.set_option('display.max_colwidth', None)

        # Erstelle eine Zusammenfassung des Datensatzes
        ds_summary = {
            "Institution": dataset.institution if hasattr(dataset, 'institution') else "N/A",
            "Dimensionen": list(dataset.dimensions.keys()),
            "Variablen": list(dataset.variables.keys()),
            "Variablen-Dimensionen": [
                np.shape(dataset[variable]) for variable in dataset.variables.keys()
            ],
        }

        # Konvertiere das Zusammenfassungs-Dictionary in ein DataFrame für bessere Visualisierung
        dataset_summary = pd.DataFrame(list(ds_summary.items()), columns=['Beschreibung', 'Bemerkungen'])

        # Zeige das Zusammenfassungs-DataFrame an
        dataset_summary


Im erstellten Summary sehen Sie, dass die Datei **898** valide Zeitschritte enthält. Da es sich um monatliche Mittelwerte handelt un die Datei im Januar 1950 ihren ersten Zeitschritt hat, wissen wir nun, dass im Oktober 2024 der letzte Zeitschritt ist: **(2024 - 1950) x 12 + 10 = 898**.

.. _create-a-plot-of-a-month:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2. Erstellen eines Plots für August 1980
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mit dem folgenden Code-Blöcken können Sie sich ein flexibles Plotskript erstellen, mit dem Sie ind er Lage sind, schnell zwischen Visualisierungen verschiedener Monate zu switchen.

Um dies zu erreichen definieren Sie Aliase für Jahr und Monat direkt zu Beginn, genau wie für die Speicherpfade und Dateipfade.

	.. code-block:: python

		# Definieren Sie das Zieljahr und den Zielmonat für die Visualisierung
		selected_year = 1980
		selected_month = 8

		# Berechnen Sie den Bandindex für das ausgewählte Jahr und den ausgewählten Monat
		# Der Index wird durch die Position in der Zeitdimension bestimmt
		band_index = (selected_year - 1950) * 12 + (selected_month - 1)

		# Extrahieren Sie den Datenausschnitt, der dem ausgewählten Jahr und Monat entspricht
		# Dies ergibt die räumlichen Daten (Breitengrad x Längengrad) für die angegebene Zeit
		band_data = variable_data[band_index,:,:]

Im folgenden Block legen Sie noch einige Visualisierungsoptionen fest, bevor Sie sich das Ergebnis anschauen können.

    .. code-block:: python

        import matplotlib.pyplot as plt

        # Daten mit matplotlib darstellen
        fig, ax = plt.subplots(figsize=(8, 8))

        # Vordefinierte Farbkarte laden
        cmap = plt.get_cmap("turbo")

        # Pseudofarbdiagramm für die Daten erstellen
        pcm = ax.pcolormesh(
            lon_list,
            lat_list,
            band_data,
            cmap=cmap,
            shading="auto",
        )

        # Farbbalken mit Einheiten hinzufügen
        cbar = plt.colorbar(pcm, ax=ax, label=f'{summary["Long Name"]} ({summary["Einheiten"]})')

        # Diagrammtitel und Beschriftungen festlegen
        ax.set_title(
            f'{summary["Long Name"]} ({summary["Einheiten"]}) - {selected_year}-{selected_month:02d}',
            fontsize=14,
        )
        ax.set_ylabel('Breitengrad', fontsize=12)
        ax.set_xlabel('Längengrad', fontsize=12)

        # Diagramm anzeigen
        plt.tight_layout()
        plt.show()

Sie können dem Plot weitere Informationen hinzufügen, wie zum Beispiel administrative Grenzen oder Gitterlinien. Zur besseren Lesbarkeit können Sie die Temperaturewerte von °Kelvin zu °Celsius konvertieren oder die Farbgebung anpassen. Einige Möglichkeiten haben wir Ihnen in den nächsten Code-Blöcken vorbereitet.

Das benötigte Shapefile von Konstanz können Sie sich hier herunterladen:

.. raw:: html

   <div class="download-button">
       <a href="../_static/zip/kn_boundary.zip" download>⇩ Shapefile von Konstanz</a>
   </div>

Laden Sie die Datei **kn_boundary.zip** herunter und entpacken Sie sie in Ihren Arbeitsordner. Denken Sie daran, im folgenden den Dateipfad zum Shapefile anzupassen, damit das Skript darauf zugreifen kann.

    .. code-block:: python

        import numpy as np
        import math as ma
        import geopandas as gpd
        import matplotlib.pyplot as plt
        from matplotlib.ticker import FuncFormatter
        from mpl_toolkits.axes_grid1 import make_axes_locatable

        # Temperaturdaten von Kelvin in °C umwandeln
        band_data_C = variable_data[band_index, :, :] - 273.15

        # Minimal- und Maximalwerte innerhalb der Banddaten berechnen
        vmin = np.nanmin(band_data_C)
        vmax = np.nanmax(band_data_C)

        vmin_floor = ma.floor(vmin * 10) / 10
        vmax_ceil = ma.ceil(vmax * 10) / 10

        # Intervall für die Farbleiste berechnen
        interval = 0.1
        bins = int((vmax_ceil - vmin_floor) / interval)

    .. code-block:: python

        # Funktion zum Formatieren von Breitengrad-Markierungen
        def format_latitude(x, pos):
            return f"{x:.2f}°N"

        # Funktion zum Formatieren von Längengrad-Markierungen
        def format_longitude(x, pos):
            return f"{x:.2f}°E"

        # Plotten mit matplotlib
        fig, ax = plt.subplots(figsize=(8, 8))

        # Vordefinierte Farbkarte mit 10 diskreten Farben laden
        cmap = plt.get_cmap('turbo', bins)

        pcm = ax.pcolormesh(
            lon_list,
            lat_list,
            band_data_C,
            cmap=cmap,
            vmin=vmin_floor,
            vmax=vmax_ceil
        )

        # Verwaltungsgrenze von Konstanz hinzufügen (Shapefile)
        konstanz_shp = r"./shapefiles/kn_boundary.shp"
        konstanz_boundary = gpd.read_file(konstanz_shp)
        konstanz_boundary.boundary.plot(ax=ax, edgecolor='red')

        # Farbbalken plotten
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=-0.95)
        plt.colorbar(pcm, cax=cax, label=f'{summary["Long Name"]} (°C)')

        # Gitternetzlinien hinzufügen
        ax.grid(visible=True, which='major', color='#f0f0f0', linestyle='--', alpha=0.5)

        # Benutzerdefinierte Tick-Formatierer für Breiten- und Längengrad festlegen
        ax.xaxis.set_major_formatter(FuncFormatter(format_longitude))
        ax.yaxis.set_major_formatter(FuncFormatter(format_latitude))

        ax.set_title(f'{summary["Long Name"]} (°C)')
        ax.set_ylabel('Breitengrad', fontsize=12)
        ax.set_xlabel('Längengrad', fontsize=12)

		# Diagramm anzeigen
        plt.show()

Mit dem Plot können Sie sich einfach einen Überblick über die räumliche Ausprägung und Verteilung eines Paramenters verschaffen. Probieren Sie verschiedene Konfigurationen aus um herauszufinden, welche Farbgebung und Skala für Ihren Zweck am besten funktioniert.

.. _create-a-plot-time-series:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3. Erstellen eines Plots für eine Zeitserie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um den Verlauf der aggregierten monatlichen Temperatur-Mittelwerte für August aller Jahre einer Region zu betrachten eignet sich ein **Linienplot**. Diesen erstellen Sie mit dem foilgenden Code-Block. Dabei arbeiten Sie mit der dataframe-Struktur, einem Format, das (ähnlich einer Tabelle mit Zeilen und Spalten) sortierte Variablengruppen erstellt, welche sehr nützlich im Umgang mit großen Datenpaketen sein können.

Mehr Informationen zum richtigen Einsatz von Listen, Arrays und Dataframes in Python finden Sie online.

	.. code-block:: python

		# Listen zum Speichern von Statistiken initialisieren
		mean_values_list = []
		median_values_list = []
		std_values_list = []

		# Gesamtanzahl der Zeitbänder berechnen
		total_bands = range(variable_data.shape[0])

		# Listen für Jahr und Monat basierend auf dem Zeitindex ableiten
		year_list = [(band_index // 12) + 1950 for band_index in total_bands]
		month_list = [(band_index % 12) + 1 for band_index in total_bands]

		# Über alle Bänder iterieren, um Statistiken zu berechnen
		for band_index in total_bands:
			# Kelvin in Celsius umrechnen
			band_data = variable_data[band_index, :, :] - 273.15

			# Statistiken berechnen und hinzufügen
			mean_values_list.append(np.nanmean(band_data))  # Mittelwert ohne NaNs
			median_values_list.append(np.ma.median(band_data))  # Median für maskierte Arrays
			std_values_list.append(np.nanstd(band_data))  # Standardabweichung ohne NaNs

		# Ein Dictionary zur Speicherung der Ergebnisse erstellen
		df_data = {
			'Jahr': year_list,
			'Monat': month_list,
			'Mittelwerd': mean_values_list,
			'Median': median_values_list,
			'Standardabweichung': std_values_list
		}

		# Dictionary in ein DataFrame umwandeln
		df_statistics = pd.DataFrame(df_data)

		# Die ersten Zeilen des DataFrames anzeigen
		df_statistics.head()

	.. code-block:: python

		import matplotlib.ticker as ticker

		# Das Statistik-DataFrame nach dem ausgewählten Monat (August) filtern
		selected_month = 8  # August
		df_statistics_filtered = df_statistics[df_statistics['Month'] == selected_month]

		# Diagramm initialisieren
		fig, ax = plt.subplots(figsize=(14, 8), facecolor='#f1f1f1')

		# Titel und Achsenbeschriftungen
		ax.set_title(
			f'Durchschnittliche  {summary["Long Name"]} für August (°C)',
			fontsize=20,
			fontweight='bold',
			color='#333333',
			pad=20
		)
		ax.set_xlabel("Jahr", fontsize=16, color='#555555')
		ax.set_ylabel(f'{summary["Long Name"]} (°C)', fontsize=16, color='#555555')

		# Diagrammparameter für Konsistenz aktualisieren
		params = {
			'axes.labelsize': 16,
			'axes.titlesize': 18,
			'xtick.labelsize': 12,
			'ytick.labelsize': 12,
		}
		plt.rcParams.update(params)

		# Raster und Tick-Formatierung hinzufügen
		ax.grid(visible=True, color='#b0b0b0', linestyle='--', linewidth=0.8, alpha=0.6)
		ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))
		ax.tick_params(axis='y', which='both', color='#b0b0b0')

		# Begrenzung der y-Achse definieren
		ax.set_ylim(15,24)

		# Durchschnittliche Temperatur-Trendlinie zeichnen
		line1, = ax.plot(
			df_statistics_filtered['Jahr'],
			df_statistics_filtered['Mittelwert'].astype(float),
			label='Durchschnittstemperatur',
			color='#ff6f61',
			linestyle='-.',
			marker='o',
			linewidth=2.5
		)

		# Quadratische Anpassung (Grad 2) für die Trendlinie berechnen
		degree = 2  # Quadratische Anpassung
		coefficients = np.polyfit( 
			df_statistics_filtered['Jahr'],
			df_statistics_filtered['Mittelwert'].astype(float),
			degree
		)
		curve_fit = np.poly1d(coefficients)

		# Angepasste Trendlinie zeichnen
		ax.plot(
			df_statistics_filtered['Jahr'],
			curve_fit(df_statistics_filtered['Jahr']),
			label=f'Kurvenanpassung (Grad {degree})',
			color='blue',
			linestyle='--',
			linewidth=1.5
		)

		# Legende hinzufügen
		ax.legend(loc='upper left', fontsize=12, frameon=True, facecolor='#ffffff', 	edgecolor='#b0b0b0')

		# Diagramm anzeigen
		plt.tight_layout()
		plt.show()
