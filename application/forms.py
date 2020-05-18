from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DecimalField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
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
    tour_length = SelectField('Tour Length', choices=[('1 Day', '1 Day Tour'),('2 Days', '2 Days Tour'),('3 Days', '3 Days Tour'),('5 Days', '5 Days Tour'),('7 Days', '7 Days Tour')], validators=[DataRequired()])
    tour_country = SelectField('Tour Location', choices=[('france', 'France'),('ireland', 'Ireland'), ('italy', 'Italy'),('spain', 'Spain'), ('uk', 'United Kingdom'),('us', 'United States')], validators=[DataRequired()])
    tour_price = DecimalField('Tour price', places=2, validators=[DataRequired()])
    tour_description = TextAreaField('Tour Description', validators=[DataRequired()])
    tour_photo1 = StringField('Photo ID 1', validators=[DataRequired(),Length(min=11, max=11)])
    tour_photo2 = StringField('Photo ID 2', validators=[DataRequired(),Length(min=11, max=11)])
    tour_photo3 = StringField('Photo ID 3', validators=[DataRequired(),Length(min=11, max=11)])
    submit = SubmitField("Add Tour")