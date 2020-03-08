'''В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
выведите их имена в лексикографическом порядке.

Примечание:
﻿В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

Пример входных данных:
4d8b92b34eb68a1b2c0003f4
537def3c139b21353f0006a6
4e2ed576477cc70001006f99

Пример выходных данных:
Abbott Mary
Warhol Andy
Abbas Hamra
'''

import requests
import json

# Данные для доступа к API
client_id = '...'
client_secret = '...'

# token request:
# curl -v -X POST "https://api.artsy.net/api/tokens/xapp_token?client_id=7eb64a7828d4b25b1c5d&client_secret=d89e8bce7c877611ebd082df026ecdc3"

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}

def artists_list(id):
    # инициируем запрос с заголовком
    url = "https://api.artsy.net/api/artists/" + str(id)
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    # разбираем ответ сервера
    j = json.loads(r.text)
    #print(j)
    return (int(j['birthday']), j['sortable_name'])

result = []

# Файл с данными: ./data/dataset_24476_4.txt

with open("./data/dataset_24476_4.txt", "r") as listid:
    for line in listid:
        line = line.strip()
        result.append(artists_list(line))
    result.sort(key = lambda tup: (tup[0], tup[1]))

# Выводим имена худодников
for i in result:
    print(i[1])



