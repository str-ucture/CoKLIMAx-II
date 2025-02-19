.. _kurs1-element2:

=========
Element 2
=========

-------------------
Learning Objectives
-------------------

* :ref:`Structure and Handling of a file in NetCDF Format <netcdf_how_to>`
	* :ref:`Unpacking the NetCDF Zip file <netcdf_unzip>`
	* :ref:`Investigate the NetCDF file <netcdf_investigate>`
* :ref:`Visualization of a Time Series and a Selected Region <netcdf_visualize>`

----

All the steps from this course is also available in a ready-to-use notebook for download from the following link:

.. raw:: html

   <div class="download-button">
       <a href="../_static/notebooks/element2_netcdf.ipynb" download>⇩ Element2: Notebook</a>
   </div>

Open the notebook in Jupyter Lab and follow the instructions. Alternatively, you can copy the Python code snippet into your Jupyter Notebook and execute the cell.

----

.. _netcdf_how_to:

---------------------
Handling NetCDF Files
---------------------

NetCDF (Network Common Data Form) is a data format specifically designed for scientific data. It was developed in the late 1980s by the Unidata program of the University Corporation for Atmospheric Research (UCAR). The goal was to provide a standardized format for storing and exchanging multidimensional data, particularly suited for applications in climate research, meteorology, and oceanography. Since then, NetCDF has become a key tool for working with spatial and temporal data.

For more information, visit the `UCAR website <https://docs.unidata.ucar.edu/netcdf-c/current/faq.html>`_.

To work with NetCDF files, first install the necessary Python libraries:

    .. code-block::

        pip install netCDF4 xarray numpy matplotlib

.. _netcdf_unzip:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Unpacking the NetCDF Zip file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open your Jupyter Lab via the command prompt (cmd):

	.. code-block::

		jupyter lab

Open a notebook in a folder of your choice. You can use the "CDSdata" folder from the first course module (:ref:`Element 1 <kurs1-element1>`), as it contains the data we will be working with.

The file you downloaded in the first course module (:ref:`Element 1 <kurs1-element1>`) is in NetCDF format but is still compressed in a ZIP file. Alternatively, you can download the dataset from Element 1 here and move it inside "CDSdata" folder inside the current working folder in Jupyter Lab:

.. raw:: html

   <div class="download-button">
       <a href="../_static/notebooks/CDSdata/reanalysis-era5-land.zip" download>⇩ ERA5-Land (Dataset)</a>
   </div>

First, extract the data by copying the following code block into your notebook and modifying the lines as needed:

    .. code-block:: python

        import zipfile
        import os

        # Path to the ZIP file (same directory or absolute path)
        zip_file = './CDSdata/reanalysis-era5-land.zip'

        # Target directory for extraction
        target_directory = 'Era5Data'
        os.makedirs(target_directory, exist_ok=True) # Create the directory if it doesn't exist

        # Open and extract the ZIP file
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(target_directory)
        print(f"ZIP file successfully extracted to '{target_directory}'.")

Now, let's take a closer look at the file.

.. _netcdf_investigate:

^^^^^^^^^^^^^^^^^^^^^^^^^^
2. Examining a NetCDF File
^^^^^^^^^^^^^^^^^^^^^^^^^^

NetCDF files are structured into dimensions, variables, and attributes. Dimensions serve as the axes along which the variables are arranged. These axes can represent, for example, geographic longitude and latitude or different altitude levels. Variables are the meteorological parameters contained in the file, such as temperature, air pressure, or wind speeds. Attributes of a NetCDF file are the metadata and include the units of the variables, descriptions, and the sources/authors of the data.

First, get an overview of the dataset.

    .. code-block:: python
        
        import netCDF4 as nc  
        
        # Open file
        dataset = nc.Dataset('ERA5Data/data_0.nc', 'r')
        
        # Display Metadata
        print(dataset)  

The ``print`` command provides the most important information about the given file in a readable text format. At a glance, you can see which variables are included, their formats, and how many time steps are available.

There are many other ways to quickly obtain more information about a NetCDF file. You can display the **keys**, meaning the short names of the variables, and thus apply the ``print`` command to an individual one. With the following code block, you can immediately check whether the ``2m temperature`` values of our test dataset appear valid.

    .. code-block:: python
        
        # List variables
        print(dataset.variables.keys())
        
        # Access a variable
        temperature = dataset.variables['t2m'][:]
        print(temperature)

Once you have tried out the various commands for a quick overview, you can proceed with different visualization options.

----

.. _netcdf_visualize:

---------------------------------------
Visualization and Selection of a Region
---------------------------------------

To have more options for visualization, you will need an additional dataset. We have already made this available for download. Just like in the previous section, it is a dataset from the ERA-5 reanalysis, containing monthly averages of the 2m temperature for a predefined region in southern Germany.

.. raw:: html
    
    <div class="download-button">
        <a href="../_static/notebooks/era5-land-monthly/download/reanalysis-era5-land-monthly-means_2m_temperature_1950_2024.nc" download>⇩ Dataset for Visualization</a>
    </div>

First, you should define the paths for your output. This step should be included at the beginning of every notebook to ensure that you can easily locate your generated data and plots. It also makes your code more flexible. By using aliases (e.g., "output_folder") for storage paths, you avoid the hassle of searching through your notebook if the paths change. You only need to update the paths in the first code block, and the rest will automatically adjust thanks to the aliases.

    .. code-block:: python
        
        import os
        
        # ---- Specify directories below ----
        download_folder = r"./era5-land-monthly/download"  # Folder for downloaded data
        output_folder = r"./era5-land-monthly/output"      # Folder for final outputs
        # ---- End of user inputs ----
        
        # Create directories if they do not exist
        os.makedirs(download_folder, exist_ok=True)
        os.makedirs(output_folder, exist_ok=True)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Reading and Exploring the Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the following steps, we will use some useful Python libraries, such as the data analysis library **pandas**. Further information on each library can be found online, as they are not included in the resources of **CoKLIMAx II**. The code blocks contain comments that document each step in text form.

In addition to defining storage paths, you should also specify the paths to the files you want to work with.

    .. code-block:: python

        # Specify the dataset filename and construct its full path
        filename = "reanalysis-era5-land-monthly-means_2m_temperature_1950_2024.nc"
        filepath = os.path.join(download_folder, filename)

        # Display the constructed file path for verification
        print(f"Dataset file path: {filepath}")

Now, get an overview of the file, including its spatial and temporal extent, as well as the available variables and time steps.

    .. code-block:: python

        import netCDF4 as nc

        # Open the NetCDF file in read mode
        dataset = nc.Dataset(filepath, mode='r')

        # List all variables in the dataset
        variables_list = dataset.variables.keys()
        print(f"Available variables: {list(variables_list)}")

        # Extract coordinate data and the primary variable's data
        lon_list = dataset['longitude'][:]  # Extract longitude
        lat_list = dataset['latitude'][:]  # Extract latitude

    .. code-block:: python

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

    .. code-block:: python

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
        dataset_summary = pd.DataFrame(list(ds_summary.items()), columns=['Description', 'Remarks'])

        # Display the summary DataFrame
        dataset_summary

In the generated summary, you can see that the file contains **898** valid time steps. Since the data represents monthly averages and the file starts with its first time step in January 1950, we now know that the last time step is in October 2024: **(2024 − 1950) × 12 + 10 = 898**.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2. Creating a Plot for August 1980
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the following code blocks, you can create a flexible plotting script that allows you to quickly switch between visualizations for different months.

To achieve this, define aliases for the year and month at the beginning, just as you did for the storage and file paths.

    .. code-block:: python

        # Define the target year and month for visualization
        selected_year = 1980
        selected_month = 8

        # Calculate the band index for the selected year and month
        # Index is determined by the position in the time dimension
        band_index = (selected_year - 1950) * 12 + (selected_month - 1)

        # Extract the data slice corresponding to the selected year and month
        # This gives the spatial data (latitude x longitude) for the specified time
        band_data = variable_data[band_index, :, :]

In the next block, you will set some visualization options before viewing the final result.

    .. code-block:: python

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
            f'{summary["Long Name"]} ({summary["Units"]}) - {selected_year}-{selected_month:02d}',
            fontsize=14,
        )
        ax.set_xlabel("Longitude", fontsize=12)
        ax.set_ylabel("Latitude", fontsize=12)

        # Display the plot
        plt.tight_layout()
        plt.show()

You can add more details to the plot, such as administrative boundaries or grid lines. To improve readability, you can also convert temperature values from Kelvin to Celsius or adjust the color scheme. We have prepared some options for you in the next code blocks.

The required shapefile for Konstanz can be downloaded here:

.. raw:: html

   <div class="download-button">
       <a href="../_static/zip/kn_boundary.zip" download>⇩ Shapefile of Konstanz</a>
   </div>

Download and extract the **kn_boundary.zip** file into your working folder. Remember to adjust the file path to the shapefile in the following code so that the script can access it.

    .. code-block:: python

        import numpy as np
        import math as ma
        import geopandas as gpd
        import matplotlib.pyplot as plt
        from matplotlib.ticker import FuncFormatter
        from mpl_toolkits.axes_grid1 import make_axes_locatable

        # Convert the temperature data from Kelvin to °C
        band_data_C = variable_data[band_index, :, :] - 273.15

        # Calculate minimum and maximum values within the band data
        vmin = np.nanmin(band_data_C)
        vmax = np.nanmax(band_data_C)

        vmin_floor = ma.floor(vmin * 10) / 10
        vmax_ceil = ma.ceil(vmax * 10) / 10

        # Compute interval for the color bar
        interval = 0.1
        bins = int((vmax_ceil - vmin_floor) / interval)

    .. code-block:: python

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

        pcm = ax.pcolormesh(
            lon_list,
            lat_list,
            band_data_C,
            cmap=cmap,
            vmin=vmin_floor,
            vmax=vmax_ceil
        )

        # Add administrative boundary of Konstanz (Shapefile)
        konstanz_shp = r"./shapefiles/kn_boundary.shp"
        konstanz_boundary = gpd.read_file(konstanz_shp)
        konstanz_boundary.boundary.plot(ax=ax, edgecolor='red')

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

With this plot, you can easily get an overview of the spatial characteristics and distribution of a parameter. Try out different configurations to determine which color scheme and scale work best for your purpose.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3. Creating a Plot for a Time Series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To analyze the trend of aggregated monthly temperature averages for August across all years in a specific region, a **line plot** is well suited. You can generate this using the following code block. This approach utilizes the DataFrame structure, a format that organizes variables into sorted groups (similar to a table with rows and columns). This structure is particularly useful when working with large datasets.

More information on the proper use of lists, arrays, and DataFrames in Python can be found online.

    .. code-block:: python

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

    .. code-block:: python

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

        # Define y-axis limits
        ax.set_ylim(15, 24)

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
        ax.legend(loc='upper left', fontsize=12, frameon=True, facecolor='#ffffff', edgecolor='#b0b0b0')

        # Display the plot
        plt.tight_layout()
        plt.show()