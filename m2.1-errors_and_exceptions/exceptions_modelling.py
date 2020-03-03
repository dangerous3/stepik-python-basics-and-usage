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

