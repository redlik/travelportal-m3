from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config')
app.config.from_pyfile('config.py')

app.config["MONGO_URI"] = 'mongodb://localhost:27017/flask_m3_project'
app.config["SECRET_KEY"] = '9nfZWZfPNd'
database = PyMongo(app)



from application import routes