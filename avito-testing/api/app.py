import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return '<p>Advertisments!</p>'


@app.route('/advertisments')
def create_advertisment():
    pass


if __name__ == "__main__":
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    app.run(host, port)
