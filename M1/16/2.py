from pprint import pprint

import requests

response = requests.get('http://google.com')
print(response.status_code)
# with open('google.html', 'wb') as f:
#     f.write(response.content)
print(response.headers)