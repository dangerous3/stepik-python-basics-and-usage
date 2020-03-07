'''Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов,
 которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за
 исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru

Пример для отладки: https://stepik.org/lesson/24471/step/7?discussion=378280&unit=6780
'''

import requests
import re

urls = []

page_url = input()
r = requests.get(page_url)
page_source = r.text
r.text.strip()
regex_res = re.findall(
    r'<[a|(?:script)]\s+.*?href=[\"|\']?(?:\w+\:\/\/)?((?:\w[a-zA-Z0-9\.\-_]+)(?:\.)([a-zA-Z]){2,6})(?:[a-zA-Z0-9\.\&\/\?\:@\-_=#])*',
    page_source)

s = set()

for i in regex_res:
    s.add(i[0])

urls = list(s)
urls.sort()

for i in urls:
    print(i)


