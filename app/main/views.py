from flask import render_template
from . import main

@main.route('/test',methods=['GET','POST'])
def index():
    return '<h3>Bad password.</h3>'

@main.route('/template',methods=['GET','POST'])
def render():
    return render_template('index.html')
