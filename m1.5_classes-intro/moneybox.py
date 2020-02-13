class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = int(capacity)
        self.amount = 0


    def can_add(self, v):
        v = int(v)
        # True, если можно добавить v монет, False иначе
        if self.amount + v > self.capacity:
            return False
        else:
            return True

    def add(self, v):
        # положить v монет в копилку
        v = int(v)
        if self.can_add(v):
            self.amount += v

    def get_amount(self):
        return self.amount


money = MoneyBox(10)
print(money.can_add(6))
print(money.can_add(11))
money.add(7)
print(money.get_amount())
money.add(3)
print(money.get_amount())
money.add(1)
print(money.get_amount())
