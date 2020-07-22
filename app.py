from flask import Flask, render_template
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from models.role import Role

config = app_config[app_active]

app = Flask(__name__)
app.secret_key = config.SECRET
app.config.from_object(config)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
db.init_app(app)

@config.APP.route('/')
def hello_world():
    roles = []

    res = db.session.query(Role).all()
    for role in res:
        roles.append({
            'id:': db.i,
            'Role:': db.role
        })

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host=config.IP_HOST, port=config.PORT_HOST)
