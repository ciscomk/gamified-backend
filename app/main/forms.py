from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class HelpForm(Form):
    submit = SubmitField('Submit')

class FinishForm(Form):
    submit = SubmitField('Submit')
