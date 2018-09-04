import os
import sqlite3
from flask import Flask, request, session, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
'''app.config.from_object(os.environ['APP_SETTING'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
'''
app.config['SQLALCHEMY_DATABASE_URI']=\
        'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db= SQLAlchemy(app)

from models import Result

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')



@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
