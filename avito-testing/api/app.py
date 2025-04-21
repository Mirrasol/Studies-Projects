import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


if __name__ == "__main__":
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    app.run(host, port)
