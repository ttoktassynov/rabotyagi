from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import Types, Openings, Cities
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/openings', methods=['POST', 'GET'])
@login_required
def openings():
    if request.method == "GET":
        types = Types.query.all()
        openings = Openings.query.all()
        cities = Cities.query.all()
        return render_template('openings.html', 
            types=types, rows=openings, cities=cities)
    else:
        name = request.form.get("name")
        type = request.form
        user_id = current_user.id
        city = request.form.get("cities")
        type = request.form.get("types")
        date = datetime.now()
        new_opening = Openings(user_id=user_id,name=name,type=type,city=city,date=date)
        db.session.add(new_opening)
        db.session.commit()
        flash("Вакансия успешно добавлена!")
        return redirect(url_for('main.openings'))
    