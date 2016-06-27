from flask import render_template, session, redirect, url_for, abort, current_app, flash
from .. import db
from ..models import User
#from ..email import send_email
from . import main
from .forms import NameForm, HelpForm, FinishForm
from flask.ext.login import login_required, current_user
from flask.ext.admin import Admin, BaseView
from .. import admin
from flask.ext.admin.contrib.sqla import ModelView
import datetime
import time
from sqlalchemy import desc


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        #    if current_app.config['LTRRST1179_ADMIN']:
        #       send_email(current_app.config['LTRRST1179_ADMIN'], 'New User',
        #                 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))


@main.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	if current_user.username == username:
		finishform = FinishForm(prefix="finishform")
		helpform = HelpForm(prefix="helpform")
		if helpform.validate_on_submit() and helpform.submit.data:
			#print "help"
			#print helpform.errors
			#print "finish"
			#print finishform.errors
			current_user.money = current_user.money - 5
			current_user.needs_help = True
			current_user.help_time = datetime.datetime.now().time()
			flash('Help is on the way! Do not refresh your browser.')
		elif finishform.validate_on_submit() and finishform.submit.data:
			#print helpform.errors
			#print finishform.errors
			current_user.finished_scenario = True
			current_user.scenario_time = datetime.datetime.now().time()
			flash('Hang back - The customer is coming to check your work. Do not refresh your browser.')
		return render_template('user.html', user=user, finishform=finishform, helpform=helpform)
	return abort(401)

@main.route('/user/scenario')
def loadscenario():
    #Labs use two digits:First digit is lab #, 2nd is advanced level (0=base)
    #Ex: T1A0 = Task 1, Advanced Task 0 (not an advanced task)
    #BGP Lab uses Scenarios: 10-39.
    #IPv6 Lab uses Scenario Range: 40-69
	if current_user.current_scenario == 10:
		return render_template('T1A0.html')
	elif current_user.current_scenario == 11:
		return render_template('T1A1.html')
	elif current_user.current_scenario == 20:
		return render_template('T2A0.html')
	elif current_user.current_scenario == 21:
		return render_template('T2A1.html')
	elif current_user.current_scenario == 22:
		return render_template('T2A2.html')
	elif current_user.current_scenario == 30:
		return render_template('T3A0.html')
	elif current_user.current_scenario == 31:
		return render_template('T3A1.html')
	elif current_user.current_scenario == 40:
		return render_template('T4A0.html')
	elif current_user.current_scenario == 41:
		return render_template('T4A1.html')
	elif current_user.current_scenario == 50:
		return render_template('T5A0.html')
	elif current_user.current_scenario == 51:
		return render_template('T5A1.html')
	elif current_user.current_scenario == 60:
		return render_template('T6A0.html')
	elif current_user.current_scenario == 61:
		return render_template('T6A1.html')
	else:
		return render_template('nomessages.html')

@main.route('/user/supplement')
def loadsupplement():
	if current_user.current_scenario == 10:
		return render_template('sup-T1.html')
	elif current_user.current_scenario == 20:
		return render_template('sup-T2.html')
	elif current_user.current_scenario == 30:
		return render_template('sup-T3.html')
	elif current_user.current_scenario == 40:
		return render_template('sup-T4.html')
	elif current_user.current_scenario == 50:
		return render_template('sup-T5.html')
	elif current_user.current_scenario == 60:
		return render_template('sup-T6.html')
	else:
		return render_template('nomessages.html')

@main.route('/top')
def showtop():
	users = db.session.query(User).order_by(User.money.desc()).all()
	return render_template('top.html', users=users)

@main.route('/change/<scenario>')
def changeScenario(scenario):
	users = User.query.all()
	for u in users:
		u.current_scenario = scenario
	db.session.commit()
	return 'Changes Committed!'

@main.route('/reset/')
def resetUsers():
	users = User.query.all()
	for u in users:
		u.needs_help = False
		u.help_time = datetime.time()
		u.finished_scenario = False
		u.scenario_time = datetime.time()
	db.session.commit()
	return 'Everyon is reset!'


class MyView(BaseView):
    def is_accessible(self):
        return login.current_user.is_authenticated()

admin.add_view(ModelView(User, db.session))
