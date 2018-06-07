from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
[]
app.config['SECRET_KEY'] = 'd5f26d0322127d1e33f260907633c5c5'

posts = [
    {"author": "shashi troor",
     "title": "first post",
     "content": "first content",
     "date_posted": "June 08,2018"},

    {"author": "suna troor",
     "title": "suna post",
     "content": "first suna content",
     "date_posted": "June 07,2018"}
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
