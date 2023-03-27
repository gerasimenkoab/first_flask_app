from flask import render_template
from app import app

@app.route('/')
def index_1():
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
def index_2():
    return(render_template("index.html",title="The best", user ={"username":"Pepega"}))

@app.route('/shmindex')
def index_3():
    return(render_template("base_template.html"))
