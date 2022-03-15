# Thomas Simpson
# Plotting temperature trend against emissions
# 07/08/21



# Importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Plotting emissions

markers = np.array(["bo", "ro"])

for counter in range(2):

    # Reading in emission data csv
    file = open("co2_emissions.csv")
    df = pd.read_csv(file)

    # Extracting Specific country data
    country_name = input("Please enter a country name:   ")
    country_df = (df[df["Entity"] == country_name])  # Important

    # Creating numpy arrays
    years = np.array([])
    emissions = np.array([])

    # Plotting
    years = np.append(years, country_df["Year"])
    emissions = np.append(emissions, country_df["Annual CO2 emissions"])
    plt.plot(years, emissions, markers[counter], markersize=4, ls = "-")



# Plotting points
plt.show()

