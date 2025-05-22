import requests
from bs4 import BeautifulSoup

html = """
<div>
    <p class="first">Первый абзац.</p>
    <p class="first second">Второй абзац <span>со вложенным</span> текстом.</p>
</div>
"""

def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find_all('p', class_='first')
    for i in tag:
        print(i) 


get_html(html)