import tempfile
import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
bcrypt = Bcrypt(app)




app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join( tempfile.gettempdir(), 'test12.db')


db = SQLAlchemy(app)





from app import views , db
