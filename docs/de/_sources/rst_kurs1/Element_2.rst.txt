=========
Element 2
=========

.. _kurs1-element2:

---------
Lernziele
---------

 * :ref:`Aufbau und Umgang mit einer Datei im NetCDF-Format<netcdf_how_to>`
  * :ref:`Entpacken der NetCDF zip-Datei<netcdf_unzip>`
  * :ref:`Untersuchen der NetCDF-Datei<netcdf_investigate>`
 * :ref:`Visualisierung einer Zeitreihe und einer gewählten Region <netcdf_visualize>`

----

.. _netcdf_how_to:

-------------------------
Umgang mit NetCDF-Dateien
-------------------------

NetCDF (Network Common Data Form) ist ein Datenformat, das speziell für wissenschaftliche Daten entwickelt wurde. Es wurde in den späten 1980er-Jahren vom Unidata-Programm des University Corporation for Atmospheric Research (UCAR) entwickelt. Ziel war es, ein standardisiertes Format für die Speicherung und den Austausch von multidimensionalen Daten bereitzustellen, das besonders für Anwendungen in der Klimaforschung, Meteorologie und Ozeanographie geeignet ist. NetCDF hat sich seitdem zu einem zentralen Werkzeug für die Arbeit mit raum- und zeitbezogenen Daten entwickelt.

Für weitere Informationen besuchen Sie die `UCAR-Websites <https://docs.unidata.ucar.edu/netcdf-c/current/faq.html>`_.

Um mit den NetCDF Dateien arbeiten zu können installieren Sie zunächst die notwendigen Python Bibliotheken

	.. code-block::

		pip install netCDF4 xarray numpy matplotlib

.. _netcdf_unzip:

^^^^^^^^^^^^^^^^^^^^^^^^^
1. NetCDF-Datei entpacken
^^^^^^^^^^^^^^^^^^^^^^^^^

Öffnen Sie Ihr Jupyter lab über die Eingabeaufforderung (cmd):

	.. code-block::

		jupyter lab

Öffnen Sie ein Notebook in einem Ordner Ihrer Wahl. Sie können den "CDSdata" Ordner aus dem 1. Kurselement nehmen, in diesem befinden sich die Daten, mit denen wir arbeiten wollen.

Die Datei die Sie im 1. Kurselement heruntergeladen haben ist im NetCDF Format, jedoch noch in einer Zip Datei komprimiert.Zunächst entpacken Sie die Daten, kopieren Sie sich folgenden Block in Ihr Notebook und modifizieren Sie die Zeilen wie benötigt:

	..  code-block::

		import zipfile
		import os

		# Pfad zur ZIP-Datei (im selben Verzeichnis oder absoluter Pfad)
		zip_datei = 'beispiel.zip'

		# Zielverzeichnis zum Entpacken
		zielverzeichnis = 'Era5Data'
		os.makedirs(zielverzeichnis, exist_ok=True)  # Verzeichnis erstellen, falls nicht vorhanden
		
		# ZIP-Datei öffnen und extrahieren
			with zipfile.ZipFile(zip_datei, 'r') as zip_ref:
				zip_ref.extractall(zielverzeichnis)
			print(f"ZIP-Datei erfolgreich in '{zielverzeichnis}' entpackt.")

Nun schauen Sie sich die Datei genauer an. 

.. _netcdf_investigate:

^^^^^^^^^^^^^^^^^^^^^^^^^^^
2. NetCDF-Datei untersuchen
^^^^^^^^^^^^^^^^^^^^^^^^^^^

NetCDF Dateien sind in Dimensionen, Variablen und Attributen aufgebaut. Dabei sind Dimensionen die Achsen, an denen sich die Variablen bewegen. Achsen können beispielsweise geographische Länge und Breite sein, oder verschiedene Höhenlevel. Variablen sind die meteorologischen Parameter, die in der Datei beinhaltet sind. Beispielsweise Temperatur, Luftdruck oder Windgeschwindigkeiten. Attribute einer NetCDF-Datei sind die Metadaten und beinhalten Einheiten der Variablen, Beschreibungen und die Quellen/Autoren der Daten.

Zunächst verschaffen Sie sich einen Überblick über den Datensatz.

.. code-block::
	
	import netCDF4 as nc

	# Datei öffnen
	dataset = nc.Dataset('ERA5Data/data_0.nc', 'r')

	# Metadaten anzeigen
	print(dataset)

Der ``print``-Command gibt Ihnen die wichtigsten Informationen über die vorliegende Datei als lesbaren Text wieder. Sie können auf einen Blick sehen, welche Variablen enthalten sind, welche Formate diese Variablen haben oder auch wie viele Zeitschritte verfügbar sind.

Es gibt viele weitere Möglichkeiten schnell mehr Informationen über eine NetCDF-Datei zu erhalten. Sie können sich die **keys**, also die Kurznamen der Variablen anzeigen lassen und dadurch den ``print``-Command auf eine einzelne anwenden. Mit dem nächsten Code-Block können Sie auf einen Bloick sehen, ob die ``2m-Temperatur``-Werte unseres Test-Datensatzes valide erscheinen.

	.. code-block::

		# Variablen auflisten
		print(dataset.variables.keys())

		# Zugriff auf eine Variable
		temperatur = dataset.variables['t2m'][:]
		print(temperatur)

Wenn Sie die verschiedenen Commands für den schnellen Überblick ausprobiert haben, können Sie mit den verschiedenen Visualisierungsmöglichkeiten weiter machen.

Alle zuvor ausgeführten Schritte finden Sie auch fertigen Notebook zum Download:

:download:`Element1_API_Test.ipynb </../_static/Element2_NetCDF.ipynb>`

.. _netcdf_visualize:

---------------------------------------
Visualisierung und Auswahl einer Region
---------------------------------------

Um für die Visualisierung mehr Möglichkeiten zu haben benötigen Sie einen weiteren Datensatz. Diesen haben wir Ihnen bereits zum Download zur Verfügung gestellt. Es handelt sich genau wie im vorangegangenen Abschnitt um einen Datensatz aus der ERA-5 Reanalyse, die Monatsmittel der 2m-Temperatur für eine vordefinierte Region in Süddeutschland.

:download:`Datensatz Visualisierung <.\data\era5-land-monthly\download\reanalysis-era5-land-monthly-means_2m_temperature_1950_2024.nc>`

Zunächst sollten Sie die Pfade für Ihren Output definieren. Damit sollen Sie jedes Notebook beginnen, um sicherzugehen, dass Sie Ihre erzeugten Daten und Plots wiederfinden. Es sorgt auch dafür, dass Ihr Code flexibler wird. Durch die Aliase (Bsp. "output_folder") für die Speicherpfade ersparen Sie sich mühsames durchsuchen Ihres Notebooks, falls sich diese einmal ändern sollten. Sie müssen nur die Pfade im ersten Codeblock anpassen, der Rest erledigt sich durch die Aliase von alleine.

	.. code-block::

		import os

		# ---- Specify directories below ----
		download_folder = r".\data\era5-land-monthly\download"  # Folder for downloaded data
		output_folder = r".\data\era5-land-monthly\output"      # Folder for final outputs
		# ---- End of user inputs ----

		# Create directories if they do not exist
		os.makedirs(download_folder, exist_ok=True)
		os.makedirs(output_folder, exist_ok=True)


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Einlesen und Kennenlernen der Daten
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Im Folgenden nutzen wir einige nützliche Python Bibliotheken, wie zum Beispiel die Datenanalyse-Bibliothek **pandas**. Weiterführende Informationen zu den einzelnen Bibliotheken finden Sie online, diese sind nicht in den Ressourcen von **CoKLIMAx II** inkludiert. Die Code-Böcke enthalten Kommentare, die die einzelnen Arbeitschritte in Textform dokumentieren.

Definieren Sie zusätzlich zu den Speicherpfaden auch die Pfade zu den Dateien, mit denen Sie arbeiten möchten.

	.. code-block::

		# Specify the dataset filename and construct its full path
		filename = "reanalysis-era5-land-monthly-means_2m_temperature_1950_2024.nc"
		filepath = os.path.join(download_folder, filename)

		# Display the constructed file path for verification
		print(f"Dataset file path: {filepath}")

Nun verschaffen Sie sich einen Überblick über die Datei, die räumliche und zeitliche Ausdehnung, sowie die verfügbaren Variablen und Zeitschritte.

	.. code-block::

		import netCDF4 as nc

		# Open the NetCDF file in read mode
		dataset = nc.Dataset(filepath, mode='r')

		# List all variables in the dataset
		variables_list = dataset.variables.keys()
		print(f"Available variables: {list(variables_list)}")

		# Extract coordinate data and the primary variable's data
		lon_list = dataset['longitude'][:]  # Extract longitude
		lat_list = dataset['latitude'][:]  # Extract latitude

	.. code-block::

			import pandas as pd

			test_variable = 't2m'
			variable_data = dataset[test_variable]

			# Generate summary of the primary variable
			summary = {
					"Variable Name": test_variable,
					"Data Type": variable_data.dtype,
					"Shape": variable_data.shape,
					"Variable Info": f"{test_variable}({', '.join(variable_data.dimensions)})",
					"Units": getattr(variable_data, "units", "N/A"),
					"Long Name": getattr(variable_data, "long_name", "N/A"),
			}
		
		# Display dataset summary as a DataFrame for better visualization
		nc_summary = pd.DataFrame(list(summary.items()), columns=['Description', 'Remarks'])

		# Display the summary DataFrame
		nc_summary

	.. code-block::

		import numpy as np
		import pandas as pd

		# Configure pandas display settings for better readability
		pd.set_option('display.max_colwidth', None)

		# Create a summary of the dataset
		ds_summary = {
			"Institution": dataset.institution if hasattr(dataset, 'institution') else "N/A",
			"Dimensions": list(dataset.dimensions.keys()),
			"Variables": list(dataset.variables.keys()),
			"Variable dimensions": [
				np.shape(dataset[variable]) for variable in dataset.variables.keys()
			],
		}

		# Convert the summary dictionary into a DataFrame for better visualization
		dataset_summary = pd.DataFrame(list(ds_summary.items()), columns=['Description', 	'Remarks'])

		# Display the summary DataFrame
		dataset_summary

Im erstellten Summary sehen Sie, dass die Datei 898 valide Zeitschritte enthält. Da es sich um monatliche Mittelwerte handelt un die Datei im Januar 1950 ihren ersten Zeitschritt hat, wissen wir nun, dass im Oktober 2024 der letzte Zeitschritt ist. (2024-1950)*12 + 10 = 898.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Erstellen eines Plots für August 1980
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mit dem folgenden Code-Blöcken können Sie sich ein flexibles Plotskript erstellen, mit dem Sie ind er Lage sind, schnell zwischen Visualisierungen verschiedener Monate zu switchen.

Um dies zu erreichen definieren Sie Aliase für Jahr und Monat direkt zu Beginn, genau wie für die Speicherpfade und Dateipfade.

	.. code-block::

		# Define the target year and month for visualization
		selected_year = 1980
		selected_month = 8

		# Calculate the band index for the selected year and month
		# Index is determined by the position in the time dimension
		band_index = (selected_year - 1950) * 12 + (selected_month - 1)

		# Extract the data slice corresponding to the selected year and month
		# This gives the spatial data (latitude x longitude) for the specified time
		band_data = variable_data[band_index,:,:]

Im folgenden Block legen Sie noch einige Visualisierungsoptionen fest, bevor Sie sich das Ergebnis anschauen können.

	.. code-block::

		import matplotlib.pyplot as plt

		# Plot the data using matplotlib
		fig, ax = plt.subplots(figsize=(8, 8))

		# Load predefined colormap
		cmap = plt.get_cmap("turbo")

		# Create a pseudo-color plot for the data
		pcm = ax.pcolormesh(
			lon_list,
			lat_list,
			band_data,
			cmap=cmap,
			shading="auto",
		)

		# Add colorbar with units
		cbar = plt.colorbar(pcm, ax=ax, label=f'{summary["Long Name"]} ({summary["Units"]})')

		# Set plot title and labels
		ax.set_title(
				f'{summary["Long Name"]} ({summary["Units"]}) - {selected_year}-		{selected_month:02d}',
			fontsize=14,
		)
		ax.set_xlabel("Longitude", fontsize=12)
		ax.set_ylabel("Latitude", fontsize=12)

		# Display the plot
		plt.tight_layout()
		plt.show()

Sie können dem Plot weitere Informationen hinzufügen, wie zum Beispiel administrative Grenzen oder Gitterlinien. Zur besseren Lesbarkeit können Sie die Temperaturewerte von °Kelvin zu °Celsius konvertieren oder die Farbgebung anpassen. Einige Möglichkeiten haben wir Ihnen in den nächsten Code-Blöcken vorbereitet.

Das benötigte Shapefile von Konstanz können Sie sich hier herunterladen:

:download:`Shapefile von Konstanz </../_static/kn_boundary.shp>`

Denken Sie daran, im folgenden den Dateipfad zum Shapefile anzupassen, damit das Skript darauf zugreifen kann.

	.. code-block::

		import numpy as np
		import math as ma
		import geopandas as gpd
		import matplotlib.pyplot as plt
		from matplotlib.ticker import FuncFormatter
		from mpl_toolkits.axes_grid1 import make_axes_locatable

		# Convert the temperature data from K to °C
		band_data_C = variable_data[band_index,:,:]-273.15

		# Calculate minimum and maxium value within the band data
		vmin = np.nanmin(band_data_C)
		vmax = np.nanmax(band_data_C)

		vmin_floor = ma.floor(vmin * 10) / 10
		vmax_ceil = ma.ceil(vmax * 10) / 10

		# Compute interval for color bar
		interval = 0.1
		bins = int((vmax_ceil - vmin_floor)/interval)

	.. code-block::

		# Function to format latitude tick labels
		def format_latitude(x, pos):
			return f"{x:.2f}°N"

		# Function to format longitude tick labels
		def format_longitude(x, pos):
			return f"{x:.2f}°E"

		# Plot using matplotlib
		fig, ax = plt.subplots(figsize=(8, 8))

		# Load predefined Colormap with 10 discrete colors
		cmap = plt.get_cmap('turbo', bins)

		pcm = ax.pcolormesh(lon_list, 
						lat_list,
						band_data_C,
						cmap=cmap,
						vmin=vmin_floor,
						vmax=vmax_ceil)

		# Add administrative boundary of Konstanz (Shapefile)
		germany_shp = r".\shapefiles\kn_boundary.shp"
		germany_boundary = gpd.read_file(germany_shp)
		germany_boundary.boundary.plot(ax=ax, edgecolor='red')

		# Plot color bar
		divider = make_axes_locatable(ax)
		cax = divider.append_axes("right", size="5%", pad=-0.95)
		plt.colorbar(pcm, cax=cax, label=f'{summary["Long Name"]} (°C)')

		# Add grid lines
		ax.grid(visible=True, which='major', color='#f0f0f0', linestyle='--', alpha=0.5)

		# Set custom tick formatters for latitude and longitude
		ax.xaxis.set_major_formatter(FuncFormatter(format_longitude))
		ax.yaxis.set_major_formatter(FuncFormatter(format_latitude))

		ax.set_title(f'{summary["Long Name"]} (°C)')
		ax.set_ylabel('Latitude', fontsize=12)
		ax.set_xlabel('Longitude', fontsize=12)

		plt.show()

Mit dem Plot können Sie sich einfach einen Überblick über die räumliche Ausprägung und Verteilung eines Paramenters verschaffen. Probieren Sie verschiedene Konfigurationen aus um herauszufinden, welche Farbgebung und Skala für Ihren Zweck am besten funktioniert.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Erstellen eines Plots für eine Zeitserie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um den Verlauf der aggregierten monatlichen Temperatur-Mittelwerte für August aller Jahre einer Region zu betrachten eignet sich ein **Linienplot**. Diesen erstellen Sie mit dem foilgenden Code-Block. Dabei arbeiten Sie mit der dataframe-Struktur, einem Format, das (ähnlich einer Tabelle mit Zeilen und Spalten) sortierte Variablengruppen erstellt, welche sehr nützlich im Umgang mit großen Datenpaketen sein können.

Mehr Informationen zum richtigen Einsatz von Listen, Arrays und Dataframes in Python finden Sie online.

	.. code-block::

		# Initialize lists to store statistics
		mean_values_list = []
		median_values_list = []
		std_values_list = []

		# Calculate the total number of time bands
		total_bands = range(variable_data.shape[0])

		# Derive year and month lists based on the time index
		year_list = [(band_index // 12) + 1950 for band_index in total_bands]
		month_list = [(band_index % 12) + 1 for band_index in total_bands]

		# Iterate over all bands to compute statistics
		for band_index in total_bands:
			# Convert Kelvin to Celsius
			band_data = variable_data[band_index, :, :] - 273.15

			# Compute and append statistics
			mean_values_list.append(np.nanmean(band_data))  # Mean excluding NaNs
			median_values_list.append(np.ma.median(band_data))  # Median for masked arrays
			std_values_list.append(np.nanstd(band_data))  # Standard deviation excluding NaNs

		# Create a dictionary to store results
		df_data = {
			'Year': year_list,
			'Month': month_list,
			'Mean': mean_values_list,
			'Median': median_values_list,
			"Std Dev": std_values_list
		}

		# Convert dictionary to DataFrame
		df_statistics = pd.DataFrame(df_data)

		# Display the first few rows of the DataFrame
		df_statistics.head()

	.. code-block::

		import matplotlib.ticker as ticker

		# Filter the statistics DataFrame by the selected month (August)
		selected_month = 8  # August
		df_statistics_filtered = df_statistics[df_statistics['Month'] == selected_month]

		# Initialize the plot
		fig, ax = plt.subplots(figsize=(14, 8), facecolor='#f1f1f1')

		# Titles and labels
		ax.set_title(
			f'Average {summary["Long Name"]} for August (°C)',
			fontsize=20,
			fontweight='bold',
			color='#333333',
			pad=20
		)
		ax.set_xlabel("Year", fontsize=16, color='#555555')
		ax.set_ylabel(f'{summary["Long Name"]} (°C)', fontsize=16, color='#555555')

		# Update plot parameters for consistency
		params = {
			'axes.labelsize': 16,
			'axes.titlesize': 18,
			'xtick.labelsize': 12,
			'ytick.labelsize': 12,
		}
		plt.rcParams.update(params)

		# Add grid and tick formatting
		ax.grid(visible=True, color='#b0b0b0', linestyle='--', linewidth=0.8, alpha=0.6)
		ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))
		ax.tick_params(axis='y', which='both', color='#b0b0b0')

		# Define yaxis limits
		ax.set_ylim(15,24)

		# Plot the mean temperature trend
		line1, = ax.plot(
			df_statistics_filtered['Year'],
			df_statistics_filtered['Mean'].astype(float),
			label='Mean Temperature',
			color='#ff6f61',
			linestyle='-.',
			marker='o',
			linewidth=2.5
		)

		# Fit a quadratic curve (degree 2) for the trend line
		degree = 2  # Quadratic fit
		coefficients = np.polyfit(
			df_statistics_filtered['Year'],
			df_statistics_filtered['Mean'].astype(float),
			degree
		)
		curve_fit = np.poly1d(coefficients)

		# Plot the curve fit trend line
		ax.plot(
			df_statistics_filtered['Year'],
			curve_fit(df_statistics_filtered['Year']),
			label=f'Curve Fit (Degree {degree})',
			color='blue',
			linestyle='--',
			linewidth=1.5
		)

		# Add legend
		ax.legend(loc='upper left', fontsize=12, frameon=True, facecolor='#ffffff', 	edgecolor='#b0b0b0')

		# Display the plot
		plt.tight_layout()
		plt.show()
