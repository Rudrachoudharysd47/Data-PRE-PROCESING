import csv 
dataset1 = []
dataset2 = []
with open("final.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
with open("lastandfinal.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
headers1 = dataset1[0]
headers2 = dataset2[0]
planetdata1 = dataset1[1:]
planetdata2 = dataset2[1:]
headers = headers1+headers2
planetdata = []
for index,datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])
with open("finall1.csv","a+")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)

with open("finall1.csv")as input , open("final.csv","w",newline = "")as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if  any(field.strip () for field in row):
            writer.writerow(row)
 
