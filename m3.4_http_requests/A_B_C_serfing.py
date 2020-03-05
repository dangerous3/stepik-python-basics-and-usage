from html.parser import HTMLParser
from urllib.request import urlopen

class StepikHTMLParser(HTMLParser):
    def __init__(self, url1, url2, *args, **kwargs):
        # список ссылок
        self.links = []
        #self.site_name = site_name
        self.url1 = url1
        self.url2 = url2
        # имя сайта
        # вызываем __init__ родителя
        super().__init__(*args, **kwargs)
        # при инициализации "скармливаем" парсеру содержимое страницы
        self.feed(self.read_site_content())

    def read_site_content(self):
        return str(urlopen(self.url1).read())

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])
            self.check_links_to(self.url2, self.links)

    def check_links_to(self, url, urllist):
        self.url = url
        self.urllist = urllist
        self.flag = False
        for urls in self.urllist:
            if self.url in urls:
                self.flag = True
                print("True")
                return True
        if self.flag == False:
            print("False")
            return False

u1 = input()
u2 = input()

a = StepikHTMLParser(u1, u2)

