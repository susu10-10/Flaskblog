from flask import Flask, render_template, url_for, redirect, flash
from form import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit()
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
