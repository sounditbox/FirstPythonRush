class RevIter:
    def __init__(self, data):
        self.data = data
        self.i = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == -1:
            raise StopIteration
        self.i -= 1
        return self.data[self.i + 1]


class MyList(list):
    def __iter__(self):
        return RevIter(self)


items = MyList([1, 2, 3])
iterator = iter(items)
for item in iterator:
    print(item)

