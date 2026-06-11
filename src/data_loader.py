import csv

file_path = "data/interactions.csv"

with open(file_path, "r") as file:
    data = csv.reader(file)

dict = {}

for row in data:
    user = row[0]
    item = row[1]

    print(user, item)

