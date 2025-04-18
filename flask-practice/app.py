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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'veryverysecret'


@app.route('/homepage')
@app.route('/')
def homepage():
    return render_template('homepage.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'owl' and request.form['password'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    
    return render_template('login.html', title='Login Time')


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
