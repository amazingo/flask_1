from flask import Flask
from flask import request
from flask import render_template
import os
import sqlite3

def create_app():
    print os.getcwd()
    app=Flask(__name__)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app

