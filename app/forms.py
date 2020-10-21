from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    header = StringField('Task Header', validators=[DataRequired()])
    body = TextField('Task body', validators=[DataRequired()])
    done = BooleanField()
    submit = SubmitField('Add new task')