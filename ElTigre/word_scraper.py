import random
import requests
import string
import os


class WikiScraper:
    def __init__(self):
        self.list = []
        self.selected = []

    def truncate(self):
        try:
            self.stats = os.stat('words.txt')

            self.size = self.stats.st_size(1024 * 1024)

            if self.size > 1.0:
                self.file = open('words.txt', 'w')
        except:
            self.file = open('words.txt', 'a+')

        website = requests.get(
            "https://en.wikipedia.org/wiki/Special:Random")

        from bs4 import BeautifulSoup

        more = website.content

        soup = BeautifulSoup(website.text, 'html.parser')

        soup = soup.find('p').get_text()

        for i in string.digits:
            soup.replace(i, '')

        for i in string.punctuation:
            soup.replace(i, '')

        soup = str(soup).split()

        for i in soup:
            if i.isalpha() and len(i) > 4:
                self.selected.append(i)

        with self.file as scraped:
            for i in self.selected:
                scraped.write(f"{i}\r")

        scraped.close()


    def get_word(self):
        with open('words.txt', 'r') as scraped:
            for i in scraped.readlines():
                self.list.append(i.replace('\n', ''))
        return random.choice(self.list)


