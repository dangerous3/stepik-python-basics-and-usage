'''Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Формат входных данных

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No",
если не является.

Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A

Sample Output:

Yes
Yes
Yes
No

'''

import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

inheritance = {}
ancestorset = set()

# ввод числа классов
n = int(input())

# ввод наследования классов
for i in range(n):
    a = input()
    if len(a.split()) > 1:
        sibling, ancestor = a.split(":")
        sibling = sibling.strip()
        ancestor = ancestor.strip()

        if inheritance.get(sibling) == None:
            for j in ancestor.split():
                ancestorset.add(j)
            inheritance[sibling] = {'ancestors': ancestorset}
            ancestorset = set()
        else:
            for j in ancestor.split():
                inheritance[sibling]['ancestors'].add(j)
    else:
        sibling = a
        inheritance[sibling] = {'ancestors': set()}

pp.pprint(inheritance)


# Проверка имени класса (не более 50 символов, используются только латинские символы). Не использую в решении, написана на всякий случай
def check_classname(name):
    pattern = re.compile("^[a-zA-Z]+$")
    if len(name) > 50:
        return "No"
    elif not pattern.match(name):
        return ("No")


# Используется алгоритм BFC (обход в ширину, breadth-first search)
def is_ancestor(class1, class2):
    ancestor = class1
    sibling = class2

    visited = []
    queue = []

    visited.append(sibling)
    queue.append(sibling)

    while queue:
        s = queue.pop(0)
        # print("Next vertex: " + s )
        if s == ancestor:
            print("Yes")
            return "Yes"
        else:
            if inheritance.get(s) == None:
                print("No")
                return "No"
            for neighbour in inheritance[s]['ancestors']:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
    print("No")
    return "No"


# ввод количества запросов
n = int(input())

# ввод запросов на то я вляется ли class1 предком class2
# Формат запроса: class1 class2
for i in range(n):
    class1, class2 = input().split()
    if class1 == class2:
        # if check_classname(class1) == "No" or check_classname(class2) == "No":
        #     print("No")
        # else:
        print("Yes")
    else:
        is_ancestor(class1, class2)
