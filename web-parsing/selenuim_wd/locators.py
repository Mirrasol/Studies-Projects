import random
import time
import faker
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Ищем каждый второй элемент <p>
url = 'http://parsinger.ru/selenium/3/3.html'

with webdriver.Chrome() as browser:
    result = []
    browser.get(url)
    text_class = browser.find_elements(By.CLASS_NAME, 'text')
    for elem in text_class:
        # second_p = elem.find_elements(By.TAG_NAME, 'p')[1].text
        second_p = elem.find_element(By.CSS_SELECTOR, 'p:nth-child(2)').text
        result.append(second_p)

# print(result[:3])


# 2. Заполняем формы за 3 сек.
url = 'http://parsinger.ru/selenium/1/1.html'
f = faker.Faker()
input_text = {'first_name': f.first_name_female(),
              'last_name': f.last_name_female(),
              'patronymic': f.name_female(),
              'age': random.randint(18, 85),
              'city': f.city(),
              'email': f.email()}

with webdriver.Chrome() as browser:
    browser.get(url)

    forms = browser.find_elements(By.CLASS_NAME, 'form')
    for form in forms:
        form_name = form.get_attribute('name')
        input = form.send_keys(input_text[form_name])

    button = browser.find_element(By.ID, 'btn').click()
    time.sleep(5)

# 3. Найти ссылку с числом
url = 'http://parsinger.ru/selenium/2/2.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_element(By.LINK_TEXT, '16243162441624').get_attribute('href')
    browser.get(link)
    result = browser.find_element(By.ID, 'result').text
    print(result)
