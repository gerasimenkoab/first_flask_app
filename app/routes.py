from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User

@app.route('/')
def chat():
    user = {"username":"Vasili"}
    elem_list = [
        {
            "number":1,
            "person":{"username":"Vasili"},
            "msg":"I am turtle!"
        },
        {
            "number":2,
            "person":{"username":"Petrovich"},
            "msg":"Que pasa?"
        }      
    ]
    html_code = render_template('index.html', title ="My", user = user, phraselist = elem_list)
    return(html_code)

@app.route('/index')
def index():
    return(render_template("index.html", title="The best", user ={"username":"Pepega"}))

@app.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember = form.remember_me.data)
        return redirect(url_for('index'))
    return(render_template("login.html", title="sign In", form = form))
