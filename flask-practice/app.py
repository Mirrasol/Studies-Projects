from datetime import datetime
from werkzeug.security import generate_password_hash
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/my_db'  # 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.column(db.String(50), unique=True)
    psw = db.column(db.String(500), nullable=False)
    date = db.column(db.DateTime, default=datetime.now)

    pr = db.relationship('Profile', backref='user', uselist=False)  # создаем отношения, главный класс = юзер, плюс все подходящие данные из профилей, один к одному

    def __repr__(self):
        return f"<users {self.id}>"


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String(50), nullable=False)
    age = db.column(db.Integer)
    city = db.column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<profiles {self.id}>"


@app.route("/")
def index():
    info = []
    try:
        info = User.query.all()
    except:
        print('Error')

    return render_template('index.html', title='Main page')


@app.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":
        # validation here
        try:
            hash = generate_password_hash(request.form['psw'])
            user = User(email=request.form['email'], psw=hash)
            db.session.add(user)  # запись пока еще только в сессии
            db.session.flush()  # перемещает запись из сессии в табл, но не в бд пока что

            profile = Profile(name=request.form['name'], age=request.form['age'],
                               city=request.form['city'], user_id=user.id)
            db.session.add(profile)
            db.session.commit()  # вот тут сохраняем в бд
        except:
            db.session.rollback()

    return render_template('register.html', title="Registration")


if __name__ == "__main__":
    app.run(debug=True)
