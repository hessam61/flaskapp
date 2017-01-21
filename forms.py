from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SignupForm(Form):
	first_name = StringField('First Name', validators=[DataRequired("First name is required")])
	last_name = StringField('Last Name', validators=[DataRequired("Last name is required")])
	email = StringField('Email', validators=[DataRequired("Email is required")])
	password = PasswordField('Password', validators=[DataRequired("Password is required")])
	submit = SubmitField('Sign Up')
