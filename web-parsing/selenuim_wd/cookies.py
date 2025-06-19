import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#1. Find cookie value
url = 'https://parsinger.ru/selenium/6/6.3.1/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    cookie = browser.get_cookie('token_22')
    print(cookie['value'])

#2. Find cookies
url = 'https://parsinger.ru/selenium/6/6.3/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    cookies = browser.get_cookies()
    name = cookies[0]['name']
    
    field_filling = browser.find_element('id', 'phraseInput').send_keys(name)
    browser.find_element('tag name', 'button').click()

    result = browser.find_element('id', 'result')
    print(result.text)

#3. Delete cookies
url = 'https://parsinger.ru/selenium/6/6.3.2/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    browser.delete_all_cookies()
    time.sleep(15)

#4. Insert cookies
url = 'https://parsinger.ru/selenium/6/6.3.3/index.html'
cookie = {'name': 'secretKey', 'value': 'selenium123'}

with webdriver.Chrome() as browser:
    browser.get(url)
    browser.add_cookie(cookie)
    browser.refresh()
    result = browser.find_element('id', 'password')
    print(result.text)
