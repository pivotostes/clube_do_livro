from flask import Flask, render_template
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from models.Role import Role
from models.User import User
from admin.Admin import start_views

config = app_config[app_active]

config.APP = Flask(__name__)
config.APP.secret_key = config.SECRET
config.APP.config.from_object(config)
config.APP.config.from_pyfile('config.py')
config.APP.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
config.APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(config.APP)

start_views(config.APP, db)

db.init_app(config.APP)


@config.APP.route('/')
def hello_world():
    roles = []

    for role in Role.query.all():
        roles.append({
            'id': role.id,
            'name': role.name
        })

    users = []

    for user in User.query.all():
        users.append({
            'id': user.id,
            'name': user.username
        })

    return render_template('login.html', roles=roles, users=users)


if __name__ == '__main__':
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
