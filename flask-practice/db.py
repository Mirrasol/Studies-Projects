import sqlite3
import os
from flask import Flask, render_template, request

DATABASE = '/tmp/flask.db'
DEBUG = True
SECRET_KEY = 'yoursecret'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flask.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row  # отображаем в виде словаря для удобства
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    pass


@app.route('/')
def index():
    db = get_db()
    return render_template('index.html')
