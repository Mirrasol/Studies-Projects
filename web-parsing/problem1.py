import requests

response = requests.get('https://parsinger.ru/selenium/6/6.3.1/index.html')

print(
    response.status_code,
    response.text,
    response.headers,
    response.cookies,
    sep='\n',
)