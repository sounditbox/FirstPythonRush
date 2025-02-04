
# PUT-запрос
# import requests
# data = {
#  'title': 'foo',
#  'body': 'bar',
#  'userId': 1
# }
# response = requests.put('https://jsonplaceholder.typicode.com/posts/42', json=data)
# print(response.status_code)
# print(response.json())


# DELETE-запрос
# import requests
# response = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
# print(response.status_code)
# print(response.json())


data = {
 'title': 'patched title',
}
# PATCH-запрос

import requests


response = requests.patch('https://jsonplaceholder.typicode.com/posts/42', json=data)
print(response.status_code)
print(response.json())

