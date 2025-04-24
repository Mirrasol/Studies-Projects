# Lesson 13: Sessions.
from flask import Flask, session
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yourverysecrt'
app.permanent_session_lifetime = datetime.timedelta(days=10)  # ставим жизнь сессии, 31 день по умолч.


@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # обновляем данные сессии
    else:
        session['visits'] = 1  # запись данных в сессию
    
    return f'<h1>Main Page</h1><p>Visits count: {session['visits']}</p>'


data = [1, 2, 3, 4]

@app.route('/session')
def session_data():
    session.permanent = True  # вручную прописываем жизнь сессий
    if 'data' not in session:
        session['data'] = data
    else:
        session['data'][1] += 1  # пытаемся поменять двойку в списке
        session.modified = True  # чтобы сохранить и поменять список
    
    return f'<p>>session["data"]: {session['data']}</p>'


# Как только закрыли браузер - сессии пропали.
# Либо вручную прописываем жизнь сессий

if __name__ == "__main__":
    app.run(debug=True)
