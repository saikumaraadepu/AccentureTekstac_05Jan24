import csv

year_runs={}
with open('OneDayInternational.csv','r')as csv_file:
    csv_reader=csv.DictReader(csv_file)
    for row in csv_reader:
        year=row['MatchDate'].split('/')[2]
        runs=int(row['Runs'])
        year_runs[year]=year_runs.get(year,0)+runs
for year,runs in sorted(year_runs.items()):
    print(year,runs)
