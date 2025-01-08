# Duck Typing - если что-то плавает, крякает и летает, как уточка,
# То это что-то является уточкой

class MyIter:
    def __iter__(self):
        return self

    def __next__(self):
        pass


for i in range(5):
    print(i)


i = None
it = iter(range(5))
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break
