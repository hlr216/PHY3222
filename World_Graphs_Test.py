import seaborn
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# creating a data frame
df = pd.read_csv("World Energy Consumption.csv")

# refine data frame to only contain relevant columns
df0 = df[[ 'country',
           'year',
           'population',
           'gdp',
           'biofuel_consumption',
           'coal_consumption',
           'gas_consumption',
           'hydro_consumption',
           'nuclear_consumption',
           'oil_consumption',
           'solar_consumption',
           'wind_consumption',
           ]]

#define functions for each plot
def plot_country_fuel_distribution(country):
    pass


def plot_energy_ratio(df, country, year):
    """
    Plots the ratio of each fuel type used for a specific country and year as a pie chart.

    Parameters:
    df (DataFrame): DataFrame containing energy consumption data.
    country (str): The name of the country to filter.
    year (int): The year to filter.

    Returns:
    None
    """
    # Filter the DataFrame for the given country and year
    filtered_data = df[(df['country'] == country) & (df['year'] == year)]

    if filtered_data.empty:
        print(f"No data available for {country} in {year}.")
        return

    # Extract energy consumption columns
    energy_columns = [
        'biofuel_consumption',
        'coal_consumption',
        'gas_consumption',
        'hydro_consumption',
        'nuclear_consumption',
        'oil_consumption',
        'solar_consumption',
        'wind_consumption'
    ]

    # Get the values for the selected country and year
    energy_values = filtered_data[energy_columns].iloc[0]

    # Remove zero values for cleaner visualization
    energy_values = energy_values[energy_values > 0]

    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        energy_values,
        labels=energy_values.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.tab10.colors
    )

    # Add title and display the chart
    plt.title(f"Energy Consumption Ratio in {country} ({year})")


import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


def plot_multiple_pie_charts(df, countries, years):
    """
    Plots multiple pie charts showing the energy consumption ratio for specified countries and years,
    with consistent color coding and a legend as a key.

    Parameters:
    df (DataFrame): DataFrame containing energy consumption data.
    countries (list): List of countries to include in the charts.
    years (list): List of years to include in the charts.

    Returns:
    None
    """
    # Define energy columns
    energy_columns = [
        'biofuel_consumption',
        'coal_consumption',
        'gas_consumption',
        'hydro_consumption',
        'nuclear_consumption',
        'oil_consumption',
        'solar_consumption',
        'wind_consumption'
    ]

    # Define a consistent color map for energy sources
    color_map = {
        'biofuel_consumption': '#8dd3c7',
        'coal_consumption': '#ffffb3',
        'gas_consumption': '#bebada',
        'hydro_consumption': '#fb8072',
        'nuclear_consumption': '#80b1d3',
        'oil_consumption': '#fdb462',
        'solar_consumption': '#b3de69',
        'wind_consumption': '#fccde5'
    }

    # Create subplots
    fig, axes = plt.subplots(len(countries), len(years), figsize=(12, len(countries) * 4))
    fig.tight_layout(pad=5, rect=[0, 0, 0.85, 1])  # Adjust layout to fit legend

    # Loop through countries and years to create pie charts
    for i, country in enumerate(countries):
        for j, year in enumerate(years):
            # Filter the DataFrame for the current country and year
            filtered_data = df[(df['country'] == country) & (df['year'] == year)]

            ax = axes[i, j] if len(countries) > 1 else axes[j]  # Adjust indexing for 1D or 2D axes

            if filtered_data.empty:
                ax.axis('off')  # Hide axis if no data is available
                ax.text(0.5, 0.5, f"No data for {country} in {year}",
                        ha='center', va='center', fontsize=10, wrap=True)
                continue

            # Get energy consumption values
            energy_values = filtered_data[energy_columns].iloc[0]
            energy_values = energy_values[energy_values > 0]  # Remove zero values

            # Use the consistent color map for the pie chart
            colors = [color_map[col] for col in energy_values.index]

            # Create pie chart
            ax.pie(
                energy_values,
                labels=None,  # Remove labels to prevent clutter
                autopct='%1.1f%%',
                startangle=90,
                colors=colors
            )
            ax.set_title(f"{country} ({year})", fontsize=12)

    # Add a legend outside the plot
    handles = [plt.Line2D([0], [0], color=color_map[col], marker='o', linestyle='', markersize=10)
               for col in energy_columns]
    labels = [col.replace('_consumption', '').capitalize() for col in energy_columns]
    fig.legend(handles, labels, loc='center right', title="Energy Sources", fontsize=10, title_fontsize=12)

    # Set global title and show the plot
    fig.suptitle("Energy Consumption Ratios by Country and Year", fontsize=16)


#testing
#print( df0.loc[(df0['country'] == 'Brazil') & (df0['year'] == 2018)])

#main code
#plot_energy_ratio(df0, "Brazil", 1988)
#plot_energy_ratio(df0, "Brazil", 2018)
# List of countries and years to include
countries = ['Germany', 'Brazil', 'Nigeria']
years = [1988, 2018]

# Call the function
#plot_multiple_pie_charts(df0, countries, years)

#plt.show()
#countries_list = df0["country"].unique()
#print("len countries_list: ", len(countries_list))
#print(countries_list)

# Get unique countries
unique_countries = df0['country'].unique()

# Order countries by GDP (ascending or descending as needed)
# First group by country and calculate the mean GDP for each country
# Calculate the mean GDP for each country and sort
gdp_ordered_countries = df0.groupby('country')['gdp'].mean().sort_values(ascending=False)

# Print countries with their mean GDP
for country, gdp in gdp_ordered_countries.items():
    print(f"{country}: {gdp:.2f}")


