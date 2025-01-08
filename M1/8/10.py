# a = [1, 2]
# a.insert(1, a)
# print(a)
# print(a[1])
# print(a[1][1])

d = {'key': 'value', 'key2': 42}
d['self'] = d
print(d)
print(d['self'])
