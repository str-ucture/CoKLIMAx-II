import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import plotly.graph_objects as go
import calendar

def compute_df_stats(variable_data):
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

    return df_statistics


def plot_linegraph(selected_month, df_statistics):
    # Filter the statistics DataFrame by the selected month
    df_statistics_filtered = df_statistics[df_statistics['Month'] == selected_month]
    
    # Initialize the plot
    fig, ax = plt.subplots(figsize=(14, 8), facecolor='#f1f1f1')

    # Titles and labels
    ax.set_title(
        f'Average 2 meter Temperature for August (°C)',
        fontsize=20,
        fontweight='bold',
        color='#333333',
        pad=20
    )
    ax.set_xlabel("Year", fontsize=16, color='#555555')
    ax.set_ylabel(f'2m Temperature (°C)', fontsize=16, color='#555555')

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
    ax.legend(loc='upper left', fontsize=12, frameon=True, facecolor='#ffffff', edgecolor='#b0b0b0')

    # Display the plot
    plt.tight_layout()
    plt.show()

def plot_linegraph_with_slider(df_statistics):
    # Set default month to August (8)
    default_month = 8

    # Create figure
    fig = go.Figure()

    for month in range(1, 13):
        df_filtered = df_statistics[df_statistics['Month'] == month]
        
        # Actual data trace
        fig.add_trace(go.Scatter(
            x=df_filtered['Year'],
            y=df_filtered['Mean'],
            mode='lines+markers',
            name=f"{calendar.month_abbr[month]} Data",
            visible=(month == default_month)
        ))
        
        # Best fit curve (Quadratic Polynomial)
        if len(df_filtered) >= 3:
            coeffs = np.polyfit(df_filtered['Year'], df_filtered['Mean'], 2)
            poly_func = np.poly1d(coeffs)
            year_range = np.linspace(df_filtered['Year'].min(), df_filtered['Year'].max(), 100)
            best_fit_values = poly_func(year_range)
            
            fig.add_trace(go.Scatter(
                x=year_range,
                y=best_fit_values,
                mode='lines',
                name=f"{calendar.month_abbr[month]} Best Fit",
                visible=(month == default_month),
                line=dict(dash='dot', width=2)
            ))
        else:
            fig.add_trace(go.Scatter(
                x=[], y=[],
                mode='lines',
                name=f"{calendar.month_abbr[month]} Best Fit",
                visible=(month == default_month)
            ))

    # Create slider steps
    steps = []
    num_months = 12
    for i in range(num_months):
        # Initialize all traces as not visible
        visibility = [False] * (num_months * 2)
        
        # Set the two traces corresponding to the current month to visible
        visibility[2 * i] = True
        visibility[2 * i + 1] = True
        steps.append(dict(
            method="update",
            args=[{"visible": visibility}],
            label=calendar.month_abbr[i + 1]
        ))

    # Update layout with slider, setting active index to default_month - 1 (August)
    fig.update_layout(
        sliders=[dict(active=default_month - 1, pad={"t": 50}, steps=steps)],
        title="Average 2 Meter Temperature (°C)",
        xaxis_title="Year",
        yaxis_title="Mean Temperature (°C)",
        height=600
    )

    fig.show()