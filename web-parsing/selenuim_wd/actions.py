import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

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

