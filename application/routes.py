from application import app, database
from flask import render_template, url_for
from slugify import slugify

@app.route("/")
def index():
    # user_collection = database.db.users
    # user_collection.insert({'name': 'John'})
    return render_template("index.html", page_title="Welcome to Travelbuddy portal", home_page=True)

@app.route("/tour")
def tour_name():
    tour = "Paris 7 days"
    tour_name = slugify(tour)
    return render_template("tour.html", tour_name = tour_name)

@app.route('/tours')
def tours():
    return render_template('tours.html', tours_page=True)

@app.route('/register')
def register():
    return render_template('register.html', register_page=True)

@app.route('/login')
def login():
    return render_template('login.html', login_page=True)