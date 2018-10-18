from server import fapp, db
from flask import render_template, request, redirect
from datetime import datetime
from models import Country, User

@fapp.route('/login', methods=['GET'])
def show_login():
    time = datetime.time(datetime.now())
    hour = time.hour
    if hour >= 0 and hour < 12:
        message = 'Good Morning'
    elif hour > 12 and hour < 16:
        message = 'Good Afternoon'
    else:
        message = 'Good evening'
    return render_template('public/login.html', message=message)

@fapp.route('/register', methods=['GET'])
def show_register():
    clist = Country.query.all()
    return render_template('public/register.html', countries=clist)

@fapp.route('/register-user', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    country = request.form['country']
    gender = request.form['gender']

    u = User(username=username, password=password, country=country, gender=gender)
    db.session.add(u)
    db.session.commit()

    if u.id:
        return redirect('/login')
    else:
        return 'Failure'

@fapp.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']

    l = User.query.filter_by(username=username, password=password).all()
    if len(l):
        return redirect('/home?username={0}'.format(username))
    else:
        return redirect('/login')

@fapp.route('/home', methods=['GET'])
def show_home():
    username = request.args.get('username')
    userlist = User.query.all()
    return render_template('private/home.html', username=username, userlist=userlist)
