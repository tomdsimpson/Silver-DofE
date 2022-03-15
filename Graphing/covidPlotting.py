# Thomas Simpson
# Applying plotting to a dataset
# 26/07/21

# Importing modules
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd

# Reading in data
file = open("CovidCaseChange.csv", "r")
data_frame = pd.read_csv(file)

# Setting index to data and changing data type
data_frame.set_index('date', inplace = True)
data_frame.index = pd.to_datetime(data_frame.index).date

# Plotting points
plt.plot(data_frame.index, data_frame["newCasesByPublishDateChange"])
plt.tick_params(labelrotation=90)
myPlot = plt.gca()

myPlot.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
myPlot.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.show()

