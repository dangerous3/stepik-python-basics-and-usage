from html.parser import HTMLParser
from urllib.request import urlopen
import requests
import re


class StepikHTMLParser(HTMLParser):
    def __init__(self, url1, url2, *args, **kwargs):
        # список ссылок
        self.links = []
        self.url1 = url1
        self.url2 = url2
        self.b = ""
        # вызываем __init__ родителя
        super().__init__(*args, **kwargs)
        # при инициализации отдаем парсеру содержимое страницы
        self.feed(self.read_site_content())


    def read_site_content(self):
        try:
            return str(urlopen(self.url1).read())
        except:
            print("No")

    def handle_starttag(self, tag, attrs):
        flag = False
        if tag == 'a':
            for attr in attrs:
                if re.search(r'http.*:\/\/.*', str(attr[1])):
                    self.links.append(str(attr[1]))
        for urls in self.links:
            r = requests.get(urls)
            if r.status_code == 200:
                if re.search(self.url2, r.text):
                    flag = True
            else:
                continue
        if flag == True:
            print("Yes")
            return True
        else:
            print("No")
            return False

u1 = input()
u2 = input()

a = StepikHTMLParser(u1, u2)
