from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Role(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.Stringer(40), unique=True, nullable=False)
