# coding: utf-8

from flask import Flask, render_template

from flask.ext.sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()

from .admin import admin

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Config.init_app(app)
    db.init_app(app)
    admin.init_app(app)

    from .device import device
    app.register_blueprint(device, url_prefix='/device')
    
    return app
