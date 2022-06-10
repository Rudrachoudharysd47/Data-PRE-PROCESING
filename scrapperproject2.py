from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(url)
soup = bs(page.text,"html.parser")
table = soup.find("table")
templist = []
tablerows = table.find_all("tr")
for tr in tablerows:
    td = tr.find_all("td")
    row = [i.text.rstrip()for i in td]
    templist.append(row)
starnames = []
distance = []
mass = []
radius = []
lum = []
for i in range(1,len(templist)):
    starnames.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lum.append(templist[i][7])
df = pd.DataFrame(list(zip(starnames,distance,mass,radius,lum)),columns = ["starnames","distance","mass","radius","lum"])
print(df)
df.to_csv("bright_stars.csv")
import csv
data = []
with open("bright_stars.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
headers = data[0]
planetdata = data[1:]
for datapoint in planetdata:
    datapoint[0] = datapoint[0].lower()
planetdata.sort(key = lambda planetdata:planetdata[0])
with open("nowsorted.csv","a+")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)

with open("nowsorted.csv")as input , open("lastandfinal.csv","w",newline = "")as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if  any(field.strip () for field in row):
            writer.writerow(row)