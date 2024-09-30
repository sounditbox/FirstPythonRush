import pickle
data: dict = pickle.load(open('data.txt', 'rb'))
data['0'] = 42
print(data)
