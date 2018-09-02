from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Setup

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Setup)

import application.views
import application.models
