import requests, json
import pandas as pd
from fontTools.misc.cython import returns

base_url = "http://api.openweathermap.org/data/2.5/weather"

# city_name = input("Enter city name : ")


dataframe = pd.read_csv("data/equipment_anomaly_data.csv")
# print(dataframe.head())


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

### URL dictionary creation ### ---------------------------------------------------------------------------------------------
city_name = ''
url_dict = {}
for x in city_name_list:
    # url_dict.update({x:city_name})
    city_name = x.replace(" ", "")
    url_dict.update({x: base_url + "appid=" + api_key + "&q=" + city_name})





### requests response ### ---------------------------------------------------------------------------------------------

response_list_dict = {}
for x in url_dict:

    x_key = url_dict[x]

    # print(x_key)

    response = requests.get(x_key)
    response_json = response.json()

    # if response_json["cod"] != "404":
    #
    #     # store the value of "main"
    #     # key in variable y
    #     y = response_json["main"]
    #
    #     # store the value corresponding
    #     # to the "temp" key of y
    #     current_temperature = y["temp"]
    #
    #     # store the value corresponding
    #     # to the "pressure" key of y
    #     current_pressure = y["pressure"]
    #
    #     # store the value corresponding
    #     # to the "humidity" key of y
    #     current_humidity = y["humidity"]
    #
    #     # store the value of "weather"
    #     # key in variable z
    #     z = response_json["weather"]
    #
    #     # store the value corresponding
    #     # to the "description" key at
    #     # the 0th index of z
    #     weather_description = z[0]["description"]
    #
    #     # print following values
    #     print(" Temperature (in kelvin unit) = " +
    #           str(current_temperature) +
    #           "\n atmospheric pressure (in hPa unit) = " +
    #           str(current_pressure) +
    #           "\n humidity (in percentage) = " +
    #           str(current_humidity) +
    #           "\n description = " +
    #           str(weather_description))
    #
    # else:
    #     print(" City Not Found ")

    # WRITE AND OVERWRITE EACH RESPONSE TXT FILE

    # response.raise_for_status()


    with open(f"WeatherCityResponseDirectory/{x} response file.txt", "w") as f:
        f.write(f"{response_json}")





# url_dict.update()
# print(city_name_list)
# print(url_dict)
# print(response_list_dict)
# print(response)


