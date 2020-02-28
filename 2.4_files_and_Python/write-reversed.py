'''Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab'''


filepath = "/home/dangerous3/Загрузки/dataset_24465_4.txt"
file_write = "samples/write-4step.txt"

# Файл с данными: samples/dataset_24465_4.txt

with open(filepath, "r") as read1, open(file_write, "w") as wr2:
    text_read = read1.readlines()
    for item in reversed(text_read):
        wr2.write(item)