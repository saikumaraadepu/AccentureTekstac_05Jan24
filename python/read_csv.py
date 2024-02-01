import csv

with open('OneDayInternational.csv','r')as csv_file:
    csv_reader=csv.DictReader(csv_file)
    count=0
    for row in csv_reader:
        print(row)
        count+=1
        if count==10:
            break