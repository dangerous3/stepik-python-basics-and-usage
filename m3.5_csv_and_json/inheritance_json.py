import json

js = json.loads(input())

#print(js)

res = {}
graph= {}

for dct in js:
    for parent in dct['parents']:
        if parent not in graph:
            graph[parent] = [dct['name']]
        else:
            graph[parent].append(dct['name'])



# Функция нахождения пути между двумя нодами
# Используется техника backtracking (см. http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml)
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start not in graph:
        return None
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None

for dct in js:
    if dct['name'] not in graph:
        graph[dct['name']] = []

for start in graph:
    res[start] = 0
    for end in graph:
        if find_path(graph, start, end):
            res[start] += 1

for i in sorted(res):
    print('{} : {}'.format(i, res[i]))

