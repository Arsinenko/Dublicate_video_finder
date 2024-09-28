import csv

with open("train.csv", "r") as file:
    reader = csv.reader(file)
    print(len(reader))
    #for row in reader:
    #    print(row)