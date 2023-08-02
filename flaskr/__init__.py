from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
#specify a url for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# create a database instance
db = SQLAlchemy(app)

#initalize the Bcrypt
bcrypt = Bcrypt(app) 
# i didnt use this one again i made use of werzeug.security
# has it has generated and check password hash

#instance of login
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# importing the routes
from flaskr import routes



#
#db.create_all()

app.run()