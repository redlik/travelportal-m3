import os
from flask import Flask, render_template, url_for, request, redirect, flash, session
from flask_pymongo import PyMongo
from forms import LoginForm, RegistrationForm, InsertTourForm
from slugify import slugify
from bson import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['SECRET_KEY'] = '9nfZWZfPNd'

database = PyMongo(app)

@app.route("/")
def index():
    tours = database.db.tours.find()
    return render_template("index.html", page_title="Welcome to Travelbuddy portal", tours=tours, home_page=True)


@app.route('/tours')
def tours():
    tours_list = database.db.tours.find().sort('tour_length')
    return render_template('tours.html', page_title="Browse through the large selection of our tours", tours=tours_list, tours_page=True)


@app.route('/tours/location/<country>')
def tours_location(country):
    tours_list = database.db.tours.find({"tour_country": country})
    return render_template('tours.html', page_title="Browse through the large selection of our tours", tours=tours_list, country=country, tours_page=True)


@app.route('/tours/length/<length>')
def tours_length(length):
    slug_length = slugify(length)
    tours_list = database.db.tours.find({"tour_length": length})
    return render_template('tours.html', page_title="Browse through the large selection of our tours", tours=tours_list, length=length, tours_page=True)



@app.route('/add-tour', methods=['GET', 'POST'])
def add_tour():
    tours = database.db.tours
    form = InsertTourForm()
    if form.validate_on_submit():
        tour_name = form.tour_name.data
        tour_length = int(form.tour_length.data)
        tour_slug = slugify(tour_name + "-" + str(tour_length) + "-day")
        tour_country = form.tour_country.data
        tour_price = int(form.tour_price.data)
        tour_description = form.tour_description.data
        tour_photo1 = form.tour_photo1.data
        tour_photo2 = form.tour_photo2.data
        tour_photo3 = form.tour_photo3.data
        tour_data = {"tour_name": tour_name, "tour_slug": tour_slug, "tour_length": tour_length, "tour_country": tour_country, "tour_price": tour_price, "tour_description": tour_description, "tour_photo1": tour_photo1, "tour_photo2": tour_photo2,"tour_photo3": tour_photo3, "owner": session["email"]}
        tours.insert(tour_data)
        return redirect(url_for('index'))
    return render_template('add-tour.html', form=form, page_title="Add New Tour")

@app.route('/delete/<tour_id>')
def delete_tour(tour_id):
    tours = database.db.tours
    tours.delete_one({"_id": ObjectId(tour_id)})
    return redirect(url_for('dashboard'))

@app.route('/edit/<tour_id>')
def edit_tour(tour_id):
    tour = database.db.tours.find_one({"_id": ObjectId(tour_id)})
    if 'email' in session:
        if session['email'] == tour['owner']:    
            countries = database.db.countries.find()
            tour_length = database.db.tour_length.find()
            return render_template('edit-tour.html', page_title="Edit Tour", tour=tour, countries=countries, tour_length=tour_length)
    else:
        return redirect(url_for('login'))

@app.route('/update/<tour_id>', methods=['POST'])
def update(tour_id):
    tours = database.db.tours
    existing_tour = tours.find_one({'_id': ObjectId(tour_id)})
    if 'email' in session:
        if session['email'] == existing_tour['owner']:
            tours.update({'_id': ObjectId(tour_id)},
            {
                'tour_name': request.form.get('tourName'),
                'tour_length': int(request.form.get('tourLength')),
                'tour_slug': slugify(request.form.get('tourName') + "-" + str(request.form.get('tourLength')) + "-" + 'days'),
                'tour_country': request.form.get('tourLocation'),
                'tour_price': request.form.get('tourPrice'),
                'tour_description': request.form.get('tourDescription'),
                'tour_photo1': request.form.get('tourPhoto1'),
                'tour_photo2': request.form.get('tourPhoto2'),
                'tour_photo3': request.form.get('tourPhoto3'),
                'owner': session["email"]
            },
            upsert=True)
            return redirect(url_for('dashboard'))
    else: 
        return redirect(url_for('dashboard'))

@app.route('/tour/<tour_slug>')
def tour(tour_slug):
    tours = database.db.tours
    tour = tours.find_one({"tour_slug":tour_slug})
    return render_template('tour.html', tour=tour)
@app.route('/register', methods=['GET', 'POST'])


def register():
    users = database.db.users
    form=RegistrationForm()
    if request.method == "POST": 
        if form.validate():
            email = form.email.data
            first_name = form.first_name.data
            existing_user = users.find_one({"email": email})
            if not existing_user:
                user = {"first_name": first_name, "email": email}
                users.insert(user)
                session["email"] = email
                session["name"] = first_name
                return redirect(url_for('index'))
            else:
                flash('User with this email already exists. Try a different one', 'error')
                return redirect(url_for('register'))
    return render_template('register.html', page_title="Register to become one of our hosts", form=form, register_page=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    users = database.db.users
    form = LoginForm()
    if request.method == "POST": 
        if form.validate():
            email = form.email.data
            existing_user = users.find_one({"email": email})
            if not existing_user:
                flash("User with this email doesn't exist. Please try again or create new account")
            else:
                first_name = existing_user["first_name"]
                session["email"] = email
                session["name"] = first_name
                return redirect(url_for('dashboard'))
    return render_template('login.html', page_title="Login to add, edit or remove your tours", form=form, login_page=True)

@app.route('/dashboard')
def dashboard():
    tours = database.db.tours
    if 'email' in session:
        owner = session["email"]
        user_tours = tours.find({"owner":owner})
        return render_template('dashboard.html', page_title="TravelBuddy Host Dashboard", tours=user_tours)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)