import requests, json
import pandas as pd
import os
from dotenv import load_dotenv
from pprint import pprint
import numpy as np
import statistics

api_key = os.getenv("API_KEY")
# print(api_key)

dataframe = pd.read_csv("data/equipment_anomaly_data.csv")



### Pull City Names from csv ### ---------------------------------------------------------------------------------------------
city_name_list = []
city_name_row_dump = dataframe['location'].tolist()
for x in city_name_row_dump:
    if x in city_name_list:
        pass
    else:
        city_name_list.append(x)
# print(city_name_list)


### 2025 monthly Temp averages list Fahrenheit ### ---------------------------------------------------------------------

atlanta_monthly_avg_2025_temp = [40.32, 52.29, 59.22, 67.42, 70.61, 78.3, 83.16, 76.58, 76.44, 65.12, 57.02, 48.6]
chicago_monthly_avg_2025_temp = [24.68, 29.01, 45.17, 51.96, 58.93, 75.19, 78.77, 74.94, 70.76, 59.22, 43.36, 28.81]
houston_monthly_avg_2025_temp = [51.14, 59.39, 68.45, 73.48, 78.39, 82.85, 84.36, 84.35, 81.85, 76.85, 68.44, 59.59]
newyork_monthly_avg_2025_temp = [32.48, 35.86, 45.82, 54.88, 64.36, 73.76, 82.71, 74.86, 71.94, 61.24, 49.57, 36.23]
sanfrancisco_monthly_avg_2025_temp = [52.29, 53.27, 53.54, 55.23, 57.82, 58.44, 60.65, 63.53, 65.6, 61.75, 57.21, 52.25]



### View sample of Data table ### ----------------------------------------------------------------------------------
# print(dataframe.head())
### Getting summary of the dataframe use df.info(). ### --------------------------------------------------------------
# print(dataframe.info())
### Checking for missing or null values to identify any data gaps. ### ------------------------------------------------
# print(dataframe.isnull().sum())

### MATH SECTION ### ---------------------------------------------------------------------------------------------
# Loop through all continuous data of city list temps for  Mean, Median, Mode, Variance, Standard Deviation
### Mean Loop ### ---------------------------------------------------------------------------------------------



atlanta_2025_temp_avg = np.round(np.mean(atlanta_monthly_avg_2025_temp), 2)
chicago_2025_temp_avg = np.round(np.mean(chicago_monthly_avg_2025_temp), 2)
houston_2025_temp_avg = np.round(np.mean(houston_monthly_avg_2025_temp), 2)
newyork_2025_temp_avg = np.round(np.mean(newyork_monthly_avg_2025_temp), 2)
sanfrancisco_2025_temp_avg = np.round(np.mean(sanfrancisco_monthly_avg_2025_temp), 2)
# print(atlanta_2025_temp_avg)
# print(chicago_2025_temp_avg)
# print(houston_2025_temp_avg)
# print(newyork_2025_temp_avg)
# print(sanfrancisco_2025_temp_avg)

### Weighted Mean Loop ### ---------------------------------------------------------------------------------------------


### Median Loop ### ---------------------------------------------------------------------------------------------
atlanta_2025_temp_median = np.round(np.median(atlanta_monthly_avg_2025_temp), 2)
chicago_2025_temp_median = np.round(np.median(chicago_monthly_avg_2025_temp), 2)
houston_2025_temp_median = np.round(np.median(houston_monthly_avg_2025_temp), 2)
newyork_2025_temp_median = np.round(np.median(newyork_monthly_avg_2025_temp), 2)
sanfrancisco_2025_temp_median = np.round(np.median(sanfrancisco_monthly_avg_2025_temp), 2)
# print(atlanta_2025_temp_median)
# print(chicago_2025_temp_median)
# print(houston_2025_temp_median)
# print(newyork_2025_temp_median)
# print(sanfrancisco_2025_temp_median)

### Mode Loop ### ---------------------------------------------------------------------------------------------
atlanta_2025_temp_mode = statistics.mode(atlanta_monthly_avg_2025_temp)
chicago_2025_temp_mode = statistics.mode(chicago_monthly_avg_2025_temp)
houston_2025_temp_mode = statistics.mode(houston_monthly_avg_2025_temp)
newyork_2025_temp_mode = statistics.mode(newyork_monthly_avg_2025_temp)
sanfrancisco_2025_temp_mode = statistics.mode(sanfrancisco_monthly_avg_2025_temp)
print(atlanta_2025_temp_mode)
print(chicago_2025_temp_mode)
print(houston_2025_temp_mode)
print(newyork_2025_temp_mode)
print(sanfrancisco_2025_temp_mode)

### Variance ### ---------------------------------------------------------------------------------------------


### BLANK ### ---------------------------------------------------------------------------------------------






