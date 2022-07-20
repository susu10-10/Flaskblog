from flask import render_template, redirect, url_for, flash, request
from flaskr import app, db, bcrypt
from flaskr.forms import RegisterForm, LoginForm, UpdateAccountForm
from flaskr.models import User, Post
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register/', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
    # we go ahead and hash the password and save to the db
        hashed_password = generate_password_hash(form.password.data)
        # create a new instance of a user
        user = User(fullname=form.fullname.data, 
                    username=form.username.data, email=form.email.data,
                    password=hashed_password)
        # add this user to the changes we want to make in our db
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to login','success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login/', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # users will be loggin in with their email, so we query the database, to make sure the user exists
        user = User.query.filter_by(email=form.email.data).first()
        # a cond that simulatneously checks that the user exist and pasword verifies
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # getting the next parameter from the user if it exists
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful Please check username and password','danger')
    return render_template('login.html', form=form)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('login'))


def save_picture(form_picture):
    # create a random hex that will be the base of our filename
    random_hex = secrets.token_hex(8)
    # use os module to get the file extension
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route('/account/', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.fullname = form.fullname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET': #this will populate the input fields with the user info
        form.fullname.data = current_user.fullname
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('account.html', image_file=image_file, form=form)