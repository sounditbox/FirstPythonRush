a = ['One', 'Two', 'Three', 'Four']

# i = 0
# while i < len(a):
#     del a[i]
#     i += 1

for i in range(len(a)):
    if i == 2:
        del a[i]
    print(a[i])
