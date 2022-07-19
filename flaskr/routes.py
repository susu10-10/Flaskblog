from flask import render_template, redirect, url_for, flash
from flaskr import app
from flaskr.forms import RegisterForm, LoginForm
from flaskr.models import User, Post


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/register/', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!','success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login/', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'su@gmail.com' and form.password.data == '1':
            flash(f'You have been logged in successfully!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful Please check username and password','danger')
    return render_template('login.html', form=form)
