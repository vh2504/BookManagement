from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordRepeat = PasswordField('Password (repeat)', validators=[DataRequired()])
    gmail = StringField('Gmail',validators=[DataRequired()])
    submit = SubmitField('Register')