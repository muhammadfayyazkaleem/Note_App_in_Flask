from flask import Blueprint, render_template , redirect , request , flash, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash(" Logged in successfully", category="success")
            else:
                flash("Incorrect Password! , try again" ,category='error')
        else:
            flash("Email doesnot Exist." , category='error')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect('/login')

@auth.route('/signup' , methods = ['POST', 'GET'])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        user_name = request.form.get("firstname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = User.query.filter_by(email = email).first()
        if user:
            flash('Email is already Exists', category='error')
        elif len(email) < 6:
            flash('Email must be greater Than 6 characters', category="error")
        elif len(user_name) < 3:
            flash('Name must be greater than 3 characters' , category="error")
        elif password1 != password2:
            flash("Passwords not Match", category="error")
        elif len(password1) < 5:
            flash("Password must be greater than 6", category="error")
        else:
            new_user = User(email=email ,name=user_name , password = generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!" , category="success")
            return redirect(url_for('views.home'))

    return render_template('signup.html')
