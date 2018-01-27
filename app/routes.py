from app import app
from app import db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app.forms import DataForm, LoginForm, RegistrationForm, UpdateForm, DeleteForm
from app.models import Task, User
from datetime import datetime
from flask.json import jsonify

userid= 0

@app.route('/')
@app.route('/home')
def home():
    db.drop_all()
    db.create_all()
    #return redirect(url_for('static',filename='index.html'))
    return render_template('landingpage.html')

@app.route('/test', methods=['GET','POST'])
def test():
    if request.method=='GET':
        return('<form action="/test" method="post"><input type="submit" value="Send" /></form>')

    elif request.method=='POST':
        return "OK this is a post method"
    else:
        return("ok")

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
        userdata = User.query.all()
        for temp_user in userdata:
            if temp_user.username == form.username.data:
                userid = temp_user.id
        login_user(user, remember=form.remember_me.data)
        #next_page = request.args.get('next')
        #if not next_page or url_parse(next_page).netloc != '':
            #next_page = 'landingpage.html'
        return render_template('base.html')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
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
    print userid
    if form.validate_on_submit():
    	return redirect(url_for('/dataPopulate', form= form))
    return render_template('dataentry.html', title='Data Entry', form=form)

@app.route('/dataPopulate', methods=['GET','POST'])
def dataPopulate():
	if request.method == 'POST':
		form = DataForm(request.form)
		newTask = Task(task_heading = form.task_heading.data,
                        task_description = form.task_description.data,
                        due_date = datetime.now(),
                        created_by = userid,
                        status = bool(form.status.data),
                        deleted_by = None,
                        deleted_at = datetime.now(),
                        created_at = datetime.now())
		#db.drop_all()
		#db.create_all()
        db.session.add(newTask)
        db.session.commit()
        allTasks = Task.query.all()
        for temp in allTasks:
            print(temp.task_description)
        return render_template('base.html')
	return 'OK'


@app.route('/dataDisplay')
def dataDisplay():
    allTasks = Task.query.all()
    return render_template('datadisplay.html', tasks=allTasks)

@app.route('/dataUpdateentry', methods= ['GET','POST'])
def dataUpdateEntry():
    form = UpdateForm()
    if form.validate_on_submit():
        return redirect(url_for('/dataUpdate',form= form))
    return render_template('dataupdate.html',title='Data Update',form=form)

@app.route('/dataUpdate', methods = ['GET', 'POST'])
def dataUpdate():
    if request.method == 'POST':
        form = UpdateForm(request.form)
        new_task = Task.query.filter_by(task_heading=form.task_heading.data).update(dict(task_description=form.new_task_description.data))
        db.session.commit()
    return "Update done"

@app.route('/dataDeleteEntry', methods= ['GET','POST'])
def dataDeleteEntry():
    form = DeleteForm()
    if form.validate_on_submit():
        return redirect(url_for('/dataDelete',form= form))
    return render_template('datadelete.html',title='Data Delete',form=form)

@app.route('/dataDelete', methods = ['GET', 'POST'])
def dataDelete():
    if request.method == 'POST':
        form = DeleteForm(request.form)
        new_task = Task.query.filter_by(task_heading=form.task_heading.data).first()
        if new_task.deleted_by:
            return "Task already deleted"
        else:
            new_task.deleted_by = userid
            new_task.deleted_at = datetime.now()
            db.session.commit()
    return "Delete done"


if __name__ == '__main__':
    app.debug = True
    app.run()