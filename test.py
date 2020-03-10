from requests import get, post, delete, put
from pprint import pprint

print(put('http://localhost:5000/api/news/2',
          json={'title': 'Привет'}).json())
