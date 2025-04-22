import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URL'] = os.getenv('SQLALCHEMY_DATABASE_URL')


if __name__ == "__main__":
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    app.run(host, port)
