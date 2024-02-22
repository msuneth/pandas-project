# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #         #print(row[1]
# # print(temperatures)
# # #print(data)
#
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data['temp'].to_list()
# # print(temp_list)
# #
# # print(f"Average temp: {round(sum(temp_list)/len(temp_list),1)}")
# # print(data['temp'].mean())
# # print(f"Max temp: {data['temp'].max()}")
# #
# # print(data.condition)
# # print(data["condition"])
# # print(data[data.day == "Monday"])
# # # print(data[data.temp == data.temp.max()])
# # monday_temp = data[data.day == "Monday"].temp
# # print(monday_temp)
# # print(f"temp in F:{monday_temp * 9 / 5 + 32}")
# # #(0°C × 9/5) + 32
#
# data_dict = {"students":['suneth','niwantha','perera'],"scores":[10,20,30]}
# print(data_dict)
# data_new = pandas.DataFrame(data_dict)
# print(data_new)
# data.to_csv("data.csv")
#
# raw_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# #filtered_data = raw_data['Primary Fur Color']
# grey = len(raw_data[raw_data['Primary Fur Color'] == 'Gray'])
# cinnamon = len(raw_data[raw_data['Primary Fur Color'] == 'Cinnamon'])
# black = len(raw_data[raw_data['Primary Fur Color'] == 'Black'])
# #grey = filtered_data[filtered_data['Primary Fur Color'] == 'Gray'].count()
# data_dict = {"Fur Color":['grey','cinnamon','black'],"Count":[grey,cinnamon,black]}
# # data_dict = {"Fur Color":}
# print(data_dict)
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

import asyncio


async def fetch_data(task_number):
    print(f"Fetching data...{task_number}")
    await asyncio.sleep(1)  # Simulate I/O-bound operation
    print(f"Data fetched!{task_number}")


async def main():
#def main():
    task1 = fetch_data(1)
    task2 = fetch_data(2)

    await asyncio.gather(task1, task2)


asyncio.run(main())
#main()
