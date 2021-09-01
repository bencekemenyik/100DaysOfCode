# import pandas
#
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# numbers = squirrel_data["Primary Fur Color"].value_counts()
# colors = squirrel_data["Primary Fur Color"].unique()
#
#
# data_dict = {
#     "Fur Color": [colors[1], colors[2], colors[3]],
#     "Count": [numbers[0], numbers[1], numbers[2]]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("squirrel_count.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_teacher.csv")
