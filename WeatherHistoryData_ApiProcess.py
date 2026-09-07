import requests, json
import pandas as pd
import os
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from pprint import pprint

import openmeteo_requests

openmeteo = openmeteo_requests.Client()

load_dotenv()
api_key = os.getenv("API_KEY")
# print(api_key)
base_url = "https://api.open-meteo.com/v1/forecast"

lat = 0
long = 0
start_day = "2025-01-01"
end_day = "2025-12-31"


atlanta_params = {
	"latitude": 33.748997,
	"longitude": -84.387985,
    "start_date": start_day,
    "end_date": end_day,
    "daily": ["temperature_2m_max", "temperature_2m_min"]

}

chicago_params = {
	"latitude": 41.878113,
	"longitude": -87.629799,
    "start_date": start_day,
    "end_date": end_day,
    "daily": ["temperature_2m_max", "temperature_2m_min"]

}
sanfrancisco_params = {
	"latitude": 37.774929,
	"longitude": -122.419418,
    "start_date": start_day,
    "end_date": end_day,
    "daily": ["temperature_2m_max", "temperature_2m_min"]

}
newyork_params = {
	"latitude": 40.712776,
	"longitude": -74.005974,
    "start_date": start_day,
    "end_date": end_day,
    "daily": ["temperature_2m_max", "temperature_2m_min"]

}
houston_params = {
	"latitude": 29.749907,
	"longitude": -95.358421,
    "start_date": start_day,
    "end_date": end_day,
    "daily": ["temperature_2m_max", "temperature_2m_min"]

}




dataframe = pd.read_csv("data/equipment_anomaly_data.csv")
city_name_row_dump = dataframe['location'].tolist()
### LATLONG  ### ---------------------------------------------------------------------------------------------


atlanta_latlong = [
    {
        "lat": 33.748997,
        "long": -84.387985,
    }
]
chicago_latlong = [
    {
        "lat": 41.878113,
        "long": -87.629799,
    }
]
sanfrancisco_latlong = [
    {
        "lat": 37.774929,
        "long": -122.419418,
    }
]
newyork_latlong = [
    {
        "lat": 40.712776,
        "long": -74.005974,
    }
]
houston_latlong = [
    {
        "lat": 29.749907,
        "long": -95.358421,
    }
]


### Full URLs ### --------------------------------------------------------------------------------------------------------
atlanta_full_url = 'https://api.open-meteo.com/v1/forecastlat=33.748997&lon=-84.387985&appid=4d4abe6f83b083056d523437bf77c146'
chicago_full_url = 'https://api.open-meteo.com/v1/forecastlat=41.878113&lon=-87.629799&appid=4d4abe6f83b083056d523437bf77c146'
houston_full_url = 'https://api.open-meteo.com/v1/forecastlat=29.749907&lon=-95.358421&appid=4d4abe6f83b083056d523437bf77c146'
newyork_full_url = 'https://api.open-meteo.com/v1/forecastlat=40.712776&lon=-74.005974&appid=4d4abe6f83b083056d523437bf77c146'
sanfrancisco_full_url = 'https://api.open-meteo.com/v1/forecastlat=37.774929&lon=-122.419418&appid=4d4abe6f83b083056d523437bf77c146'


### Pull City Names from csv ### ---------------------------------------------------------------------------------------------
city_name_list = []
for x in city_name_row_dump:
    # city_name_list.append(x)
    # print(x)
    if x in city_name_list:
        pass
    else:
        city_name_list.append(x)
        # dataframe['location'].tolist()
print(city_name_list)




# ### URL dictionary creation ### ---------------------------------------------------------------------------------------
# city_name = ''
# url_dict = {}
#
#
# for x in city_name_list:
#     city_name = x.replace(" ", "")
#     x_url = f"{base_url}lat=__LATITUDE__&lon=__LONGITUDE__&appid={api_key}"
#     url_dict.update({x:{"url":x_url}})
#
# with open(f"City url Dict/ city url dict file.json", "w") as f:
#     f.write(f"{url_dict}")
#
# pprint(url_dict)



 ### requests response ### ---------------------------------------------------------------------------------------------

for x in city_name_list:
    params_x = x + "_params"
    print(params_x)
    responses = openmeteo.weather_api(base_url, params= params_x)
    print(responses)





### each city  request --------------------------------------------------------------------------------

atlanta_responses = openmeteo.weather_api(atlanta_full_url, params= atlanta_params)
chicago_responses = openmeteo.weather_api(base_url, params= chicago_params)
houston_responses = openmeteo.weather_api(base_url, params= sanfrancisco_params)
newyork_responses = openmeteo.weather_api(base_url, params= newyork_params)
sanfrancisco_responses = openmeteo.weather_api(base_url, params= houston_params)



atlanta_response = atlanta_responses[0]
chicago_response = chicago_responses[0]
houston_response = houston_responses[0]
newyork_response = newyork_responses[0]
sanfrancisco_response = sanfrancisco_responses[0]

print(atlanta_response)



#
# response_list_dict = {}
# for x in url_dict:
#
#     x_key = url_dict[x]
#
#     # print(x_key)
#
#     response = requests.get(x_key)
#     response_json = response.json()
#
#     # if response_json["cod"] != "404":
#     #
#     #     # store the value of "main"
#     #     # key in variable y
#     #     y = response_json["main"]
#     #
#     #     # store the value corresponding
#     #     # to the "temp" key of y
#     #     current_temperature = y["temp"]
#     #
#     #     # store the value corresponding
#     #     # to the "pressure" key of y
#     #     current_pressure = y["pressure"]
#     #
#     #     # store the value corresponding
#     #     # to the "humidity" key of y
#     #     current_humidity = y["humidity"]
#     #
#     #     # store the value of "weather"
#     #     # key in variable z
#     #     z = response_json["weather"]
#     #
#     #     # store the value corresponding
#     #     # to the "description" key at
#     #     # the 0th index of z
#     #     weather_description = z[0]["description"]
#     #
#     #     # print following values
#     #     print(" Temperature (in kelvin unit) = " +
#     #           str(current_temperature) +
#     #           "\n atmospheric pressure (in hPa unit) = " +
#     #           str(current_pressure) +
#     #           "\n humidity (in percentage) = " +
#     #           str(current_humidity) +
#     #           "\n description = " +
#     #           str(weather_description))
#     #
#     # else:
#     #     print(" City Not Found ")
#
#     # WRITE AND OVERWRITE EACH RESPONSE TXT FILE
#
#     # response.raise_for_status()
#
#
#     with open(f"WeatherCityResponseDirectory/{x} response file.txt", "w") as f:
#         f.write(f"{response_json}")
#
#
#
#
#
# # url_dict.update()
# # print(city_name_list)
# # print(url_dict)
# # print(response_list_dict)
# # print(response)
#
#
#
# # complete_url = base_url + "appid=" + "33ae3127a66a7f8d3391e53d13ceded8" + "&q=" + "Atlanta"
# # response = requests.get(complete_url)
# # x = response.json()
# # print(x)
#
#
#
