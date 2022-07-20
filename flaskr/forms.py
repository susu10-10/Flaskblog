from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from flaskr.models import User


class RegisterForm(FlaskForm):
    fullname = StringField('Full name:',
                            validators=[DataRequired()])

    username = StringField('Username:', 
                            validators=[DataRequired()])

    email = StringField('Email:', 
                        validators=[Email(), DataRequired()])
    password = PasswordField('Password:',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password:', 
                                validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        #check if user submitted is already in our database
        user = User.query.filter_by(username=username.data).first()
        if user: #if user is none then no error but if there is already a user with that name then throw an error
            raise ValidationError('That username is taken. Please choose another username.')

    def validate_email(self, email):
        #check if user submitted is already in our database
        user = User.query.filter_by(email=email.data).first()
        if user: #if user is none then no error but if there is already a user with that name then throw an error
            raise ValidationError('That Email is taken. Please choose another one.')



class LoginForm(FlaskForm):
    email = StringField('Email:', 
                        validators=[Email(), DataRequired()])
    password = PasswordField('Password:',
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class UpdateAccountForm(FlaskForm):
    fullname = StringField('Full name:',
                            validators=[DataRequired()])
    username = StringField('Username:', 
                            validators=[DataRequired()])
    email = StringField('Email:', 
                        validators=[Email(), DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            #check if user submitted is already in our database
            user = User.query.filter_by(username=username.data).first()
            if user: #if user is none then no error but if there is already a user with that name then throw an error
                raise ValidationError('That username is taken. Please choose another username.')

    def validate_email(self, email):
        if email.data != current_user.email:
            #check if user submitted is already in our database
            user = User.query.filter_by(email=email.data).first()
            if user: #if user is none then no error but if there is already a user with that name then throw an error
                raise ValidationError('That Email is taken. Please choose another one.')