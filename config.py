import os


class Config(object):
    CSRF_ENABLE = True
    SECRET = 'ng+=+igi7)5990c=bpy&zk$w=)%=3z(-@$03s!_-8t%4o+r8i8'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None


class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = 'sqllite:///' + os.path.join(ROOT_DIR,
                                                           'db.sqlite3')


class ProductionConfig(Config):
    TESTING = False
    DEBUG = True
    IP_HOST = 'http://pivotostes.com'
    PORT_HOST = 8000
    URL_MAIN = IP_HOST


app_config = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')

app_config[app_active]
