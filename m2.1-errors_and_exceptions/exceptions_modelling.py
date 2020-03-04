'''Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде
будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого
положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.

Формат входных данных

В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.
Формат выходных данных

Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом
поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.

Sample Input:

4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Sample Output:

FileNotFoundError

'''

import pprint

pp = pprint.PrettyPrinter(indent=4)

inheritance = {}
ancestorset = set()

# ввод числа исключений
n = int(input())

# ввод исключений
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


# Используется DFS (depth-first search) (см. https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/)

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]['ancestors'] - visited)
    return visited  # возвращает список из элемента и его предков


# ввод количества запросов для исключений
n = int(input())

# ввод запросов для исключений

already_raised = []
found = False

for i in range(n):
    exception = input()
    dfs_result = dfs(inheritance, exception)
    if len(dfs_result) == 1 and exception not in already_raised:
        already_raised.append(exception)
        continue
    else:
        dfs_result.remove(exception)
        if exception not in already_raised:
            for j in dfs_result:
                if j in already_raised:
                    print(exception)
                    found = True
                    break
            if found == False:
                already_raised.append(exception)
        else:
            continue
