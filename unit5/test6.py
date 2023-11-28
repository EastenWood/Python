import csv

csv_read = csv.reader(open("sec.csv", encoding="utf-8"))
for row in csv_read:
    print(row)
