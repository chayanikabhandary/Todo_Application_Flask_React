from app import app
from app import db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app.forms import DataForm, LoginForm, RegistrationForm
from app.models import Task, User
from datetime import datetime
from flask.json import jsonify

@app.route('/')
@app.route('/home')
def home():
    db.drop_all()
    db.create_all()
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dataentry'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dataentry')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dataentry'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/dataentry', methods=['GET','POST'])
def dataentry():
    form= DataForm()
    if form.validate_on_submit():
    	return redirect(url_for('/dataPopulate',form= form))
    return render_template('dataentry.html',title='Data Entry',form=form)

@app.route('/dataPopulate', methods=['GET','POST'])
def dataPopulate():
	if request.method == 'POST':
		form = DataForm(request.form)
		newTask = Task(task_description = form.task_description.data,
                        due_date = datetime.now(),
                        created_by = form.created_by.data,
                        status = bool(form.status.data),
                        deleted_by = None,
                        deleted_at = datetime.now(),
                        created_at = datetime.now())
		db.drop_all()
		db.create_all()
        db.session.add(newTask)
        db.session.commit()
        allTasks = Task.query.all()
        print(allTasks)
        return Task.query.get(1)
	return 'OK'

if __name__ == '__main__':
    app.debug = True
    app.run()