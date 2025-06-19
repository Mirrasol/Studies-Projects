import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#1. Ищем число на рефрешах. 
url = 'https://parsinger.ru/methods/1/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    while True:
        result = browser.find_element(By.ID, 'result').text
        browser.refresh()
        if result.lower() != 'refresh page':
            print(result)
            break

#2. Scroll forth and back.
url = 'https://parsinger.ru/selenium/6/6.2/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    browser.find_element('tag name', 'a').click()
    browser.find_element('tag name', 'a').click()

    browser.back()
    browser.back()

    button = browser.find_element('tag name', 'button').click()
    time.sleep(5)

# 3. Скриншот
url = 'https://parsinger.ru/selenium/6/6.2.1/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    pic = browser.find_element('id', 'this_pic').screenshot('pic.png')

# 4. ActionChains
url = 'https://parsinger.ru/selenium/5.6/3/index.html'

# 5. Field Clear
url = 'https://parsinger.ru/selenium/5.5/1/1.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    fields = browser.find_elements(By.CLASS_NAME, 'text-field')
    for field in fields:
        field.clear()

    browser.find_element('tag name', 'button').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
