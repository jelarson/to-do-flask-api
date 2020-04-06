import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABSE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "app.sqlite")

if __name__ == "__main__":
    app.debug = True
    app.run()