# Here we will import the forms package
from flask_wtf import FlaskForm
# Here we will import the package for creating field in the forms. 
# SubmitField will help in sending the user input data to us 
from wtforms import StringField, PasswordField, SubmitField, BooleanField
# Here we will create the validators mainly required for the set of conditions to be implied on the textual inputs. 
# EqualTO validator will make sure that both of the passed data of flaskform should be equal.
from wtforms.validators import DataRequired, Length, Email, EqualTo

# This class will create a registration form having 'username' and validators required for setting limitations on the user input such as length of username and such. 
# Data required is like the class for the validators which will set the field should not be empty 
class RegistrationForm(FlaskForm):
  username = StringField('username', validators = [DataRequired(),       Length(min = 4, max = 12)])
  email = StringField('Email ID', validators = [DataRequired(), Email()])
  password = PasswordField('Password', validators = [DataRequired(),       Length(min = 3, max = 7)])
  confirm_password = PasswordField('Password', validators = [DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
  email = StringField('Email ID', validators = [DataRequired(), Email()])
  password = PasswordField('Password', validators = [DataRequired(),       Length(min = 3, max = 7)])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Log In')