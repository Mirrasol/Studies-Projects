import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#1. Модальные окна
url = 'http://parsinger.ru/blank/modal/1/index.html'


with webdriver.Chrome() as browser:
    browser.get(url=url)
    browser.find_element(By.ID, 'alert').click()
    time.sleep(2)
    alert = browser.switch_to.alert
    time.sleep(2)
    alert.accept()


#2. Фреймы
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/4/index.html')

    iframe_element = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(iframe_element)

    iframe_content = browser.page_source

    print(iframe_content)


#3. Window size
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/1/')
    browser.set_window_size(1200, 720)
    time.sleep(5)

