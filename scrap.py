from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
import pandas as pd
from WikipediaClasses import WikipediaPolitician

#presidents
data21_pres = requests.get('https://en.wikipedia.org/wiki/Category:21st-century_presidents_of_the_United_States').text
soup21_pres = BeautifulSoup(data21_pres, 'lxml')
data20_pres = requests.get('https://en.wikipedia.org/wiki/Category:20th-century_presidents_of_the_United_States').text
soup20_pres = BeautifulSoup(data20_pres, 'lxml') 

#Vice-Presidents
data21_vp = requests.get("https://en.wikipedia.org/wiki/Category:21st-century_vice_presidents_of_the_United_States").text
soup21_vp = BeautifulSoup(data21_vp, 'lxml')
data20_vp = requests.get("https://en.wikipedia.org/wiki/Category:20th-century_vice_presidents_of_the_United_States").text
soup20_vp = BeautifulSoup(data20_vp, 'lxml')
data19_vp = requests.get("https://en.wikipedia.org/wiki/Category:19th-century_vice_presidents_of_the_United_States").text
soup19_vp = BeautifulSoup(data19_vp, 'lxml')


data = pd.read_csv(r'details.csv')
ids = list(data['Politician'])

for title in soup21_pres.findAll('div', {"id":"mw-pages"}):
    names_21 = title.find_all('li')
list21_pres = []    
for i in range(len(names_21)):
    if names_21[i].get_text() in ids:


print(ids)

linkz = [WikipediaPolitician.getLinkFromName(x) for x in ids]
print(linkz)

