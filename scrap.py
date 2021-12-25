from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
import pandas as pd
from WikipediaClasses import WikipediaPolitician

data = pd.read_csv(r'details.csv')
ids = list(data['Politician'])
#print(ids)

linkz = [WikipediaPolitician.getLinkFromName(x) for x in ids]
print(linkz)

for link in linkz:
    data = requests.get(link).text
    soup = BeautifulSoup(data, 'lxml')
    occupation = soup.findAll('div', class_='hlist hlist-separated')
    print(occupation[-1])
    print("============================================================")
    
