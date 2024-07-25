import requests

url = 'https://dzen.ru/'

response = requests.get(url)
print(response.status_code)

