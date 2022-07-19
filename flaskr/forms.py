from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import StringField, SubmitField, PasswordField, BooleanField


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


class LoginForm(FlaskForm):
    email = StringField('Email:', 
                        validators=[Email(), DataRequired()])
    password = PasswordField('Password:',
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')
