'''

Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.
Пример архива: samples/sample.zip
Пример ответа: samples/sample_ans.txt
'''

import os
import urllib.request
import zipfile

# Файл с данными также здесь: samples/main.zip

url = "https://stepik.org/media/attachments/lesson/24465/main.zip"

sam_dir = "samples/2.4-6"

for_sorting = set()

urllib.request.urlretrieve(url, 'samples/main.zip')

z = zipfile.ZipFile('samples/main.zip', mode='r')
z.extractall(path=sam_dir)
z.close()

os.chdir(sam_dir)
curdir = os.getcwd()

# Файл c результатом: samples/result-2.4-6.txt

with open("../result-2.4-6.txt", "w") as wr:
    for root, dirs, files in os.walk(curdir):
        for file in files:
            if file.endswith(".py"):
                #print(os.path.join(root, file))
                fullpath = root
                relative = os.path.relpath(path=fullpath, start='/home/dangerous3/PycharmProjects/stepik-python-basics-and-usage/2.4_files_and_Python/samples/2.4-6')
                for_sorting.add(relative)
    for i in sorted(for_sorting):
        wr.write(i + "\n")









