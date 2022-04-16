import requests

URL = 'https://api.myanimelist.net/v2/anime'

response = requests.get(URL)
print(response.status_code)