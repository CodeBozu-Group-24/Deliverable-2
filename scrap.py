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
    data = requests.get(link)
    soup = BeautifulSoup(data, 'lxml')
