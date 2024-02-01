import csv

with open('OneDayInternational.csv','r')as csv_file:
    csv_reader=csv.DictReader(csv_file)
    countries=set()
    for row in csv_reader:
        countries.add(row['Versus'])
    countries=sorted(countries)
    print(countries)