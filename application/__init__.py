import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config.from_pyfile('config.py')

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

database = PyMongo(app)

from application import routes

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)