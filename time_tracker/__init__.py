from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["ENV"] = "production"

if app.config['ENV'] == "production":
    app.config.from_object('conf.ProductionConfig')
else:
    app.config.from_object('conf.DevConfig')

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///db/{app.config['DB_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import time_tracker.views
db.create_all()