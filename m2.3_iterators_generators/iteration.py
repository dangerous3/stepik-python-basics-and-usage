from random import random

lst = [1, 2, 3, 4, 5, 6]

book = {
    'title' : "The Langoliers",
    'author' : 'Stephen King',
    'year_published' : 1990
}

string = 'Hello, world!'

iterator = iter(book)
print(next(iterator))
print(next(iterator))
print(next(iterator))

# for i in book:
#     print(i)

class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __iter__(self):
        return(self)

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

x = RandomIterator(3)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

for x in RandomIterator(10):
    print(x)

class DoubleElementListIterator:
    def __init__(self, lst):
        self.i = 0
        self.lst = lst

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration

class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)

for pair in MyList([1, 2, 3, 4, 5, 6]):
    print(pair)

def random_generator(k):
    for i in range(k):
        yield random()

gen = random_generator(3)
print(type(gen))

def simple_gen():
    print("Checkpoint 1")
    yield 1
    print("Checkpoint 2")
    yield 2
    print("Checkpoint 3")

gen = simple_gen()
# x = next(gen)
# print(x)
# y = next(gen)
# print(y)
# z = next(gen)

for i in gen:
    print(i)

