import json
from collections import defaultdict

js = json.loads(input())

print(js)

sibling = []
inverted = {}

# Конвертирование в структуру данных:
# inverted = {ancestor : [list of siblings]}
for dct in js:
    if len(dct['parents']) != 0:
        for parent in dct['parents']:
           if inverted.get(parent) == None:
                inverted[parent] = [dct['name']]
           else:
               inverted[parent].append(dct['name'])


print(inverted)

# Функция нахождения всех путей между двумя нодами
# Используется техника backtracking (см. http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml)
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths