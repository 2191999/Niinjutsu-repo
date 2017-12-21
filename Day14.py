import csv

with open("Day14.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Animal", "Dog"])
    writer.writerow(["Bird", "Kingfisher"])


with open("Day14.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("Day14.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Sweet","GulabJamun"])


with open("Day14.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("Day14.csv","w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Animal", "Dog"])
    writer.writerow(["Bird", "Kingfisher"])

with open("Day14.csv", "r+") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("Day14.csv","w") as csvfile:
    fieldnames = ["id", "title"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"id":123,"title":"new title"})
