from app import app
from app import db
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import DataForm, LoginForm, RegistrationForm
from app.forms import UpdateForm, DeleteForm
from app.models import Task, User
from datetime import datetime
# from flask.json import jsonify

userid = 0


@app.route('/')
@app.route('/home')
def home():
    return redirect(url_for('static', filename='index.html'))
    # return render_template('landingpage.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return(
            '<form action="/test" method="post">'
            '<input type="submit" value="Send" /></form>'
        )

    elif request.method == 'POST':
        print request.data
        print request.json
        print request.json['username']
        return 'hello'
    else:
        return("ok")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print 'Congratulations, you are now a registered user!'
        return "Successfully logged in"
        # return redirect(url_for('dataentry'))
    user = User.query.filter_by(username=request.json['username']).first()
    if user is None or not user.check_password(request.json['password']):
        flash('Invalid username or password')
        return redirect(url_for('login'))
        # userid = user.id
    login_user(user, remember=request.json['remember_me'])
    return render_template('base.html')
    # return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(username=request.json['username'],
                    email=request.json['email'])
        user.set_password(request.json['password'])
        db.session.add(user)
        db.session.commit()
        print "inside"
        return jsonify(result=True, id=user.id)


@app.route('/dataentry', methods=['GET', 'POST'])
@login_required
def dataentry():
    form = DataForm()
    print userid
    if form.validate_on_submit():
        return redirect(url_for('/dataPopulate', form=form))
    return render_template('dataentry.html', title='Data Entry', form=form)


@app.route('/dataPopulate', methods=['GET', 'POST'])
def dataPopulate():
    if request.method == 'POST':
        # form = DataForm(request.form)
        newTask = Task(task_heading=request.json['task_heading'],
                       task_description=request.json['task_description'],
                       due_date=datetime.now(),
                       created_by=current_user.id,
                       status=bool(request.json['status']),
                       deleted_by=None,
                       created_at=datetime.now(),
                       deleted_at=datetime.now())
        db.session.add(newTask)
        db.session.commit()
        allTasks = Task.query.all()
        for temp in allTasks:
            print(temp.task_description)
        return render_template('base.html')
    return 'OK'


@app.route('/dataDisplay')
def dataDisplay():
    allTasks = Task.query
    return jsonify({'json_list': [task.serialize for task in allTasks]})
    # return render_template('datadisplay.html', tasks=allTasks)


@app.route('/dataUpdateentry', methods=['POST'])
def dataUpdateEntry():
    form = UpdateForm()
    if form.validate_on_submit():
        return redirect(url_for('/dataUpdate', form=form))
    return render_template('dataupdate.html', title='Data Update', form=form)


@app.route('/dataUpdate', methods=['POST'])
def dataUpdate():
    if request.method == 'POST':
        # form = UpdateForm(request.form)
        new_task = Task.query.filter_by(task_heading=request.json['task_heading']).update(dict(task_description=request.json['new_task_description']))
        db.session.commit()
        return "OK"
    return "OK"


@app.route('/dataDeleteEntry', methods=['GET', 'POST'])
def dataDeleteEntry():
    form = DeleteForm()
    if form.validate_on_submit():
        return redirect(url_for('/dataDelete', form=form))
    return render_template('datadelete.html', title='Data Delete', form=form)


@app.route('/dataDelete', methods=['GET', 'POST'])
def dataDelete():
    if request.method == 'POST':
        # form = DeleteForm(request.form)
        new_task = Task.query.filter_by(task_heading=request.json['task_heading']).first()
        if new_task.deleted_by:
            return "Task already deleted"
        else:
            new_task.deleted_by = current_user.id
            new_task.deleted_at = datetime.now()
            db.session.commit()
    return "Delete done"


if __name__ == '__main__':
    app.debug = True
    app.run()
