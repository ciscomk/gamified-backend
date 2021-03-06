from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.user', username=form.username.data))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)   

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		if form.money.data == '100':
			sup = False
		else:
			sup = True
		user = User(username=form.username.data, password=form.password.data, money=form.money.data, supplement = sup)
		db.session.add(user)
		flash('You may now login.')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)
			
			
