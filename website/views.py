from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/' , methods = ['GET', 'POST'])
@login_required
def home():
    if request.method=='POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
    return render_template('home.html' , user = current_user)