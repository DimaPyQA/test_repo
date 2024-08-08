import requests

urls = [
    'https://dzen.ru/',
    'https://dzen.ru/news?utm_referrer=dzen.ru',
    'https://dzen.ru/pogoda/krasnoznamensk-moscow-region?lat=55.600507&lon=37.042492'
]

for url in urls:
    response = requests.get(url)
    status_code = response.status_code
    print(status_code)
    if status_code == 200:
        print("Test successfully passed")
    else: print("Failure")
