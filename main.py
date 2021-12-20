import csv
import wolframalpha
import matplotlib.pyplot as plt
from csv import reader

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

plt.bar(x, y, color = 'g', width = 0.72, label = "Distribution")
plt.xlabel('Coasts')
plt.ylabel('Officials (Presidents and Vice Presidents)')
plt.title('Distribution of US Govt. Officials (Birthplace) in West Coast and East Coast')
plt.legend()
plt.show()
plt.savefig('graph.png')