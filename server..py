from email.policy import default
from fileinput import filename
import re
from flask import Flask, render_template, request, redirect, url_for,jsonify,abort,flash
# from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
#from werkzeug.security  import generate_password_hash, check_password_hash
from  flask_login import UserMixin, LoginManager, login_required, login_user, logout_user,current_user
#from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os
from werkzeug.utils import secure_filename

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



UPLOAD_FOLDER = '/static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def show_index():
    full_image = os.path(app.config['UPLOAD_FOLDER'])
    return render_template("index.html", image_loader = full_image)


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
         
# db.create_all()
# db.session.commit()

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
         
# db.create_all()
# db.session.commit()

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
         
# db.create_all()
# db.session.commit()


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
         
# db.create_all()
# db.session.commit()
      
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

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')



@app.route("/dashboard",methods=['GET','POST'])
def productinfo():
    if request.method == 'POST':
        file = request.files['file']
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            file.save(os.path.join(os.getcwd()+'/static', filename))

            newproduct=homepage(title=request.form['productname'],
                                price = request.form['productprice'],
                                image_loader = filename,
                            
                                )
            db.session.add(newproduct)
            db.session.commit()
            return "upload done"
      
       

        
        return jsonify({'status':200,"msg":"post compelete!!!"})

    return render_template("dashboard.html")

@app.route("/db")
def database():
    db.drop_all()
    db.create_all()
    return "Hello done!!!"








if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
