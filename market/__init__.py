from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
# This secret key is generated once by doing os.urandom(12).hex() in cmdline. This is a security layer needed to make forms work.
app.config["SECRET_KEY"] = "a6281b9267cd2386fa4f8474"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

# to let __init__ file recognize the routes we created -- when import, then python will execute routes.py
from market import routes
