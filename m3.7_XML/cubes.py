'''Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

 Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками,
имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

Sample Output:

4 3 1
'''

from xml.etree import ElementTree as ET

def count_cube(tree):
    countd = {"red": 0, "green": 0, "blue": 0}
    counter = 0

    def goto_child(element):
        nonlocal counter
        counter += 1
        for child in element:
            countd[child.attrib["color"]] += counter
            goto_child(child)
        counter -= 1

    goto_child(tree)
    print("{} {} {}".format(countd["red"], countd["green"], countd["blue"]))

sample = input()

tree = ET.Element("tree")
tree.append(ET.fromstring(sample))

count_cube(tree)