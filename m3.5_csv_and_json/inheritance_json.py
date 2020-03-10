import json

js = json.loads(input())

print(js)

transposed = {}
js_transposed = []
ts = set()

for i in js:
    if len(i['parents']) != 0:
        for j in i['parents']:
            if j != i['name']:
                ts.add(i['name'])
                transposed[j] = ts

print(transposed)

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