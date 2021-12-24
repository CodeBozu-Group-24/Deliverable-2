from bs4 import BeautifulSoup
import requests
from requests.api import request
import re
from csv import writer
import requests
from bs4 import BeautifulSoup
class notCSV(Exception):
    def __init__(self, *args, **kwargs):
        pass
    pass

class WikipediaPolitician():
    def __init__(self, link):
        data = requests.get(link).text
        soup = BeautifulSoup(data, "lxml")
        self.name = soup.find('div', class_="fn").text

        self.birth_name = soup.find('div', class_="nickname").text

        self.dob = soup.find('span', class_='bday').text

        age = soup.find('span', class_='noprint ForceAgeToShow').text
        self.age = str(age)

        data_full = soup.find_all('span', class_='noprint')
        self.birth_place = data_full[0].parent.get_text()

        party_full = soup.find_all('th', class_='infobox-label')
        self.party_reduced = party_full[4].parent.get_text()

        self.json = {
            "name":self.name,
            "birth_name":self.birth_name,
            "dob":self.dob,
            "age":self.age,
            "birth_place":self.birth_place,
            "party":self.party_reduced
        }

    @staticmethod
    def getLinkFromName(name):
        converted = re.sub("\s", "_", name)
        return "https://en.wikipedia.org/wiki/%s"%(converted)

    def writeToFile(self, file):
        if re.match(".+\.csv", file):
            with open(file, "a") as f:
                writer_ob = writer(f)
                writer_ob.writerow([self.name,
                    self.birth_name,
                    self.dob,
                    self.birth_place,
                    self.party_reduced
                ])
        else:
            raise notCSV("thats not a csv file lmao")