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
    if len(a) > 1:
        sibling, ancestor = a.split(":")
        sibling = sibling.strip()
        ancestor = ancestor.strip()

        if inheritance.get(sibling) == None:
            for j in ancestor.split():
                ancestorset.add(j)
            inheritance[sibling] = { 'ancestors' :  ancestorset }
            ancestorset = set()
        else:
            for j in ancestor.split():
                inheritance[sibling]['ancestors'].add(j)
    else:
        sibling = a
        inheritance[sibling] = {'ancestors': set()}

pp.pprint(inheritance)

def check_classname(name):
    pattern = re.compile("^[a-zA-Z]+$")
    if len(name) > 50:
        return "No"
    elif not pattern.match(name):
        return("No")


anc_flag = False
ancestor_original = ''

def is_ancestor(class1, class2):
    ancestor = class1
    if anc_flag == False:
        ancestor_original = class1
    sibling = class2
    exec('anc_flag=True', globals())

    if sibling not in inheritance.keys() or ancestor not in inheritance.keys():
        print("No")
        return "No"
    if check_classname(class1) == "No" or check_classname(class2) == "No":
        print("No")
        return "No"
    if ancestor == sibling:
        print("Yes")
        return "Yes"
    if inheritance[sibling]['ancestors'] == set():
        print("No")
        return "No"
    for anc in inheritance[sibling]['ancestors']:
        if anc == set():
            print("No")
            return "No"
        elif ancestor in inheritance[sibling]['ancestors']:
            print("Yes")
            return "Yes"
        else:
            if inheritance[anc]['ancestors'] == set() and anc == ancestor_original:
                return (is_ancestor(anc, anc))
            for k in inheritance[anc]['ancestors']:
                return(is_ancestor(ancestor, k))

# ввод количества запросов
n = int(input())

# ввод запросов на то я вляется ли class1 предком class2
# Формат запроса: class1 class2
for i in range(n):
    class1, class2 = input().split()
    if class1 == class2:
        if check_classname(class1) == "No" or check_classname(class2) == "No":
            print("No")
        else:
            print("Yes")
    else:
        is_ancestor(class1, class2)


