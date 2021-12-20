import csv
import wolframalpha
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from csv import reader

#west_coast_states = ['Colorado', 'Utah', 'Nevada', 'New Mexico', 'Idaho', '']
#wc_states = requests.get('https://www.law.cornell.edu/definitions/uscode.php?width=840&height=800&iframe=true&def_id=43-USC-64403383-1554264330&term_occur=999&term_src=title:43:chapter:35:subchapter:I:section:1702').text
#soup_wc = BeautifulSoup(wc_states, 'lxml')
input_wolfram_wc = "What are the West Coast states of the U.S.?"
app_id = "UY8J28-KPKYW5Y2RT"
client = wolframalpha.Client(app_id)
result = client.query(input_wolfram_wc)
answer = next(result.results).text
answers_wc = answer.split(' | ') 
answers_wc.extend(['Alaska', 'Hawaii']) #list of west coast states

input_wolfram_ec = "What are the East Coast states of the U.S.?"
app_id = "UY8J28-KPKYW5Y2RT"
client = wolframalpha.Client(app_id)
result = client.query(input_wolfram_ec)
answer = next(result.results).text
answers_ec = answer.split(' | ')  #list of east coast states
x = ['West Coast', 'East Coast']
y = []
with open('details.csv') as f:
    line = csv.reader(f)
    counter = 0
    for row in line:
        for element in answers_wc:
            if element in row[4].split() == True:
                counter+=1
    y.append(counter)
print(y)    