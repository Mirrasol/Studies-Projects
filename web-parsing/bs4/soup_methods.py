from bs4 import BeautifulSoup

# 1. Parent
html = '''
!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Пример .parent</title>
</head>

<body>
<div id="parent-container">
    <h1 id="main-heading">Заголовок</h1>
    <p id="paragraph">Текст абзаца</p>
    
    <ul id="list">
        <li class="list-item">Элемент списка 1</li>
        <li class="list-item">Элемент списка 2</li>
    </ul>
</div>

</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
paragraph = soup.find('p', id='paragraph')
parent_div = paragraph.parent
print(parent_div)

# 2. Text / get_text()
html_string = """
<div>
    <p>Первый абзац.</p>
    <p>Второй абзац <span>со вложенным</span> текстом.</p>
</div>
"""

soup = BeautifulSoup(html_string, 'html.parser')
div_text = soup.find('div').get_text(separator=" | ")
print(div_text)

# 3. Find() / find_all()
html2 = """
<html>
    <body>
        <h1>Заголовок</h1>
        <p>Первый абзац</p>
    </body>
</html>
"""
soup = BeautifulSoup(html2, "html.parser")

p = soup.find("p")
print(p)           # <p>Первый абзац</p>
print(p.text)      # Первый абзац

html3 = """
<ul>
  <li class="item">Пункт 1</li>
  <li class="item special">Пункт 2</li>
  <li class="item">Пункт 3</li>
</ul>
"""
soup = BeautifulSoup(html3, "html.parser")

special = soup.find("li", {"class": "special"})  # class find
special = soup.find("li", class_="special")  # kwargs find

print(special)     # <li class="item special">Пункт 2</li>

# 4. Select() / select_one()
html4 = """
<html>
  <body>
    <p class="highlight">This is a highlighted paragraph.</p>
    <p>This is a normal paragraph.</p>
    <div id="div1">
      <p>This is a paragraph in a div.</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html4, "html.parser")

highlighted_paras = soup.select(".highlight")  # все параграфы с классом "highlight"
for para in highlighted_paras:
    print(para.text)

print('----разделитель----')

div_paras = soup.select("#div1 p")  # все параграфы, находящиеся внутри элемента с идентификатором "div1"
for para in div_paras:
    print(para.text)

