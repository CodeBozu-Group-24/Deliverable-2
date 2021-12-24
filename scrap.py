from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
import pandas as pd
from WikipediaClasses import WikipediaPolitician

data = pd.read_csv(r'details.csv')
ids = list(data['Politician'])

linkz = [WikipediaPolitician.getLinkFromName(x) for x in ids]

for link in linkz:
    data = requests.get(link).text
    soup = BeautifulSoup(data, 'lxml')
    for title in soup.findAll('div', {"id":"mw-pages"}):
        names = title.find_all('li')
        for i in range(len(names)):
            if names_21[i].get_text() in ids:
                pass #here we have to code

    
