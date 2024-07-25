import requests

url = 'https://dzen.ru/'

response = requests.get(url)
status_code = response.status_code
print(status_code)

if status_code == 200:
    print("Test successfully passed")
else: print("Failure")
