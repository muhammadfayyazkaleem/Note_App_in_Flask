from flask import Blueprint, render_template , redirect

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect('/login')

@auth.route('/signup' , methods = ['POST', 'GET'])
def signup():
    return render_template('signup.html')
