l1 = [42, 33, 56, 77, 11]

# for elem in l1:
    # print(elem)

for i in range(len(l1)):
    l1[i] = int(str(l1[i]) * 2) + 1
    # print(f'i:{i}, elem: {l1[i]}')
print(l1)