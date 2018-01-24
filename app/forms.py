from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired

class DataForm(FlaskForm):
    task_description = StringField('Task Description: ', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()], format= '%m/%d/%Y')
    status = BooleanField('Status')
    created_by = StringField('Created By: ', validators=[DataRequired()])
    created_at = DateField('Created At', validators=[DataRequired()])
    done = SubmitField('Done')