from app import app
from app import db
from flask import redirect, url_for, request, jsonify
from flask_login import login_user, logout_user
from flask_login import current_user
from app.models import Task, User
from datetime import datetime
from sqlalchemy.exc import IntegrityError


@app.route('/')
@app.route('/home')
def home():
    return redirect(url_for('static', filename='index.html'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = User.query.filter_by(username=request.json['username']).first()
    if user is None or not user.check_password(request.json['password']):
        return jsonify({'err': "Invalid username or password"}), 500
    else:
        login_user(user, remember=request.json['remember_me'])
        return jsonify({'success': "Successfully logged in"})


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            user = User(username=request.json['username'],
                        email=request.json['email'])
            user.set_password(request.json['password'])
            db.session.add(user)
            db.session.commit()
            return jsonify({'success': "User registered"}), 200
        except IntegrityError as e:
            print "Error" + repr(e)
            return jsonify({'err': "User already exists"}), 500


@app.route('/dataPopulate', methods=['POST'])
def dataPopulate():
    try:
        newTask = Task(task_heading=request.json['task_heading'],
                       task_description=request.json['task_description'],
                       due_date=datetime.strptime(request.json['due_date'],
                                                  '%Y-%m-%d %H:%M:%S'),
                       created_by=current_user.id,
                       status=bool(request.json['status']),
                       created_at=datetime.now())
        db.session.add(newTask)
        db.session.commit()
        return jsonify({'success': "Task created"}), 200
    except IntegrityError as e:
            print "Error" + repr(e)
            return jsonify({'err': "Task heading already exists"}), 500

    return jsonify({'success': "Task created"}), 200


@app.route('/dataDisplay', methods=['GET', 'POST'])
def dataDisplay():
    allTasks = Task.query.filter_by(created_by=current_user.id)
    return jsonify({
                   'json_list': [task.serialize for task in allTasks]}), 200


@app.route('/dataUpdate', methods=['POST'])
def dataUpdate():
    exists = db.session.query(Task.id).filter_by(
        task_heading=request.json['task_heading']).scalar() is not None
    task_creator = Task.query.filter_by(task_heading=request.json[
                                        'task_heading']
                                        ).first()
    if exists:
        if task_creator.created_by != current_user.id:
            return jsonify({'err': "Update not authenticated"}), 500
        Task.query.filter_by(
            task_heading=request.json['task_heading']
        ).update(
            dict(
                task_description=request.json['new_task_description'],
                status=bool(request.json['new_status']),
                due_date=datetime.strptime(request.json['new_due_date'],
                                           '%Y-%m-%d %H:%M:%S')
            )
        )
        db.session.commit()
        return jsonify({'success': "Task updated"}), 200
    return jsonify({'err': "Task cannot be updated"}), 500


@app.route('/dataDelete', methods=['POST'])
def dataDelete():
    exists = db.session.query(Task.id).filter_by(
        task_heading=request.json['task_heading']).scalar() is not None
    if exists:
        new_task = Task.query.filter_by(
            task_heading=request.json['task_heading']).first()
        if new_task.created_by != current_user.id:
            return jsonify({'err': "Delete not authenticated"}), 500
        if new_task.deleted_by:
            return jsonify({'err': "Task already deleted"}), 500
        else:
            new_task.deleted_by = current_user.id
            new_task.deleted_at = datetime.now()
            db.session.commit()
        return jsonify({'success': "Delete deleted"}), 200
    return jsonify({'err': "Task cannot be deleted"}), 500


if __name__ == '__main__':
    app.debug = True
    app.run()
