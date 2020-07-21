from flask_admin import Admin


def start_view(app, db):

    admin = Admin(app, name='Meu Sistema', template_mode='bootstrap3')
