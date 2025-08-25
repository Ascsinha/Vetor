from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Acsa'}
    posts = [
    {
        'author': {'username': 'Theo'},
        'body': 'Lindo dia em Portland!'
    },
    {
        'author': {'username': 'Eduardo'},
        'body': 'O filme dos Vingadores foi muito legal!'
    },
    {
        'author': {'username': 'Acsa'},
        'body': 'Finalmente estudando Flask!'
    }
    ]
    return render_template('index.html', title='Home' , user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)