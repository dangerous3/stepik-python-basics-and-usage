'''В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический
факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring'''

import requests
import json

with open("./data/dataset_24476_3.txt", "r") as num:
    for line in num:
        line = line.strip()
        url = 'http://numbersapi.com/{}/math?json=true'.format(line)
        r = requests.get(url, proxies=dict(http='socks5://127.0.0.1:9050',
                                 https='socks5://127.0.0.1:9050'))
        #print(r.text)
        ans = json.loads(r.text)
        if ans['found'] == True:
            print('Interesting')
        else:
            print("Boring")


