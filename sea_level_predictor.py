import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.7, s=20)

    # Create first line of best fit
    res_all = lineregress(d['Year'], df['CSIRO Adjusted Sea Level'])
    #lineregress calculates the linear regress by square minimums and returns, amongst others,
    #the slope (res.slope) and the intercept point with y axis (res.intercept)
    x_all = pd.Series(range(df['Year'].min(), 2051))
    # a series of all years (thats why range) that starts in the minimum year which is 1880
    y_all = res_all.slope * x_all + res_all.intercept
    #literally the formula of a recta: y = m*x + n
    plt.plot(x_all, y_all, 'r', label='Fit: 1880-2050')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    #so it just contains data from 2000 onwards
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    #literally the formula of a recta: y = m*x + n
    plt.plot(x_recent, y_recent, 'green', label='Fit: 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()