import csv
import datetime

##sample large data set to extract only Obama and McCain donations
file = csv.DictReader(open('small_sample.csv', 'r'))
frontrunner = ['P80003338', 'P80002801']
extraction = []

for line in file:
    for i in frontrunner:
        if i in line:
            extraction.append(line[:-1])
print extraction

##output new array into csv
with open("frontrunnerdata.csv", 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(extraction)
f.close()


