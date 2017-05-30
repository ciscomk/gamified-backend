from flask import Flask
from flask.ext.bootstrap import Bootstrap
#from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.login import LoginManager
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
import flask_wtf
import flask_admin as admin


bootstrap = Bootstrap()
#mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
#login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
admin = Admin()



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #flask_wtf.CsrfProtect(app)

    bootstrap.init_app(app)
    #mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
