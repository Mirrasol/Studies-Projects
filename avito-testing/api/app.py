import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
from pydantic import ValidationError

from api.data import CreateAdvertismentDTO
from api.db import db

# from api.models import AdvertisementModel
from api.service import create_advertisment_service

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db.init_app(app)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return '<p>Advertisments!</p>'


@app.post('/advertisments')
def create_advertisment():
    body = request.json
    body['photos'] = ", ".join(body['photos'])

    try:
        body = CreateAdvertismentDTO(**body)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    return jsonify(dict(create_advertisment_service(db, body)))


@app.get('/advertisments')
def get_advertisments():
    pass


@app.get('/advertisments/search')
def search_advertisments():
    pass


def main():
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    app.config['DEBUG'] = os.getenv('DEBUG')
    app.run(host, port)


if __name__ == "__main__":
    main()
