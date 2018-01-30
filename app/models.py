# from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    task_heading = db.Column(db.String(64), index=True)
    task_description = db.Column(db.String(1024), index=True)
    due_date = db.Column(db.DateTime, nullable=True)
    created_by = db.Column(Integer, ForeignKey('users.id'), nullable=False)
    status = db.Column(db.Boolean)
    deleted_by = db.Column(db.Integer, ForeignKey('users.id'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, task_heading, task_description, due_date, created_by, status, deleted_by, created_at, deleted_at):
        self.task_heading = task_heading
        self.task_description = task_description
        self.due_date = due_date
        self.created_by = created_by
        self.status = status
        self.deleted_by = deleted_by
        self.created_at = created_at
        self.deleted_at = deleted_at

    def dump_datetime(self, value):
        if value is None:
            return ""
        return value.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def serialize(self):
        exists_deleted_by = False
        if self.deleted_by:
            exists_deleted_by = True 
        return{
            'id': self.id,
            'task_heading': self.task_heading,
            'task_description': self.task_description,
            'due_date': self.dump_datetime(self.due_date),
            'created_by': load_user(self.created_by).username,
            'status': self.status,
            'deleted_by': load_user(self.deleted_by).username if self.deleted_by else "",
            'created_at': self.dump_datetime(self.created_at),
            'deleted_at': self.dump_datetime(self.deleted_at)
        }

    def __repr__(self):
        return '<Task {}>'.format(self.task_description)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
