'''Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных
в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное
число раз в 2015 году.

Файл с данными: ./data/Crimes.csv'''

import csv
import collections as col

crimes = []

with open('./data/Crimes.csv', "r") as csvfile:
    crime = csv.reader(csvfile)
    for row in crime:
        crimes.append(row[5])

print(col.Counter(crimes).most_common(1))