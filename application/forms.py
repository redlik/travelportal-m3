from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DecimalField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
from wtforms.fields.html5 import EmailField, URLField

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=15, message="You can use maximum 15 characters")])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Register")

class InsertTourForm(FlaskForm):
    tour_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=25, message="You can use maximum 25 characters")])
    tour_length = SelectField('Tour Length', choices=[('1-day', '1 Day Tour'),('2-day', '2 Days Tour'),('3-day', '3 Days Tour'),('5-day', '5 Days Tour'),('7-day', '7 Days Tour')], validators=[DataRequired()])
    tour_country = SelectField('Tour Location', choices=[('france', 'France'),('ireland', 'Ireland'), ('italy', 'Italy'),('spain', 'Spain'), ('uk', 'United Kingdom'),('us', 'United States')], validators=[DataRequired()])
    tour_price = DecimalField('Tour price', places=2, validators=[DataRequired()])
    tour_description = TextAreaField('Tour Description', validators=[DataRequired()])
    tour_photo1 = URLField('Link to photo 1', validators=[DataRequired()])
    tour_photo2 = URLField('Link to photo 2', validators=[DataRequired()])
    tour_photo3 = URLField('Link to photo 3', validators=[DataRequired()])
    submit = SubmitField("Add Tour")