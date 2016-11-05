import tempfile
import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand



app = Flask(__name__)
bcrypt = Bcrypt(app)
sess = Session()
sess.init_app(app)

app.config['SECRET_KEY'] = 'k21ey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join( tempfile.gettempdir(), 'test12.db')
app.config['SESSION_TYPE'] = 'memcached'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)





from app import views , db
