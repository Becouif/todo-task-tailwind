from wsgiref.validate import validator

from flask_wtf import FlaskForm
from wtforms import  StringField,SelectField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    # id = StringField('ID', validators=[DataRequired()])
    task= StringField('Task', validators=[DataRequired()])
    priority = SelectField('Priority', choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')])
    status = SelectField('Status', choices=[('in progress', 'In Progress'), ('pending', 'Pending'),('completed', 'Completed')])
    submit = SubmitField('Submit')