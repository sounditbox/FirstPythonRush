# SOLID

class MyList(list):
    def __iter__(self):
        return DoubleIterator(self)


class InfiniteIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            self.index = 0
        item = self.data[self.index]
        self.index += 1
        return item


class DoubleIterator:
    def __init__(self, data):
        self.times = 0
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            self.times += 1
            if self.times == 2:
                raise StopIteration
            self.index = 0
        item = self.data[self.index]
        self.index += 1
        return item


# Использование
my_iterable = MyList([1, 2, 3, 4])
for item in my_iterable:
    print(item)
