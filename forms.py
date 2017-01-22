from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First Name', validators=[DataRequired("First name is required")])
	last_name = StringField('Last Name', validators=[DataRequired("Last name is required")])
	email = StringField('Email', validators=[DataRequired("Email is required"), Email("Please enter a valid email address")])
	password = PasswordField('Password', validators=[DataRequired("Password is required"), Length(min=6, message="Password should be at least 6 characters long")])
	submit = SubmitField('Sign Up')

class LoginForm(Form):
	email = StringField('Email', validators = [DataRequired("Please enter your email address"), Email("Please enter a valid email address")])
	password = PasswordField('Password',validators = [DataRequired("Please enter your password")])
	submit = SubmitField('Sign in')

class AddressForm(Form):
	address = StringField('Address', validators = [DataRequired('Please enter an address')])
	submit = SubmitField('Search')