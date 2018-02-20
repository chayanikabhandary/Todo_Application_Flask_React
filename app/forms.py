from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, BooleanField, SubmitField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class DataForm(FlaskForm):
    task_heading = StringField('Task Heading: ', validators=[DataRequired()])
    task_description = StringField('Task Description: ', 
        validators=[DataRequired()])
    due_date = DateTimeField('Due Date', validators=[DataRequired()], 
        format= '%Y-%m-%d %H:%M:%S')
    status = BooleanField('Status')
    done = SubmitField('Done')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class UpdateForm(FlaskForm):
    task_heading = StringField('Task Heading: ', validators=[DataRequired()])
    new_task_description = StringField('New Task Description: ', 
        validators=[DataRequired()])
    new_due_date = DateTimeField('New Due Date', validators=[DataRequired()], 
        format= '%Y-%m-%d %H:%M:%S')
    new_status = BooleanField('Status')
    done = SubmitField('Done')


class DeleteForm(FlaskForm):
    task_heading = StringField('Task Heading: ', validators=[DataRequired()])
    done = SubmitField('Done')

