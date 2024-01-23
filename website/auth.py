from flask import Blueprint, render_template , redirect , request , flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
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
        
        if len(email) < 6:
            flash('Email must be greater Than 6 characters', category="error")
        elif len(user_name) < 3:
            flash('Name must be greater than 3 characters' , category="error")
        elif password1 != password2:
            flash("Passwords not Match", category="error")
        elif len(password1) < 5:
            flash("Password must be greater than 6", category="error")
        else:
            flash("Account Created!" , category="success")
    return render_template('signup.html')
