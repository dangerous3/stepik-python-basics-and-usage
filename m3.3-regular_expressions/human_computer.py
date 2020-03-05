'''Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки (нужно
выводить ВСЕ строки. не только замененные!).

Sample Input:

I need to understand the human mind
humanity

Sample Output:

I need to understand the computer mind
computerity'''

import sys
import re

for line in sys.stdin:
    if line:
        line = line.rstrip()
        if re.search(r'human', line):
            line = re.sub('human', 'computer', line)
        print(line)