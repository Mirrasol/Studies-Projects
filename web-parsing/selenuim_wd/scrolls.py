import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#1. Element scrolling
url = 'https://parsinger.ru/selenium/6/6.5/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    element = browser.find_element('id', 'target')
    browser.execute_script('return arguments[0].scrollIntoView(true);', element)
    element.click()
    time.sleep(10)

#2. Element blocked by another one
url = 'http://parsinger.ru/scroll/4/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    result = 0

    buttons = browser.find_elements('class name', 'btn')
    for button in buttons:
        browser.execute_script('return arguments[0].scrollIntoView(true);', button)
        button.click()
        number = browser.find_element('id', 'result').text
        result += int(number)

    print(result)

#3. Cleaning up uranium
url = 'https://parsinger.ru/selenium/5.7/1/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(2)

    buttons = browser.find_elements(By.CLASS_NAME, 'clickMe')
    for button in buttons:
        browser.execute_script('return arguments[0].scrollIntoView(true);', button)
        button.click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    time.sleep(5)
    print(alert_text)
