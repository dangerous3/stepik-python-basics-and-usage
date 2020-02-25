class Buffer():
    def __init__(self):
        # конструктор без аргументов
        self.buffer = []
        self.temp = []

    def add(self, *a):
        if len(self.buffer) <= 5:
            for i in range(len(a)):
                self.temp.append(a[i])
            temp_range = range(len(self.temp))
            for j in temp_range:
                if len(self.buffer) < 5:
                    self.buffer.append(self.temp[0])
                    if len(self.temp) > 1:
                        self.temp = self.temp[1:]
            print(self.temp)
            print(sum(self.buffer))


        else:
                print(sum(self.buffer))
                self.buffer.clear()


    # добавить следующую часть последовательности

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        print(self.buffer)
        #print(self.temp)

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()