from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask.ext.login import UserMixin
from . import login_manager

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    money = db.Column(db.Integer)
    is_administrator = db.Column(db.Boolean, default=False)
    needs_help = db.Column(db.Boolean, default=False, index=True)
    help_time = db.Column(db.Time)
    finished_scenario = db.Column(db.Boolean, default=False, index=True)
    scenario_time = db.Column(db.Time)
    current_scenario = db.Column(db.Integer, default=10)
    supplement = db.Column(db.Boolean)
	
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
