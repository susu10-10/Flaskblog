from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
#specify a url for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# create a database instance
db = SQLAlchemy(app)

# importing the routes
from flaskr import routes


app.run()