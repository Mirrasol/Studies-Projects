from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/homepage')
@app.route('/')
def homepage():
    return render_template('homepage.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/profile/<path:username>')  # конвертеры для обозначения пути (int=только цифры, path=любые допустимые символы и слэш и тд)
def profile(username):
    return f'Current user: {username}'


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print(request.form)
        print(request.form['email'])
        
    return render_template('contact.html', title='Contact Us')


# with app.test_request_context():
#     print(url_for('about'))
#     print(url_for('profile', username='Wyll'))

if __name__ == "__main__":
    app.run(debug=True)  # для тестов в dev-среде
