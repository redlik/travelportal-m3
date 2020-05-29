from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms.fields.html5 import EmailField, URLField
from wtforms_validators import ActiveUrl

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=15, message="You can use maximum 15 characters")])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Register")

class InsertTourForm(FlaskForm):
    tour_name = StringField("Tour Name", validators=[DataRequired(), Length(min=2, max=25, message="You can use maximum 25 characters")])
    tour_length = SelectField('Tour Length', choices=[('1', '1 Day Tour'),('2', '2 Days Tour'),('3', '3 Days Tour'),('5', '5 Days Tour'),('7', '7 Days Tour')], validators=[DataRequired()])
    tour_country = SelectField('Tour Location', choices=[('france', 'France'),('ireland', 'Ireland'), ('italy', 'Italy'),('spain', 'Spain'), ('uk', 'United Kingdom'),('us', 'United States')], validators=[DataRequired()])
    tour_price = IntegerField('Tour price', validators=[DataRequired(), NumberRange(min=1, max=9999, message="Please provide a valid number")])
    tour_description = TextAreaField('Tour Description', validators=[DataRequired()])
    tour_photo1 = StringField('Photo ID 1', validators=[DataRequired(),Length(min=11, max=11, message="A correct ID from Unsplash is 11 characters")])
    tour_photo2 = StringField('Photo ID 2', validators=[DataRequired(),Length(min=11, max=11, message="A correct ID from Unsplash is 11 characters")])
    tour_photo3 = StringField('Photo ID 3', validators=[DataRequired(),Length(min=11, max=11, message="A correct ID from Unsplash is 11 characters")])
    submit = SubmitField("Add Tour")