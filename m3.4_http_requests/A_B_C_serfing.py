'''
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">,
возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за
один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML
документы.

Sample Input 1:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:

Yes

Sample Input 2:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html

Sample Output 2:

No

Sample Input 3:

https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 3:

Yes

'''

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
        self.check_links()


    def read_site_content(self):
            return str(urlopen(self.url1).read())

    def handle_starttag(self, tag, attrs):

        if tag != 'a':
            return
        elif tag == 'a':
            for attr in attrs:
                if re.search(r'http.*:\/\/.*', str(attr[1])):
                    self.links.append(str(attr[1]))

    def check_links(self):
        flag = False
        if len(self.links) == 0:
            print("No")
            return False
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

try:
    a = StepikHTMLParser(u1, u2)
except:
    print("No")
