import os
from flask import Flask, redirect
from flask_fefset import FEFset
from flask_iam import IAM
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config['SECRET_KEY'] = os.urandom(12).hex()
    app.config['FEFSET_BRAND_NAME'] = 'THE BRAND'
    db = SQLAlchemy()
    db.init_app(app)
    fef = FEFset(frontend='bootstrap4', test=True, role_protection=True)
    fef.nav_menu.append({'name':'Home','url':'/test/blabla/yadayada','role':False})
    fef.init_app(app)
    iam = IAM(db)
    iam.init_app(app)
    with app.app_context():
        db.create_all()
    fef.nav_menu.append({'name':'Admin1','url':'/test/yadayada/blabla','role':'admin'})
    app.extensions['fefset'].add_menu_entry('Admin2','/test/yadayada/blabla',submenu='Submenu')
    @app.route('/')
    def index():
        return redirect('/front')

    return app
