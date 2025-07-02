import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options

#1. Scrolling

# options = Options()
# options.add_argument("--headless")  # Без графического интерфейса
# options.add_argument('--disable-gpu')  # Отключаем GPU
# options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

url = 'https://parsinger.ru/selenium/7/7.4.1/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    div = browser.find_element(By.CLASS_NAME, 'long-page')
    for _ in range(5):
        actions = ActionChains(browser)
        actions.scroll_by_amount(0, 500).perform()
        time.sleep(5)

#2. Drag and Drop
url = "https://parsinger.ru/selenium/5.10/1/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)

    draganddrop = browser.find_element(By.CLASS_NAME, "draganddrop")
    draganddrop_end = browser.find_element(By.CLASS_NAME, "draganddrop_end")

    ActionChains(browser).drag_and_drop(draganddrop, draganddrop_end).perform()
    time.sleep(5)

#3. Пример каптчи
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.10/5/index.html')

    slider = browser.find_element(By.ID,'volume')
    width = slider.size['width']

    offset = width / 100

    actions = ActionChains(browser)

    actions.click_and_hold(slider).perform()

    for _ in range(10):  # пример для 10 шагов
        actions.move_by_offset(offset, 0).perform()
        time.sleep(0.1)  # пауза для наглядности

    actions.release().perform()
