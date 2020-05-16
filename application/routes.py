from application import app, database
from flask import render_template, url_for, request
from slugify import slugify
from application.forms import LoginForm, RegistrationForm

@app.route("/")
def index():
    # user_collection = database.db.users
    # user_collection.insert({'name': 'John'})
    return render_template("index.html", page_title="Welcome to Travelbuddy portal", home_page=True)

@app.route('/tours')
def tours():
    return render_template('tours.html', page_title="Browse through the large selection of our tours", tours_page=True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    users = database.db.users
    form=RegistrationForm()
    if request.method == "POST": 
        if form.validate():
            email = form.email.data
            first_name = form.first_name.data
            user = {"first_name": first_name, "email": email}
            users.insert(user)
    return render_template('register.html', page_title="Register to become one of our hosts", form=form, register_page=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', page_title="Login to add, edit or remove your tours", form=form, login_page=True)