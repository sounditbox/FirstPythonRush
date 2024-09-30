f = open('data.txt', mode='a', encoding='utf-8')
f.writelines(map(lambda x: x+'\n', ['123', 'abc', 'xyz']))
f.close()
