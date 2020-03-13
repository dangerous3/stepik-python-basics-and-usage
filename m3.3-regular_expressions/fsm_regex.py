'''
Примечание:
Эта задача является дополнительной, то есть ее решение не принесет вам баллы.
Задача сложнее остальных задач из этого раздела, и идея ее решения выходит за рамки простого понимания регулярных
выражений как средства задания шаблона строки.
Мы решили включить данную задачу в урок, чтобы показать, что регулярным выражением можно проверить не только
"внешний вид" строки, но и заложенный в ней смысл.


Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.

Двоичной записью числа называется его запись в двоичной системе счисления.

Примечание 2:
﻿Данная задача очень просто может быть решена приведением строки к целому числу и проверке остатка от деления на три,
но мы все же предлагаем вам решить ее, не используя приведение к числу.

Sample Input:

0
10010
00101
01001
Not a number
1 1
0 0

Sample Output:

0
10010
01001

# correct regex: (1(01*0)*1|0)*
# see also test_binary_3() on https://github.com/qntm/greenery/blob/master/greenery/lego_test.py
# see also: https://itnan.ru/post.php?c=1&p=420817
# see also: https://fooobar.com/questions/1247901/convert-finite-state-machine-to-regular-expression
'''

from greenery import fsm, lego
import re
import sys

A, B, C = range(3)
a, b = '1', '0'

machine = fsm.fsm(
    alphabet = {a, b},
    states   = {"initial", "zero", A, B, C, None},
    initial  = "initial",
    finals   = {"zero", A},
    map      = {
        "initial" : {b : "zero", a : B},
        "zero" : {a : None, b : None},
        A : {a : B, b : A},
        B : {a : A, b : C},
        C : {a : C, b : B},
        None : {a : None, b : None},
    },
)

# convert it to regex
rex = lego.from_fsm(machine)

print(machine)

print(rex)
# (0|1(01*0)*1)*1(01*0)*01*

for line in sys.stdin:
    if line:
        line = line.rstrip()
        if re.fullmatch('{rex}', line):
            print(line)
        elif line == '0':
            print('0')

# For stepik solution checker:
# import re
# import sys
#
# for line in sys.stdin:
#     if line:
#         line = line.rstrip()
#         if re.fullmatch(r'(1(01*0)*1|0)*', line):
#             print(line)
#         elif line == '0':
#             print('0')

