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

params = {
	"latitude": lat,
	"longitude": long,
    "start_date": start_day,
    "end_date": end_day,

}

# responses = openmeteo.weather_api(base_url, params=params)


dataframe = pd.read_csv("data/equipment_anomaly_data.csv")
city_name_row_dump = dataframe['location'].tolist()
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
# print(city_name_list)

# ### LATLONG  ### ---------------------------------------------------------------------------------------------
# dataframe_latlong = pd.read_csv("data/city Lat Long list.csv")
# city_name_row_dump = dataframe_latlong['location'].tolist()

# {'Atlanta':
#      {'lat':""},
#  'Chicago': ,
#  'San Francisco': ,
#  'New York': ,
#  'Houston': }


# ### URL dictionary creation ### ---------------------------------------------------------------------------------------
city_name = ''
url_dict = {}


for x in city_name_list:
    city_name = x.replace(" ", "")
    x_url = f"{base_url}lat={lat}&lon={long}&appid={api_key}"
    url_dict.update({x:{"url":x_url}})
    url_dict["lat"] = ""


with open(f"City url Dict/ city url dict file.txt", "w") as f:
    f.write(f"{url_dict}")

pprint(url_dict)



# ### requests response ### ---------------------------------------------------------------------------------------------
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
