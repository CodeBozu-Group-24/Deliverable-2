from bs4 import BeautifulSoup
import requests
import csv
import wolframalpha
import matplotlib.pyplot as plt
from csv import reader
import pandas as pd

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
    lines = csv.reader(f)
    counter = 0
    for row in lines:
        if any(answers_wc[i] in row[4] for i in range(len(answers_wc))) == True:
            counter+=1 
    f.close()        
y.append(counter) 

with open('details.csv') as f:
    lines = csv.reader(f)
    counter2 = 0
    for row in lines:
        if any(answers_ec[i] in row[4] for i in range(len(answers_ec))) == True:
            counter2+=1 
    f.close()        
y.append(counter2)

plt.bar(x, y, color = 'b', width = 0.72, label = "Distribution")
plt.xlabel('Coasts')
plt.ylabel('Officials (Presidents and Vice Presidents)')
plt.title('Distribution of US Govt. Officials (Birthplace) in West Coast and East Coast')
plt.legend()
plt.show()

#relating months of birth and chances of being elected
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
indices = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
y_initial = []
with open('details.csv') as f:
    lines = csv.reader(f)
    counter3 = 0
    for row in lines:
        for ind in indices:
            if str(row[2][5:7]) == ind:
                y_initial.append(months[indices.index(ind)])
    f.close()

y_final = []
for i in range(len(months)):
    c = y_initial.count(months[i])
    y_final.append(c)
y_final[6] = y_final[6]+1

plt.bar(months, y_final, color = 'b', width = 0.72, label = "Distribution")
plt.xlabel('Months')
plt.ylabel('Number of Officials (Presidents and Vice Presidents)')
plt.title('Distribution of Number of Officials to Birth Months')
plt.legend()
plt.show() 

#analyzing the distribution on the basis of winter or not winter
x_wnw = ["Winter", "Not Winter"]
y_wnw = []
with open('details.csv') as f:
    lines = csv.reader(f)
    counter_w = 0
    counter_nw = 0
    for row in lines:
            if str(row[2][5:7]) in ['01', '02', '12']:
                counter_w += 1
            elif str(row[2][5:7]) in ['03', '04', '05', '06', '07', '08', '09', '10', '11']:
                counter_nw += 1     
    y_wnw.append(counter_w)
    y_wnw.append(counter_nw)                
    f.close()

plt.bar(x_wnw, y_wnw, color = 'y', width = 0.72, label = "Distribution")
plt.xlabel('Seasons')
plt.ylabel('Number of Officials (Presidents and Vice Presidents)')
plt.title('Seasonal Distribution of Birth Months of Officials')
plt.legend()
plt.show()   

#Occupation
import scrap

#family members  
data = requests.get('https://en.wikipedia.org/wiki/Political_family').text
soup = BeautifulSoup(data, 'lxml')
text = soup.findAll('a', href=True)
list_all = []
for string in text:
    str = string.text
    if 'family' in str:
        list_all.append(str)
list_final = list_all[5:13]
list_final.append('Harrison family') #got excluded due to inconsistency
list_final.append('Clinton family')  #got excluded due to inconsistency
list2 = []
for ele in list_final:
    if ele not in list2:
        list2.append(ele)
names = []

for ele in list2:
    ele = ele.split()
    if 'The' in ele and 'family' in ele:
        names.append(ele[1])
    elif 'family' in ele:
        names.append(ele[0])    

data = pd.read_csv(r'details.csv')
ids = list(data['Politician'])

counter = 0
for elements in ids:
    str = elements.split()
    for ele in names:
        if ele in str:
            counter+=1
y = []
y.append(counter)
y.append(len(ids)-counter)

x = ["Politicians", "Not Politicians"]
plt.bar(x, y, color = 'b', width = 0.72, label = "Distribution")
plt.ylabel('No. of Officials (Presidents and Vice Presidents)')
plt.title('Distribution of US Govt. Officials on the basis of Parental Political Background')
plt.legend()
plt.show()       