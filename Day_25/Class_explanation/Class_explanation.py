# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     next(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
    
#     print(temperatures)
 
import pandas as pd

data = pd.read_csv("weather_data.csv")

##Getting a serie
# print(data.temp)

##getting a row
# data[data.day == "Monday"]

#getting the row with highest temperature of the week
#data[data.temp == data.temp.max()]

## Top 3 temperatures
# top_3_temperatures = data.nlargest(3, 'temp')
# print(top_3_temperatures)

##
# monday = data[data.day == "Monday"]
# print(monday.condition)

# #Converting monday's temperature to farenheit
# monday = data[data.day == "Monday"]
# monday_temp_F = monday.temp * 9/5 +32
# print(monday_temp_F)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# data_dict = {
# "students": ["Anna", "Joel", "James", "Mark"],
# "scores": [76,86,54,65]
# }

# # Creating a dataframe from scratch
# score_data = pd.DataFrame(data_dict)
# print(score_data)

# # saving it into a csv
# score_data.to_csv("score_data.csv")