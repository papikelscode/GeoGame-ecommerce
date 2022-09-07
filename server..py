from email.policy import default
import re
from flask import Flask, render_template, request, redirect, url_for,jsonify,abort
# from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
#from werkzeug.security  import generate_password_hash, check_password_hash
from  flask_login import UserMixin, LoginManager, login_required, login_user, logout_user,current_user
#from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

from datetime import datetime
#from flask_marshmallow import Marshmallow


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname((__file__)))
database = "app.db"
con = sqlite3.connect(os.path.join(basedir,database))

app.config['SECRET_KEY'] = "jhkxhiuydu"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,database)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


db = SQLAlchemy(app)




class homepage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Integer, default=0000)
    image_loader = db.Column(db.String(500))

    def __repr__(self):
            return self.title
    def __repr__(self):
        return self.price
    def __repr__(self):
        return image_loader.self
         
db.create_all()
db.session.commit()

class game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Integer, default=0000)
    image_loader = db.Column(db.String(500))

    def __repr__(self):
            return self.title
    def __repr__(self):
        return self.price
    def __repr__(self):
        return image_loader.self
         
db.create_all()
db.session.commit()

class laptops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Integer, default=0000)
    image_loader = db.Column(db.String(500))

    def __repr__(self):
            return self.title
    def __repr__(self):
        return self.price
    def __repr__(self):
        return image_loader.self
         
db.create_all()
db.session.commit()


class store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Integer, default=0000)
    image_loader = db.Column(db.String(500))

    def __repr__(self):
            return self.title
    def __repr__(self):
        return self.price
    def __repr__(self):
        return image_loader.self
         
db.create_all()
db.session.commit()
      
class Secure(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    

admin = Admin(app, name='administration', template_mode='bootstrap3')
admin.add_view(ModelView(homepage, db.session))
admin.add_view(ModelView(game, db.session))
admin.add_view(ModelView(laptops, db.session))
admin.add_view(ModelView(store, db.session))



login_manager = LoginManager()
login_manager.login_view = "signin"
login_manager.init_app(app)
@login_manager.user_loader
def user_loader(homepage_id):
    return homepage.query.get(homepage_id)


@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/games.html')
def games():
    return render_template('games.html')
@app.route('/laptop.html')
def laptop():
    return render_template('laptop.html')
@app.route('/pc.html')
def pc():
    return render_template('pc.html')

@app.route('/about.html')
def about():
    return render_template('about.html')














if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
