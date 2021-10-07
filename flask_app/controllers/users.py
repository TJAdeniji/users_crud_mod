from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.getUser()
    return render_template('users.html', users = users)

@app.route('/users/new')
def newUser():
    return render_template('new_user.html')

@app.route('/users/add_user', methods = ['POST'])
def addUser():
    User.createUser(request.form)
    return redirect('/users')
