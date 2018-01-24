from app import app
from flask import render_template
from app.forms import DataForm

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    form= DataForm()
    if form.validate_on_submit():
    	return redirect('/index')
    return render_template('login.html',title='Data Entry',form=form)