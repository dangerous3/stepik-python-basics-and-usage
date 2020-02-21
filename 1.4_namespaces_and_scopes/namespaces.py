namespaces = {}
namespaces['global'] = {'parent': 'None', 'vars' : []}

def create(namespace, parent='global'):
    if namespace in namespaces:
        print('The namespace ' + namespace + ' is already existed')
        return
    else:
        namespaces[namespace] = {'parent': parent, 'vars': []}
        return namespaces[namespace]


def add(namespace, *var):
    for i in var:
        namespaces[namespace]['vars'].append(i)

def get(namespace, var):
    if var not in namespaces[namespace]['vars']:
        parent = namespaces[namespace]['parent']
        if parent != 'None':
            get(namespaces[parent], var)
    else:
        print(namespace)
        return namespace


n = int(input())

for i in range(n):
    req = input().split()
    if req[0] == 'create':
        create(req[1], req[2])
        for j in namespaces:
            print('Namespace ' + '\'' + j + '\'' + ": " + str(namespaces[j]))
    elif req[0] == 'add':
        add(req[1], req[2])
        for j in namespaces:
            print('Namespace ' + '\''+ j + '\'' + ": " + str(namespaces[j]))



