from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, logout_user
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from admin.Admin import start_views
from controller.User import UserController

config = app_config[app_active]

config.APP = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(config.APP)

config.APP.secret_key = config.SECRET
config.APP.config.from_object(config)
config.APP.config.from_pyfile('config.py')
config.APP.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
config.APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(config.APP)
start_views(config.APP, db)
db.init_app(config.APP)


@config.APP.route('/login', methods=['GET', 'POST'])
def hello_world():
    msg = None
    _type = None

    if request.method == 'POST':
        user = UserController()

        email = request.form['email']
        password = request.form['password']

        result = user.login(email, password)
        import pdb; pdb.set_trace()
        if result:
            if result.role != 1:
                return render_template('login.html',
                                       data={'status': 401, 'msg':
                                             'Seu usuário não tem permissão para\
                                              acessar o admin',
                                             'type': 2})
            else:
                login_user(result)
                return redirect('/admin')
        else:
            msg = "Usuário incorreto ou inexistente"
            _type = 2
    return render_template('login.html', data={'status': 200, 'msg': msg,
                                               'type': _type})


@config.APP.route('/logout')
def logout():
    logout_user()
    return redirect('/login')


@login_manager.user_loader
def load_user(user_id):
    user = UserController()
    return user.get_admin_login(user_id)


if __name__ == '__main__':
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
