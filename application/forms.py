from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=15, message="You can use maximum 15 characters")])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Register")

