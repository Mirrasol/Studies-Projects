from flask import (
    Flask,
    abort,
    flash,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'veryverysecret'


@app.route('/homepage')
@app.route('/')
def homepage():
    return render_template('homepage.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/login')
def login():    
    return render_template('login.html', title='Login Time')

# Ставим куки при логине
# @app.route('/login')
# def login():
#     log = '' 
#     if request.cookies.get('logged'):
#         log = request.cookies.get('logged')
    
#     res = make_response(f'<h1>Authorization Form</h1><p>logged: {log}</p>')
#     res.set_cookie('logged', 'yes', 30*24*3600)  # куки хранятся 30 дней тут
#     return res

@app.route('/logout')
def logout():
    res = make_response('<p>No longer authorized</p>')
    res.set_cookie('logged', '', max_age=0)  # в нек.браузерах все равно не очищается, пока браузер не закроешь
    return res


# Для хеша паролей: из werkzeug generate_password_hash('1223') + check_password_hash(hash, '1223')
@app.route('/register', methods=['GET', "POST"])
def register():
    if request.method == 'POST':
        if len(request.form['username']) > 4 and len(request.form['password1']) > 4 \
            and len(request.form['password2']) > 4 \
            and request.form['password1'] == request.form['password2']:
            hash = generate_password_hash(request.form['password1'])
            result = 1  # какая-то наша логика добавки в бд
            if result:
                flash('User has been registered successfully', category='success')
                return redirect(url_for('login'))
            else:
                flash('Oh my, some error occured while registering', category='danger')

    return render_template('register.html', title='Welcome, welcome!')


@app.route('/profile/<path:username>')  # конвертеры для обозначения пути (int=только цифры, path=любые допустимые символы и слэш и тд)
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return render_template('profile.html', title='Your Profile', username=username)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if '@' not in request.form['email']:
            flash('Invalid email', category='danger')
        else:
            flash('Email has been sent!', category='success')

        print(request.form)
        print(request.form['email'])
        
    return render_template('contact.html', title='Contact Us')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', title='Got Lost?'), 404

# with app.test_request_context():
#     print(url_for('about'))
#     print(url_for('profile', username='Wyll'))


@app.route('/index')
def index():
    # res = make_response('<h1>Server Error</h1>', 500)
    content = render_template('index.html', title='Index')
    res = make_response(content)
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'flask-practice'
    return res


@app.route('/transfer')
def transfer():
    return redirect(url_for('index'), 301)  # 301 = permanently moved, 302 = temporarily moved


if __name__ == "__main__":
    app.run(debug=True)  # для тестов в dev-среде
