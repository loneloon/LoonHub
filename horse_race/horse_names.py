import random
import requests

class HorseScraper:
    def __init__(self):
        website = requests.get(
            "https://grammar.yourdictionary.com/parts-of-speech/adjectives/List-of-Descriptive-Adjectives.html")

        another = requests.get("https://www.findnicknames.com/cool-nicknames/")

        from bs4 import BeautifulSoup

        soup = BeautifulSoup(website.text, 'html.parser')

        soup2 = BeautifulSoup(another.text, 'html.parser')

        adj_list = str(soup.find('tbody'))

        tags = ['<tbody>', '</tbody>', '</td>', '<td>', '<p>', '</p>', '<tr>', '</tr>']

        for tag in tags:
            if tag in adj_list:
                adj_list = adj_list.replace(tag, ' ')

        self.adjectives = adj_list.split(' ')

        while '' in self.adjectives:
            self.adjectives.remove('')

        for idx, i in enumerate(self.adjectives):
            self.adjectives[idx] = i[0].upper() + i[1:]

        self.nicknames = soup2.find(class_="entry-content").get_text().split('\n')

        while any(len(i) > 10 for i in self.nicknames):
            for idx, i in enumerate(self.nicknames):
                if len(i) > 10:
                    del self.nicknames[idx]

        while '' in self.nicknames:
            self.nicknames.remove('')

    def horse_name(self):
        return str(random.choice(self.adjectives) + ' ' + random.choice(self.nicknames))


