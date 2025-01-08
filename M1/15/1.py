f = open('data.txt', encoding='utf-8')
for line in f.readlines():
    print(line.rstrip())