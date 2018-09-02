from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Setup

app = Flask(__name__)
app.config.from_object(Setup)
db = SQLAlchemy(app)

import application.views
import application.models
