'''
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.

Sample Input:

attraction
buzzzz

Sample Output:

atraction
buz

'''

import sys
import re

for line in sys.stdin:
    if line:
        line = line.rstrip()
        line = re.sub(r'(\w)\1{1,}', r'\1', line)
        print(line)