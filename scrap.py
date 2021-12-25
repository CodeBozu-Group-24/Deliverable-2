import csv
from csv import writer
import pandas as pd
from WikipediaClasses import WikipediaPolitician
import wolframalpha
from collections import Counter
import matplotlib.pyplot as plt

def scrap():
    data = pd.read_csv(r'details.csv')
    ids = list(data['Politician'])
    #print(ids)

    linkz = [WikipediaPolitician.getLinkFromName(x) for x in ids]
    #print(linkz)

    counter = Counter()
    """
    for link in linkz:
        data = requests.get(link).text
        soup = BeautifulSoup(data, 'lxml')
        #occupation = soup.findAll('div', class_='hlist hlist-separated')
        #print(occupation.parent.get_text())
        #print("============================================================")
    """
    for official in ids:
        input_wolfram = "What were the occupations of {}?".format(official)
        app_id = "UY8J28-KPKYW5Y2RT"
        client = wolframalpha.Client(app_id)
        result = client.query(input_wolfram)  
        answer = next(result.results).text  
        listt = answer.split(" | ")
        counter.update(listt)

    toGraph = counter.most_common(30)
    people = list(zip(*toGraph))[0]
    popularityy = list(zip(*toGraph))[1]
    plt.pie(popularityy, labels=people, autopct='%1.2f%%')


    plt.title("Distribution of Officials on the basis of Occupations")
    plt.tight_layout()
    plt.show()

scrap()    