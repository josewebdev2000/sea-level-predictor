import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = sea_df["Year"]
    y = sea_df["CSIRO Adjusted Sea Level"]

    plt.figure(figsize=(15,10))
    plt.scatter(x, y)
    plt.xlabel("Year")
    plt.ylabel("Sea Level")
    plt.title("Yearly Measures of Sea Level")
    plt.savefig("yearly-sea-levels.png")

    # Create first line of best fit
    # Make a first line of best fit of linear regression for 2050
    slope, intercept, r_value, p_value, std_err = linregress(sea_df['Year'], sea_df['CSIRO Adjusted Sea Level'])

    # Plot the line of best fit
    years_for_prediction = range(1880, 2051)  # Assuming you want to predict until 2050
    line_of_best_fit = [slope * year + intercept for year in years_for_prediction]
    plt.plot(years_for_prediction, line_of_best_fit, label=f'First Line of Best Fit (Slope={slope:.4f})')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Sea Level Rise and Linear Regression')
    plt.legend()
    plt.savefig("first-prediction.png")


    # Create second line of best fit
    # Make another prediction with just the data from 2000
    recent_sea_df = sea_df[sea_df['Year'] >= 2000]

    plt.scatter(sea_df['Year'], sea_df['CSIRO Adjusted Sea Level'], label='Data Points')

    # Linear regression for recent data
    slope_recent, intercept_recent, _, _, _ = linregress(recent_sea_df['Year'], recent_sea_df['CSIRO Adjusted Sea Level'])

    # Plot the line of best fit for recent data
    years_for_prediction = range(1880, 2051)  # Assuming you want to predict until 2050
    line_of_best_fit_recent = [slope_recent * year + intercept_recent for year in years_for_prediction]
    plt.plot(years_for_prediction, line_of_best_fit_recent, label=f'Second Line of Best Fit (Slope={slope_recent:.4f})', linestyle='--')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Rise in Sea Level')

    # Show the plot
    plt.legend()

    # Add labels and title
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()