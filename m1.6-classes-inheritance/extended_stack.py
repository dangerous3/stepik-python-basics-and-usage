'''Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо поддерживать
добавление элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать операции сложения,
вычитания, умножения и целочисленного деления.

Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент (top1), затем
снимается следующий верхний элемент (top2), и затем как результат операции сложения на вершину стека кладется
элемент, равный top1 + top2.

Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) и целочисленного
деления (top1 // top2).

Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.

Примечание
Для добавления элемента на стек используется метод append, а для снятия со стека – метод pop.
Гарантируется, что операции будут совершаться только когда в стеке есть хотя бы два элемента.
'''

class ExtendedStack(list):

    def sum(self):
        # операция сложения
        self.top1 = self.pop()
        self.top2 = self.pop()
        self.res = self.top1 + self.top2
        self.append(self.res)

    def sub(self):
        # операция вычитания
        self.top1 = self.pop()
        self.top2 = self.pop()
        self.res =  self.top1 - self.top2
        self.append(self.res)

    def mul(self):
        # операция умножения
        self.top1 = self.pop()
        self.top2 = self.pop()
        self.res = self.top1 * self.top2
        self.append(self.res)

    def div(self):
        # операция целочисленного деления
        self.top1 = self.pop()
        self.top2 = self.pop()
        self.res = self.top1 // self.top2
        self.append(self.res)

def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2, "Деление выполнено неверно"
    ex_stack.sub()
    assert ex_stack.pop() == 6, "Вычитание выполнено неверно"
    ex_stack.sum()
    assert ex_stack.pop() == 7, "Суммирование выполнено неверно"
    ex_stack.mul()
    assert ex_stack.pop() == 2, "Умножение выполнено неверно"
    assert len(ex_stack) == 0, "Стек не пустой"

test()