import requests

base_url = 'https://captcha-parsinger.ru/search'
my_params = {
    'q': 'python requests',
    'page': 2
}
response = requests.get(base_url, params=my_params)
print(response.url) # Что будет выведено?
