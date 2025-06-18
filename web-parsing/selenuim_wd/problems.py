import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/2/2.html'

with webdriver.Chrome() as browser:
    browser.get(url)
